"""LLM API 클라이언트.

1차 추천(JSON 구조화)과 최종 리포트(Markdown) 생성을 담당한다.
OpenAI 계열과 Google Gemini 계열을 모두 지원하며, `--mock` 모드에서는
실제 API를 호출하지 않고 샘플 응답을 반환한다.
"""

from __future__ import annotations

import json
import os
import time
from typing import Any

import requests

from errors import ApiError, AuthError, NetworkError, ParseError

REQUEST_TIMEOUT = 60  # seconds (리포트 등 긴 출력 대비)
MAX_RETRIES = 2  # 네트워크 타임아웃/5xx 시 추가 재시도 횟수
RETRY_BACKOFF = 2  # seconds (재시도 간 대기; 시도마다 배수 증가)


# ---------------------------------------------------------------------------
# 프롬프트
# ---------------------------------------------------------------------------
def _recommend_prompt(date: str, count: int) -> str:
    """1차 추천용 프롬프트. 반드시 JSON만 출력하도록 지시한다."""
    if count > 1:
        schema = (
            '{\n'
            '  "recommended_cities": ["도시1", "도시2"],   // string 배열, %d개\n'
            '  "weather": "해당 시기 일반적 날씨 요약 (string)",\n'
            '  "events": ["행사/축제 후보", ...],           // string 배열 1~3개\n'
            '  "reason": "추천 근거 2~4문장 (string)"\n'
            '}'
        ) % count
    else:
        schema = (
            '{\n'
            '  "recommended_city": "제주",                 // string\n'
            '  "weather": "해당 시기 일반적 날씨 요약 (string)",\n'
            '  "events": ["행사/축제 후보", ...],           // string 배열 1~3개\n'
            '  "reason": "추천 근거 2~4문장 (string)"\n'
            '}'
        )
    return (
        f"당신은 국내(대한민국) 여행 추천 도우미입니다.\n"
        f"여행 날짜는 {date} 입니다. 이 시기에 국내에서 여행하기 좋은 지역을 추천하세요.\n"
        f"실제 날씨/행사 데이터의 정확도가 아니라, 아래 스키마에 맞는 '구조화된 출력'이 중요합니다.\n\n"
        f"반드시 아래 JSON 스키마만 출력하세요. 코드블록(```)이나 설명 문장 없이 순수 JSON만 반환합니다.\n\n"
        f"{schema}\n"
    )


def _retry_recommend_prompt(date: str, count: int) -> str:
    """파싱 실패 시 재시도용 프롬프트(필수 키만 강조)."""
    if count > 1:
        keys = '"recommended_cities"(string 배열), "weather", "events"(string 배열), "reason"'
    else:
        keys = '"recommended_city", "weather", "events"(string 배열), "reason"'
    return (
        f"여행 날짜 {date} 에 대한 국내 여행 추천입니다.\n"
        f"다른 텍스트 없이 다음 필수 키만 포함한 순수 JSON 한 개만 출력하세요: {keys}."
    )


def _report_prompt(date: str, recommendation: dict, places_by_city: dict, errors: list) -> str:
    """최종 리포트(Markdown) 생성용 프롬프트."""
    context = {
        "date": date,
        "recommendation": recommendation,
        "places_by_city": places_by_city,
        "errors": errors,
    }
    return (
        "아래 JSON 데이터를 바탕으로 국내 여행 추천 리포트를 한국어 Markdown으로 작성하세요.\n"
        "다음 섹션(제목)을 반드시 포함하세요:\n"
        "1. `# {date} 국내 여행 추천 리포트` (제목)\n"
        "2. `## 추천 지역`\n"
        "3. `## 추천 이유`\n"
        "4. `## 날씨 요약`\n"
        "5. `## 행사/축제`\n"
        "6. `## 맛집 추천` (지역별로 정리. 맛집이 0건인 지역은 '데이터 없음 (장소 검색 결과 0건)'으로 표기)\n"
        "7. `## 1일 일정 제안` (오전/오후/저녁 수준)\n"
        "8. `## 오류 요약(errors)` (errors가 비어 있으면 '없음'으로 표기)\n\n"
        "맛집은 이름, 주소, 카테고리, URL이 있으면 함께 적으세요. "
        "코드블록으로 전체를 감싸지 말고 Markdown 본문만 출력하세요.\n\n"
        f"[데이터]\n{json.dumps(context, ensure_ascii=False, indent=2)}\n"
    )


