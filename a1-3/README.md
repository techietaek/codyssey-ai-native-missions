# 🎯 취미핏 (HobbyFit) — AI 취미 추천 서비스

> 뭘 시작할지 모르겠는 사람에게, 성향·여건을 입력하면 **AI가 맞춤 취미 3가지**를 추천 이유·시작 팁과 함께 제안하는 웹 서비스입니다.

**배포 URL:** https://codyssey-a1-3-web-6pya.vercel.app/

---

## 1. 서비스 소개

새 취미를 찾고 싶지만 선택지가 너무 많아 막막한 사람들을 위한 서비스입니다.
성향(내향/외향), 주당 여가시간, 월 예산, 실내/실외 선호, 자유 설명을 입력하면
AI(Gemini)가 조건에 맞는 취미 3가지를 **추천 이유**와 **오늘 바로 시작하는 팁**과 함께 알려줍니다.

- 최소 3개 이상의 섹션(홈 / 서비스 소개 / AI 추천 / FAQ / 문의) 제공
- 모바일·태블릿·데스크톱 반응형
- 다크모드 지원

## 2. 기술 스택

| 구분 | 기술 |
|------|------|
| 프론트엔드 | HTML5, CSS3, **Vanilla JavaScript** (프레임워크 미사용) |
| 백엔드 | **Vercel Serverless Functions (Python)** |
| AI | **Google Gemini API** (`google-genai` SDK) |
| 배포 | GitHub + Vercel |

## 3. 프로젝트 구조

```
a1-3/
├── index.html          # 메인 페이지 (5개 섹션 + 앵커 네비게이션)
├── css/
│   └── style.css       # 반응형 스타일 + 다크모드
├── js/
│   └── main.js         # 폼 처리, fetch 호출, 실패 처리, 다크모드
├── api/
│   └── recommend.py    # Serverless 함수 (Gemini 호출)
├── images/             # 스크린샷 등 정적 이미지
├── docs/
│   └── 기획서.md        # 서비스 기획서
├── requirements.txt    # Python 의존성 (google-genai)
├── vercel.json         # Vercel 함수 설정
├── .env.example        # 환경 변수 예시
├── .gitignore
└── README.md
```

## 4. 로컬 실행 방법

이 프로젝트는 Vercel Python 함수를 사용하므로, 로컬 테스트에는 **Vercel CLI**가 필요합니다.

```bash
# 1) Vercel CLI 설치
npm i -g vercel

# 2) 프로젝트 폴더에서 환경 변수 파일 생성
cp .env.example .env.local
#  .env.local 을 열어 GEMINI_API_KEY 에 실제 키를 입력

# 3) 로컬 개발 서버 실행 (프론트 + Python 함수 함께 구동)
vercel dev
#  → http://localhost:3000 접속
```

> 정적 화면(HTML/CSS/JS)만 확인하려면 `python3 -m http.server` 로도 열 수 있지만,
> `/api/recommend` (AI 기능)은 `vercel dev` 환경에서만 동작합니다.

## 5. 배포 방법 (GitHub + Vercel)

1. **GitHub에 저장소 생성 후 푸시**
   ```bash
   git init
   git add .
   git commit -m "feat: 취미핏 초기 버전"
   git branch -M main
   git remote add origin https://github.com/<username>/hobbyfit.git
   git push -u origin main
   ```
2. **Vercel에서 Import** — [vercel.com/new](https://vercel.com/new) → GitHub 저장소 선택 → Import
3. **환경 변수 등록** (아래 6번 참고)
4. **Deploy** 클릭 → 발급된 URL에서 동작 확인
5. 코드 수정 후 `git push` 하면 **자동 재배포**됩니다.

## 6. 환경 변수 설정 (중요)

API 키는 **절대 코드/README/스크린샷에 노출하지 않고** 환경 변수로만 관리합니다.

| 변수명 | 설명 | 필수 |
|--------|------|:---:|
| `GEMINI_API_KEY` | Gemini API 키 ([aistudio.google.com/apikey](https://aistudio.google.com/apikey) 발급) | ✅ |
| `GEMINI_MODEL` | 사용할 모델명 (미설정 시 `gemini-3.6-flash`) | – |

**Vercel에 등록:**
`Project → Settings → Environment Variables` 에서 `GEMINI_API_KEY` 추가 후 재배포합니다.

**로컬:** `.env.example` 을 `.env.local` 로 복사한 뒤 값을 채웁니다. (`.env.local` 은 `.gitignore` 로 커밋 제외)

> ⚠️ 키가 유출되면 즉시 Google AI Studio에서 폐기/재발급하고, 노출된 커밋 이력을 정리하세요.

## 7. AI 기능 동작 흐름

```
사용자 입력(폼)
   └─ js/main.js: 필수값 검증 → fetch('/api/recommend', POST, JSON)
        └─ api/recommend.py: 입력 검증 → Gemini 호출 → JSON 반환
             └─ js/main.js: 결과 카드 렌더 / 실패 시 안내 메시지
```

**실패 처리 3종 모두 구현:**
- 빈 입력(필수값 누락) → "필수 항목입니다" 안내
- API 오류(4xx/5xx) → "추천을 불러오지 못했어요" 안내
- 지연/타임아웃(25초) → "응답이 지연되고 있어요" 안내

## 8. 제출 패키지

- [x] 배포된 웹 서비스 (Vercel URL)
- [x] GitHub 저장소 (프론트/백엔드 구조 구분)
- [x] README.md
- [x] 서비스 기획서 (`docs/기획서.md`)
- [ ] 증빙 자료 (스크린샷 · AI 코딩 도구 사용 로그) — `images/` 에 추가
