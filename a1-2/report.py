"""최종 리포트(Markdown) 생성 유틸.

LLM으로 리포트를 생성하는 것이 기본이지만, mock 모드이거나 LLM 리포트
생성이 실패했을 때 사용할 수 있는 결정적(deterministic) 폴백 생성기를 제공한다.
"""

from __future__ import annotations


def normalize_cities(recommendation: dict) -> list[str]:
    """1차 추천 dict에서 도시 목록을 뽑아낸다(단일/복수 스키마 모두 지원)."""
    cities = recommendation.get("recommended_cities")
    if isinstance(cities, list) and cities:
        return [str(c) for c in cities]
    city = recommendation.get("recommended_city")
    if city:
        return [str(city)]
    return []


def build_markdown_fallback(
    date: str, recommendation: dict, places_by_city: dict, errors: list
) -> str:
    """LLM 없이도 요구 섹션을 모두 만족하는 Markdown 리포트를 만든다."""
    cities = normalize_cities(recommendation)
    weather = recommendation.get("weather", "정보 없음")
    events = recommendation.get("events", []) or []
    reason = recommendation.get("reason", "정보 없음")

    lines: list[str] = []
    lines.append(f"# {date} 국내 여행 추천 리포트")
    lines.append("")

    lines.append("## 추천 지역")
    lines.append(", ".join(cities) if cities else "정보 없음")
    lines.append("")

    lines.append("## 추천 이유")
    lines.append(reason)
    lines.append("")

    lines.append("## 날씨 요약")
    lines.append(weather)
    lines.append("")

    lines.append("## 행사/축제")
    if events:
        for e in events:
            lines.append(f"- {e}")
    else:
        lines.append("- 데이터 없음")
    lines.append("")

    lines.append("## 맛집 추천")
    if not cities:
        lines.append("- 데이터 없음 (추천 지역 없음)")
    for city in cities:
        if len(cities) > 1:
            lines.append(f"### {city}")
        places = places_by_city.get(city, [])
        if not places:
            lines.append("- 데이터 없음 (장소 검색 결과 0건)")
        else:
            for p in places:
                parts = [f"**{p.get('name', '')}**"]
                if p.get("category"):
                    parts.append(p["category"])
                detail = " · ".join(parts)
                addr = p.get("address", "")
                url = p.get("url", "")
                line = f"- {detail}"
                if addr:
                    line += f" — {addr}"
                if url:
                    line += f" ([링크]({url}))"
                lines.append(line)
        lines.append("")

    lines.append("## 1일 일정 제안")
    main_city = cities[0] if cities else "추천 지역"
    lines.append(f"- **오전**: {main_city} 대표 명소 방문 및 산책")
    lines.append("- **오후**: 맛집에서 점심 후 지역 관광/체험 활동")
    lines.append("- **저녁**: 지역 야경 감상 및 저녁 식사")
    lines.append("")

    lines.append("## 오류 요약(errors)")
    if errors:
        for e in errors:
            lines.append(
                f"- `{e.get('step', '')}` / `{e.get('type', '')}`: {e.get('message', '')}"
            )
    else:
        lines.append("- 없음")
    lines.append("")

    return "\n".join(lines)
