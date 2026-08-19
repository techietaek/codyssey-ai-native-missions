"""국내 여행 추천 CLI 프로그램.

흐름:
  [1/3] LLM으로 1차 추천(JSON) 생성
  [2/3] 지도 API로 추천 도시의 맛집 검색
  [3/3] LLM으로 최종 여행 리포트(Markdown) 생성

결과물:
  results/{date}_raw.json           원본 데이터(1차 추천 + 맛집 + errors)
  results/{date}_travel_plan.md     최종 리포트

사용 예:
  python travel_planner.py --date 2026-03-15
  python travel_planner.py --date 2026-03-15 --mock
  python travel_planner.py --date 2026-03-15 --llm gemini --map naver --multi 2
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# python-dotenv는 선택 의존성. 없으면 조용히 건너뛰고 OS 환경변수만 사용한다.
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from errors import ApiError
from llm_client import LLMClient
from place_client import PlaceClient
from report import build_markdown_fallback, normalize_cities

RESULTS_DIR = Path("results")


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="travel_planner.py",
        description="LLM + 지도 API로 국내 여행 리포트를 생성합니다.",
    )
    parser.add_argument(
        "-d", "--date", required=True, metavar="YYYY-MM-DD",
        help="여행 날짜 (필수). 예: 2026-03-15",
    )
    parser.add_argument("--llm", choices=["openai", "gemini"], default="openai",
                        help="LLM 제공자 (기본: openai)")
    parser.add_argument("--map", dest="map_provider", choices=["kakao", "naver"], default="kakao",
                        help="지도/장소 검색 제공자 (기본: kakao)")
    parser.add_argument("--multi", type=int, default=1, metavar="N",
                        help="복수 지역 추천 개수 (보너스, 기본: 1)")
    parser.add_argument("--count", type=int, default=5, metavar="N",
                        help="도시별 맛집 검색 개수 (기본: 5)")
    parser.add_argument("--mock", action="store_true",
                        help="실제 API 없이 샘플 데이터로 전체 흐름 실행")
    parser.add_argument("--cache", action="store_true",
                        help="같은 날짜의 원본 JSON이 있으면 API 호출을 건너뛰고 리포트만 재생성")
    return parser.parse_args(argv)


def validate_date(date_str: str) -> str:
    """YYYY-MM-DD 형식 검증. 실패 시 SystemExit."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"[오류] 날짜 형식이 올바르지 않습니다: {date_str!r}", file=sys.stderr)
        print('       올바른 형식: --date "YYYY-MM-DD" (예: 2026-03-15)', file=sys.stderr)
        raise SystemExit(2)
    return date_str


def die_missing_key(kind: str, names: list[str]) -> None:
    """키 미설정 시 안내 후 종료."""
    print(f"[오류] {kind} API 키가 설정되지 않았습니다.", file=sys.stderr)
    print("       .env 파일 또는 환경변수로 아래 키를 설정하세요:", file=sys.stderr)
    for n in names:
        print(f"         {n}", file=sys.stderr)
    print("       예) export OPENAI_API_KEY=\"YOUR_KEY\"", file=sys.stderr)
    print("       (실제 키 없이 테스트하려면 --mock 옵션을 사용하세요.)", file=sys.stderr)
    raise SystemExit(1)


def check_keys(args) -> None:
    """API 키 미설정이면 즉시 종료 + 설정 방법 안내."""
    if args.mock:
        return
    import os

    if args.llm == "openai" and not os.getenv("OPENAI_API_KEY"):
        die_missing_key("OpenAI LLM", ["OPENAI_API_KEY"])
    if args.llm == "gemini" and not os.getenv("GEMINI_API_KEY"):
        die_missing_key("Gemini LLM", ["GEMINI_API_KEY"])
    # 지도 키는 없어도 맛집=데이터 없음으로 계속 진행하지만, 사전 경고만 출력한다.


