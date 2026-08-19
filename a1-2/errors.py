"""외부 API 호출에서 발생하는 대표 오류를 표준화한 예외 클래스.

- AuthError    : 인증/권한 실패 (HTTP 401/403)  -> AUTH_ERROR
- NetworkError : 네트워크/타임아웃                -> NETWORK_ERROR
- ParseError   : 응답/JSON 파싱 실패             -> PARSE_ERROR
- ApiError     : 그 외(쿼터/HTTP 오류 등) 범용   -> 지정 type

각 예외는 리포트/원본 JSON의 errors[] 항목으로 직렬화할 수 있도록
step / type / message 를 보관한다.
"""

from __future__ import annotations


class ApiError(Exception):
    """API 관련 오류의 기본 클래스."""

    def __init__(self, step: str, err_type: str, message: str):
        self.step = step
        self.type = err_type
        self.message = message
        super().__init__(f"[{step}] {err_type}: {message}")

    def to_dict(self) -> dict:
        return {"step": self.step, "type": self.type, "message": self.message}


class AuthError(ApiError):
    def __init__(self, step: str, message: str):
        super().__init__(step, "AUTH_ERROR", message)


class NetworkError(ApiError):
    def __init__(self, step: str, message: str):
        super().__init__(step, "NETWORK_ERROR", message)


class ParseError(ApiError):
    def __init__(self, step: str, message: str):
        super().__init__(step, "PARSE_ERROR", message)
