"""
취미핏 (HobbyFit) — AI 추천 백엔드
Vercel Serverless Function (Python)

프론트엔드에서 POST /api/recommend 로 사용자 입력을 받아
Google Gemini API에 전달하고, 취미 추천 3가지를 JSON으로 반환한다.

- API 키는 환경 변수 GEMINI_API_KEY 로만 관리한다. (코드에 직접 노출 금지)
- 실패 상황(입력 오류/키 미설정/AI 오류)을 적절한 HTTP 상태코드로 반환한다.
"""

import json
import os
from http.server import BaseHTTPRequestHandler

from google import genai
from google.genai import errors as genai_errors
from google.genai import types

# 사용할 모델: 빠르고 저렴한 Flash (학습/데모용에 적합)
# 빈 문자열 환경변수가 기본값을 덮어쓰지 않도록 `or` 사용
MODEL = os.environ.get("GEMINI_MODEL") or "gemini-3.6-flash"

SYSTEM_PROMPT = (
    "당신은 사람의 성향과 여건에 맞는 취미를 추천해주는 친절한 취미 큐레이터입니다. "
    "반드시 한국어로, 그리고 아래 JSON 형식만으로 답하세요. 설명 문장이나 마크다운은 넣지 마세요.\n"
    '{"recommendations": ['
    '{"title": "취미 이름", "reason": "이 사람에게 왜 잘 맞는지 1~2문장", '
    '"tip": "오늘 바로 시작할 수 있는 구체적 첫걸음 팁 1문장"}'
    "]}\n"
    "recommendations 배열에는 서로 다른 취미 3개를 담으세요."
)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 1) 요청 본문 파싱
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"
            body = json.loads(raw or b"{}")

            personality = (body.get("personality") or "").strip()
            hours = (body.get("hours") or "").strip()
            budget = (body.get("budget") or "").strip()
            place = (body.get("place") or "").strip()
            note = (body.get("note") or "").strip()[:300]

            # 2) 필수값 검증 (빈 입력 → 400)
            if not (personality and hours and budget and place):
                return self._send(400, {"error": "필수 입력값(성향/여가시간/예산/장소)이 누락되었습니다."})

            # 3) API 키 확인 (미설정 → 500)
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                return self._send(
                    500,
                    {"error": "서버에 API 키가 설정되지 않았습니다. 관리자에게 문의해 주세요."},
                )

            # 4) 사용자 프롬프트 구성
            user_prompt = (
                f"성향: {personality}\n"
                f"주당 여가시간: {hours}\n"
                f"월 예산: {budget}\n"
                f"선호 장소: {place}\n"
                f"추가 설명: {note or '없음'}\n\n"
                "위 조건에 맞는 취미 3가지를 추천해 주세요."
            )

            # 5) Gemini 호출
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model=MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    # gemini-3.6-flash 는 thinking 모델이라 추론 토큰까지 예산에 포함된다.
                    # 넉넉히 잡지 않으면 JSON 본문이 잘려(MAX_TOKENS) 파싱에 실패한다.
                    max_output_tokens=2048,
                    response_mime_type="application/json",
                ),
            )

            text = (response.text or "").strip()

            # 6) 모델 응답(JSON) 파싱 — 혹시 앞뒤에 텍스트가 붙어도 JSON 부분만 추출
            data = self._extract_json(text)
            recs = data.get("recommendations", []) if isinstance(data, dict) else []
            recs = [r for r in recs if isinstance(r, dict) and r.get("title")][:3]

            if not recs:
                return self._send(502, {"error": "AI 응답을 해석하지 못했습니다. 다시 시도해 주세요."})

            return self._send(200, {"recommendations": recs})

        except json.JSONDecodeError:
            return self._send(400, {"error": "요청 형식이 올바르지 않습니다."})
        except genai_errors.APIError:
            # AI API 자체 오류 (쿼터/인증/서버 등)
            return self._send(502, {"error": "AI 서비스 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."})
        except Exception:
            return self._send(500, {"error": "알 수 없는 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."})

    # ---------- 유틸 ----------
    def _send(self, status, obj):
        payload = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    @staticmethod
    def _extract_json(text):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1 and end > start:
                try:
                    return json.loads(text[start : end + 1])
                except json.JSONDecodeError:
                    return {}
            return {}