def run(args) -> None:
    date = validate_date(args.date)
    RESULTS_DIR.mkdir(exist_ok=True)
    raw_path = RESULTS_DIR / f"{date}_raw.json"
    md_path = RESULTS_DIR / f"{date}_travel_plan.md"

    errors: list[dict] = []

    # --- 캐싱(보너스): 원본 JSON이 있으면 API 스킵 ---
    cached = None
    if args.cache and raw_path.exists():
        try:
            cached = json.loads(raw_path.read_text(encoding="utf-8"))
            print(f"[캐시] {raw_path} 를 재사용합니다 (API 호출 건너뜀).")
        except (ValueError, OSError):
            cached = None

    llm = LLMClient(provider=args.llm, mock=args.mock)

    if cached:
        recommendation = cached.get("recommendation", {})
        places_by_city = cached.get("places_by_city", {})
        errors = cached.get("errors", [])
    else:
        check_keys(args)

        # [1/3] 1차 추천
        print("[1/3] 1차 추천 생성 중(LLM)...")
        try:
            recommendation = llm.recommend(date, count=max(1, args.multi))
        except ApiError as exc:
            print(f"    - 오류: {exc.message}", file=sys.stderr)
            print("    - 1차 추천에 실패하여 진행할 수 없습니다.", file=sys.stderr)
            raise SystemExit(1)
        cities = normalize_cities(recommendation)
        print(f"    - recommended_city: {', '.join(cities) if cities else '(없음)'}")

        # [2/3] 맛집 검색
        print("[2/3] 맛집 검색 중(지도/장소 API)...")
        places_by_city = {}
        place_client = PlaceClient(provider=args.map_provider, mock=args.mock)
        if not args.mock and not place_client.has_key():
            print("    - 경고: 지도 API 키 미설정 → 맛집 섹션을 '데이터 없음'으로 처리합니다.")
            errors.append({
                "step": "place_search", "type": "AUTH_ERROR",
                "message": "지도 API 키가 설정되지 않음",
            })
            for c in cities:
                places_by_city[c] = []
        else:
            for city in cities:
                try:
                    places = place_client.search_restaurants(city, size=args.count)
                    places_by_city[city] = places
                    if places:
                        print(f"    - [{city}] 맛집 {len(places)}곳 검색 완료")
                    else:
                        print(f"    - [{city}] 검색 결과 0건 → 데이터 없음으로 진행")
                        errors.append({
                            "step": "place_search", "type": "EMPTY_RESULT",
                            "message": f"0 results for query={city} 맛집",
                        })
                except ApiError as exc:
                    print(f"    - [{city}] 오류: {exc.message}")
                    print("    - 맛집 섹션은 '데이터 없음'으로 처리하고 계속 진행합니다.")
                    places_by_city[city] = []
                    errors.append(exc.to_dict())

    # [3/3] 최종 리포트
    print("[3/3] 최종 리포트 생성 중(LLM)...")
    try:
        report_md = llm.make_report(date, recommendation, places_by_city, errors)
    except ApiError as exc:
        print(f"    - 오류: {exc.message} → 폴백 리포트를 생성합니다.")
        errors.append(exc.to_dict())
        report_md = build_markdown_fallback(date, recommendation, places_by_city, errors)
    print("    - 리포트 생성 완료")

    # --- 저장 ---
    raw_payload = {
        "date": date,
        "recommendation": recommendation,
        "places_by_city": places_by_city,
        "errors": errors,
    }
    raw_path.write_text(json.dumps(raw_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(report_md, encoding="utf-8")

    print()
    print(f"완료! {md_path} 를 확인하세요.")
    print(f"      원본 데이터: {raw_path}")
    if errors:
        print(f"      (오류 {len(errors)}건이 errors 섹션에 기록되었습니다.)")


def main(argv=None) -> None:
    args = parse_args(argv)
    run(args)


if __name__ == "__main__":
    main()
