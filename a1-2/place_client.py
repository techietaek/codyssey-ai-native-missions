"""지도/장소 검색 API 클라이언트.

Kakao Local(키워드 검색)과 Naver Local Search를 지원한다.
검색 결과가 0건이거나 오류가 나도 예외를 삼키지 않고 상위에서
errors[]로 처리할 수 있도록 표준 예외를 던진다.
"""

from __future__ import annotations

import os
import re
from typing import Any

import requests

from errors import ApiError, AuthError, NetworkError, ParseError

REQUEST_TIMEOUT = 15  # seconds


class PlaceClient:
    """지도/장소 검색 제공자 추상화 (kakao / naver / mock)."""

    def __init__(self, provider: str = "kakao", mock: bool = False):
        self.provider = provider
        self.mock = mock
        if mock:
            return
        if provider == "kakao":
            self.api_key = os.getenv("KAKAO_REST_API_KEY")
        elif provider == "naver":
            self.client_id = os.getenv("NAVER_CLIENT_ID")
            self.client_secret = os.getenv("NAVER_CLIENT_SECRET")
        else:
            raise ValueError(f"지원하지 않는 지도 provider: {provider}")

    def has_key(self) -> bool:
        if self.mock:
            return True
        if self.provider == "kakao":
            return bool(self.api_key)
        return bool(self.client_id and self.client_secret)

    def search_restaurants(self, city: str, size: int = 5) -> list[dict]:
        """도시 기준 맛집을 최대 size개 검색. 표준화된 dict 리스트 반환.

        결과 0건이면 빈 리스트를 반환한다(예외 아님).
        인증/네트워크/파싱 오류는 표준 예외로 던진다.
        """
        if self.mock:
            return _mock_places(city, size)
        query = f"{city} 맛집"
        if self.provider == "kakao":
            return self._kakao(query, size)
        return self._naver(query, size)

    # -- Kakao -------------------------------------------------------------
    def _kakao(self, query: str, size: int) -> list[dict]:
        url = "https://dapi.kakao.com/v2/local/search/keyword.json"
        headers = {"Authorization": f"KakaoAK {self.api_key}"}
        params = {"query": query, "size": min(size, 15)}
        data = _get_json(url, headers, params, step="place_search")
        docs = data.get("documents", [])
        items = []
        for d in docs[:size]:
            items.append(
                {
                    "name": d.get("place_name", ""),
                    "address": d.get("road_address_name") or d.get("address_name", ""),
                    "category": d.get("category_name", ""),
                    "url": d.get("place_url", ""),
                    "x": _to_float(d.get("x")),  # 경도(lng)
                    "y": _to_float(d.get("y")),  # 위도(lat)
                }
            )
        return items

    # -- Naver -------------------------------------------------------------
    def _naver(self, query: str, size: int) -> list[dict]:
        url = "https://openapi.naver.com/v1/search/local.json"
        headers = {
            "X-Naver-Client-Id": self.client_id or "",
            "X-Naver-Client-Secret": self.client_secret or "",
        }
        params = {"query": query, "display": min(size, 5)}
        data = _get_json(url, headers, params, step="place_search")
        items = []
        for d in data.get("items", [])[:size]:
            # Naver 좌표(mapx/mapy)는 KATECH/정수형 -> 참고용으로 그대로 보관
            items.append(
                {
                    "name": _strip_tags(d.get("title", "")),
                    "address": d.get("roadAddress") or d.get("address", ""),
                    "category": d.get("category", ""),
                    "url": d.get("link", ""),
                    "x": _to_float(d.get("mapx")),
                    "y": _to_float(d.get("mapy")),
                }
            )
        return items


# ---------------------------------------------------------------------------
# 헬퍼
# ---------------------------------------------------------------------------
def _get_json(url: str, headers: dict, params: dict, step: str) -> dict[str, Any]:
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.RequestException as exc:
        raise NetworkError(step, f"네트워크 오류: {exc}") from exc

    if resp.status_code in (401, 403):
        raise AuthError(step, f"HTTP {resp.status_code}")
    if resp.status_code == 429:
        raise ApiError(step, "QUOTA_ERROR", "요청 한도 초과(HTTP 429)")
    if resp.status_code >= 400:
        raise ApiError(step, "HTTP_ERROR", f"HTTP {resp.status_code}: {resp.text[:200]}")
    try:
        return resp.json()
    except ValueError as exc:
        raise ParseError(step, f"응답 JSON 파싱 실패: {exc}") from exc


def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _strip_tags(text: str) -> str:
    """Naver title에 포함된 <b> 등 HTML 태그 제거."""
    return re.sub(r"<[^>]+>", "", text or "")


def _mock_places(city: str, size: int) -> list[dict]:
    base = [
        {
            "name": f"{city} 맛집 {i}",
            "address": f"{city}특별시 어딘가로 {i}길 {i * 10}",
            "category": "음식점 > 한식",
            "url": f"https://place.example.com/{city}/{i}",
            "x": 126.5 + i * 0.01,
            "y": 33.5 + i * 0.01,
        }
        for i in range(1, size + 1)
    ]
    return base