# ---------------------------------------------------------------------------
# LLM 클라이언트
# ---------------------------------------------------------------------------
class LLMClient:
    """LLM 제공자 추상화 (openai / gemini / mock)."""

    def __init__(self, provider: str = "openai", mock: bool = False):
        self.provider = provider
        self.mock = mock
        self.api_key = None
        if mock:
            return
        if provider == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
            self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        elif provider == "gemini":
            self.api_key = os.getenv("GEMINI_API_KEY")
            self.model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
        else:
            raise ValueError(f"지원하지 않는 LLM provider: {provider}")

    # -- 공개 메서드 -------------------------------------------------------
    def recommend(self, date: str, count: int = 1) -> dict:
        """1차 추천을 받아 JSON(dict)으로 파싱한다. 파싱 실패 시 1회 재시도."""
        if self.mock:
            return _mock_recommendation(count)

        prompt = _recommend_prompt(date, count)
        raw = self._complete(prompt, want_json=True)
        try:
            return _extract_json(raw)
        except ParseError:
            # 재시도 1회: 필수 키만 다시 JSON으로 요청
            retry = self._complete(_retry_recommend_prompt(date, count), want_json=True)
            return _extract_json(retry)  # 실패하면 ParseError 그대로 전파

    def make_report(self, date: str, recommendation: dict, places_by_city: dict, errors: list) -> str:
        """최종 리포트를 Markdown 문자열로 생성한다."""
        if self.mock:
            from report import build_markdown_fallback
            return build_markdown_fallback(date, recommendation, places_by_city, errors)

        prompt = _report_prompt(date, recommendation, places_by_city, errors)
        return self._complete(prompt, want_json=False).strip()

    # -- 내부 호출 ---------------------------------------------------------
    def _complete(self, prompt: str, want_json: bool) -> str:
        if not self.api_key:
            raise AuthError("llm", "LLM API 키가 설정되지 않았습니다.")
        if self.provider == "openai":
            return self._openai(prompt, want_json)
        return self._gemini(prompt, want_json)

    def _openai(self, prompt: str, want_json: bool) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        body: dict[str, Any] = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        if want_json:
            body["response_format"] = {"type": "json_object"}
        data = _post_json(url, headers, body, step="llm")
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ParseError("llm", f"예상치 못한 응답 구조: {exc}") from exc

    def _gemini(self, prompt: str, want_json: bool) -> str:
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent?key={self.api_key}"
        )
        headers = {"Content-Type": "application/json"}
        body: dict[str, Any] = {"contents": [{"parts": [{"text": prompt}]}]}
        if want_json:
            body["generationConfig"] = {"responseMimeType": "application/json"}
        data = _post_json(url, headers, body, step="llm")
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ParseError("llm", f"예상치 못한 응답 구조: {exc}") from exc


# ---------------------------------------------------------------------------
# 헬퍼
# ---------------------------------------------------------------------------
def _post_json(url: str, headers: dict, body: dict, step: str) -> dict:
    """POST 요청 후 JSON 파싱. HTTP/네트워크 오류를 표준 예외로 변환.

    네트워크 타임아웃/연결 오류와 5xx(서버 일시 오류)는 지수 백오프로
    최대 MAX_RETRIES회 재시도한다. 인증(401/403)·쿼터(429)·기타 4xx는
    재시도해도 결과가 같으므로 즉시 예외로 전파한다.
    """
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.post(url, headers=headers, json=body, timeout=REQUEST_TIMEOUT)
        except requests.exceptions.RequestException as exc:
            last_exc = NetworkError(step, f"네트워크 오류: {exc}")
        else:
            if resp.status_code in (401, 403):
                raise AuthError(step, f"인증 실패(HTTP {resp.status_code})")
            if resp.status_code == 429:
                raise ApiError(step, "QUOTA_ERROR", "요청 한도 초과(HTTP 429)")
            if resp.status_code >= 500:
                # 서버 일시 오류 → 재시도 대상
                last_exc = ApiError(step, "HTTP_ERROR", f"HTTP {resp.status_code}: {resp.text[:200]}")
            elif resp.status_code >= 400:
                raise ApiError(step, "HTTP_ERROR", f"HTTP {resp.status_code}: {resp.text[:200]}")
            else:
                try:
                    return resp.json()
                except ValueError as exc:
                    raise ParseError(step, f"응답 JSON 파싱 실패: {exc}") from exc

        # 여기 도달 = 재시도 대상 오류. 남은 시도가 있으면 백오프 후 재시도.
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_BACKOFF * (attempt + 1))

    raise last_exc  # type: ignore[misc]  # 모든 재시도 소진


def _extract_json(text: str) -> dict:
    """LLM 출력 텍스트에서 JSON 객체를 추출/파싱한다."""
    if text is None:
        raise ParseError("llm", "빈 응답")
    s = text.strip()
    # 코드블록 마커 제거
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
        s = s.strip()
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        # 본문 중 첫 '{' ~ 마지막 '}' 구간만 재시도
        start, end = s.find("{"), s.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(s[start : end + 1])
            except json.JSONDecodeError as exc:
                raise ParseError("llm", f"JSON 파싱 실패: {exc}") from exc
        raise ParseError("llm", "응답에서 JSON을 찾지 못함")


def _mock_recommendation(count: int) -> dict:
    if count > 1:
        return {
            "recommended_cities": ["제주", "강릉"][:count],
            "weather": "해당 시기 평균 15°C 내외, 비교적 온화하며 바람이 다소 있음",
            "events": ["봄 시즌 지역 축제", "유채꽃 관련 지역 행사"],
            "reason": "봄철 야외 활동에 무리가 적고, 성수기 대비 항공/숙박 부담이 적습니다. "
            "해안 경관과 지역 축제를 함께 즐기기 좋은 시기입니다.",
        }
    return {
        "recommended_city": "제주",
        "weather": "3월 중순 평균 15°C 내외, 바람이 있으나 비교적 온화함",
        "events": ["유채꽃 관련 지역 행사", "봄 시즌 지역 축제(일정 변동 가능)"],
        "reason": "3월 중순은 제주가 봄꽃을 즐기기 좋은 시기입니다. "
        "항공/숙박도 성수기 대비 부담이 적고, 야외 활동에 무리가 적습니다.",
    }
