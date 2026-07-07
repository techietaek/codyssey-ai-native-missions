# Claro — 광고 스토리보드

> 브랜드: Claro | 광고 길이: 약 20초 (과제 요건 '60초 이내' 충족)
> 톤앤매너: 클린, 모던, 세련됨, 프리미엄

---

## 기능 요구사항 충족 체크리스트

| 요구사항 | 항목 | 충족 여부 |
|---|---|---|
| 1. 기획 정의 | 브랜드 아이덴티티 (타겟/톤/USP) | ✅ Section 01 |
| 1. 기획 정의 | 광고 목적 + 핵심 메시지 1문장 | ✅ Section 01 |
| 2. 스토리보드 | 씬별 필수 필드 누락 없이 작성 | ✅ Section 03 |
| 2. 스토리보드 | 프롬프트 수정 전/후 + 이유 기록 | ✅ Section 04 (Leonardo 씬별 + Runway 씬별 전 이터레이션 기록) |
| 3. 멀티모달 | 이미지 생성 AI 1종 이상 | ✅ Leonardo AI |
| 3. 멀티모달 | 비디오 생성/변환 AI 1종 이상 | ✅ Runway ML |
| 3. 멀티모달 | 오디오 생성 AI 1종 이상 | ✅ ElevenLabs + Suno |
| 3. 멀티모달 | 각 도구 선택 이유 기재 | ✅ 씬별 "사용 도구 & 목적" 필드 |
| 4. 영상 스펙 | 60초 이내 | ✅ 약 20초 |
| 4. 영상 스펙 | AI 생성 시각 요소 포함 | ✅ 전 씬 Leonardo + Runway |
| 4. 영상 스펙 | AI 생성 청각 요소 포함 | ✅ ElevenLabs 내레이션 + Suno BGM |
| 5. 서사/메시지 | 기승전결 구조 | ✅ 혼돈→앱등장→집중→브랜드 |
| 5. 서사/메시지 | 마지막 3~5초 브랜드 인지 장치 | ✅ Scene 4 (마지막 5초): 브랜드명 + 슬로건 + CTA — 요건 상한(5초) 정확히 충족 |

---

## 01. 브랜드 아이덴티티

| 항목 | 내용 |
|---|---|
| **브랜드명** | Claro |
| **카테고리** | AI 집중력 & 태스크 관리 앱 (테크 서비스) |
| **타겟** | 25–35세 직장인 · 프리랜서 · 스타트업 종사자 |
| **톤앤매너** | 클린, 모던, 프리미엄 — 군더더기 없는 미니멀리즘 |
| **USP (차별점)** | AI가 하루의 혼돈을 자동으로 정리해 집중해야 할 것만 남겨준다 |
| **광고 목적** | 브랜드 인지 (Awareness) — 앱 존재 각인 + 다운로드 유도 |
| **핵심 메시지 (1문장)** | Claro — 오늘의 혼돈을, 하나의 흐름으로. |
| **슬로건** | Think Clear. |

---

## 02. 캠페인 개요

**기승전결 구조** (총 약 20초)

```text
🔴 기 — 디지털 혼돈 (5s)
🔵 승 — 앱 등장 / 전환 (5s)
🟢 전 — 집중하는 순간 (5s)
⚪ 결 — 브랜드 각인 (5s) ← 마지막 5초, 브랜드 노출
```

> 📌 Runway 최소 생성 단위(5초) 기준으로 씬별 길이를 설계. 내레이션이 씬 시작에 맞아 들어가면서 여백이 생겨 모던하고 프리미엄한 느낌이 연출됨. 과제 스펙(60초 이내) 충족 ✅

물리적 오브젝트 없이 디지털 UI 요소, 스튜디오 제품 사진, 흰 여백만으로 구성.
복잡한 알림들이 쏟아지다 → Claro가 등장해 정리하고 → 사용자가 집중된 상태로 → 브랜드 텍스트만 남는 세련된 엔딩.

---

## 03. 씬별 스토리보드

---

### 🔴 Scene 1 — 기: 디지털 혼돈

| 필드 | 내용 |
|---|---|
| **씬 번호** | 1 |
| **씬 길이** | 5초 |
| **목표 메시지** | 쏟아지는 디지털 알림의 혼돈감을 세련되게 시각화해 타겟의 공감을 즉각 유도한다 |
| **화면 구성** | 구도: 카메라에 가까이 공중에 흩뿌려진(mid-air) 대형 카드, 다양한 각도로 떠다니고 낙하 / 피사체: 반투명 frosted glass 알림 카드 / 배경: 순백 / 텍스트: 카드 안에 판독 불가한 미세 텍스트·아이콘 형태 |
| **내레이션 / 카피** | "하루에도 수백 번, 생각이 흩어집니다." |
| **사용 도구 & 목적** | **이미지: Leonardo AI** — 디지털 UI 스타일 혼돈 이미지 생성. Flux Schnell 모델로 토큰 절약하면서 충분한 품질 확보<br><br>**영상: Runway ML** — 카드들이 사방에서 날아들어 화면 전체에 쌓이는 역동적인 모션으로 혼돈감 극대화<br><br>**오디오: ElevenLabs** — 공감을 유도하는 차분한 한국어 내레이션 생성 |

#### 🎨 이미지 프롬프트 (Leonardo AI)

```text
many frosted glass notification cards scattered mid-air close to the camera,
large cards filling the entire frame, floating and falling at various angles,
each card contains tiny illegible text lines and small icon shapes,
pure white background, dynamic scattered arrangement, cards mid-fall,
digital UI aesthetic, cool blue and light gray tones, subtle drop shadows
```

> Model: **Flux Schnell** | Dimensions: **1376 × 768**

#### 🎬 영상 프롬프트 (Runway ML)

```text
Notification cards continuously fly in from all edges of the frame
and pile up across the entire screen, cards tumbling and overlapping each other,
filling from the edges toward the center, chaotic and urgent accumulation,
fast-paced motion, dense layering effect.
```

> Image to Video → Gen-4 Turbo → Duration: **5s**

#### 🔊 내레이션 스크립트 (ElevenLabs)

```text
하루에도 수백 번, 생각이 흩어집니다.
```

> **Voice:** ElevenLabs — 'Tim' (warm·calm·husky 톤) 선정. 음성은 별도 텍스트 프롬프트 없이 목소리 선택 + 설정값으로 TTS 처리 (언어를 한국어로 설정해 발음 자연스럽게 확보)
> Speed 0.9 / Stability 60% / Similarity 75% / 언어: 한국어 / 출력: mp3 44.1kHz (128kbps) — Scene 4까지 동일 설정 유지

#### 🎵 BGM (Suno) — 전체 공통 1곡, 여기서만 생성

```text
bright minimalist ambient, airy synth pads, light and clean,
uplifting but subtle, no vocals, slow tempo, modern tech advertisement,
soft high notes, spacious and breathable
```

> 💡 **저작권 참고:** Suno 무료 플랜은 commercial rights 미포함. 학술 과제 목적 사용으로 Download Anyway 진행 (상업적 배포 아님)

| **입력 프롬프트 원문** | 위 이미지/영상/오디오 프롬프트 |
|---|---|
| **출력 결과 요약** | 공중에 흩뿌려진 대형 알림 카드 키비주얼(이미지) + 사방에서 날아와 쌓이는 역동적 혼돈 모션(영상) 확보 |
| **결과 파일명** | `scene-1.jpg` / `scene-1.mp4` / `scene-1-narration.mp3` / `bgm.mp3` |

---

### 🔵 Scene 2 — 승: 앱 등장

| 필드 | 내용 |
|---|---|
| **씬 번호** | 2 |
| **씬 길이** | 5초 |
| **목표 메시지** | Claro 앱이 혼돈을 정리해주는 핵심 가치를 프리미엄 제품 목업으로 전달한다 |
| **화면 구성** | 구도: 정면 센터 / 피사체: 부유하는 스마트폰 제품 목업 + 미니멀 태스크 리스트 UI / 배경: 순백 / 텍스트: 화면 상단 "Claro" 타이틀 + 태스크 3개("Team standup 3PM", "Review proposal", "Send report"), 각 항목 좌측 파란 원형 인디케이터 |
| **내레이션 / 카피** | "Claro가 열리는 순간," |
| **사용 도구 & 목적** | **이미지: Leonardo AI** — 프리미엄 제품 목업 스타일의 앱 UI 키비주얼 생성. 앞 씬과 같은 흰 배경 톤 유지<br><br>**영상: Runway ML** — 스마트폰이 아래에서 천천히 떠올라 5초 내내 부드럽게 부유하는 프리미엄 제품 등장 연출<br><br>**오디오: ElevenLabs** — 기대감을 조성하는 짧고 명료한 내레이션 |

#### 🎨 이미지 프롬프트 (Leonardo AI)

```text
smartphone app screen mockup floating on pure white background,
app screen shows title "Claro" at the top,
clean task list with exactly 3 items: "Team standup 3PM", "Review proposal", "Send report",
small blue filled circle on the left of each item, soft drop shadow under phone,
centered composition, generic phone with no brand logos or markings
```

> Model: **Flux Schnell** | Dimensions: **1376 × 768**

#### 🎬 영상 프롬프트 (Runway ML)

```text
Smartphone slowly and gracefully rises from below into the center of the frame,
then gently floats in place with a slow continuous subtle up and down drift,
soft even lighting throughout with no flashes or highlights,
screen always facing camera, smooth and unhurried motion filling the entire duration,
premium elegant product feel.
```

> Image to Video → Gen-4 Turbo → Duration: **5s**

#### 🔊 내레이션 스크립트 (ElevenLabs)

```text
Claro가 열리는 순간,
```

| **입력 프롬프트 원문** | 위 이미지/영상/오디오 프롬프트 |
|---|---|
| **출력 결과 요약** | 프리미엄 제품 목업 느낌의 앱 UI 키비주얼 + 스마트폰 부유 영상 확보 |
| **결과 파일명** | `scene-2.jpg` / `scene-2.mp4` / `scene-2-narration.mp3` |

---

### 🟢 Scene 3 — 전: 집중하는 순간

| 필드 | 내용 |
|---|---|
| **씬 번호** | 3 |
| **씬 길이** | 5초 |
| **목표 메시지** | 스튜디오 제품 사진 스타일로 앱을 사용하며 집중된 사용자의 순간을 감각적으로 담는다 |
| **화면 구성** | 구도: 클로즈업 / 피사체: 스마트폰을 든 한 손(one hand) / 배경: 순백 스튜디오 / 텍스트: 화면에 "Claro" 타이틀 + 짧은 태스크 항목 3개 표시 |
| **내레이션 / 카피** | "오늘 할 일이 선명해집니다." |
| **사용 도구 & 목적** | **이미지: Leonardo AI** — 스튜디오 제품 사진 스타일의 손 클로즈업 생성. 실사 느낌에 강한 Flux Schnell 활용<br><br>**영상: Runway ML** — 손이 아래에서 올라오며 화면을 천천히 스크롤하는 자연스러운 앱 사용 장면 연출<br><br>**오디오: ElevenLabs** — 해결감을 주는 따뜻한 내레이션으로 씬 마무리 |

#### 🎨 이미지 프롬프트 (Leonardo AI)

```text
close-up of one hand holding a smartphone, pure white background,
phone screen showing a minimalist task list app with title "Claro" at top
and 3 short task items in clean sans-serif text, soft studio lighting,
shallow depth of field, premium product photography, warm skin tones, centered
```

> Model: **Flux Schnell** | Dimensions: **1376 × 768**
> ⚠️ 손 모양이 이상하면 프롬프트 앞에 `realistic hands,` 추가 후 재생성

#### 🎬 영상 프롬프트 (Runway ML)

```text
Hand holding smartphone slowly raises up into frame from below,
fingers gently scroll down on the screen with slow smooth motion,
soft studio lighting, camera stays completely still,
natural and calm hand movement throughout.
```

> Image to Video → Gen-4 Turbo → Duration: **5s**

#### 🔊 내레이션 스크립트 (ElevenLabs)

```text
오늘 할 일이 선명해집니다.
```

| **입력 프롬프트 원문** | 위 이미지/영상/오디오 프롬프트 |
|---|---|
| **출력 결과 요약** | 스튜디오 제품 사진 스타일 손 클로즈업 + 스크롤 모션 영상 확보 |
| **결과 파일명** | `scene-3.jpg` / `scene-3.mp4` / `scene-3-narration.mp3` |

---

### ⚪ Scene 4 — 결: 브랜드 각인 ← 마지막 5초 브랜드 노출 구간

| 필드 | 내용 |
|---|---|
| **씬 번호** | 4 |
| **씬 길이** | **5초** (마지막 5초 브랜드 노출 요건 충족) |
| **목표 메시지** | 텍스트만 남는 미니멀 엔딩으로 브랜드명·슬로건·CTA를 각인시킨다 |
| **화면 구성** | 구도: 센터 정렬 / 피사체: 브랜드 워드마크 + 파란 원형 마크 + 슬로건 + CTA / 배경: 순백 / 텍스트: "Claro" (브랜드명) + "Think Clear." (슬로건) + "Download for free" (CTA) |
| **내레이션 / 카피** | "Claro. 지금 다운로드하세요!" |
| **사용 도구 & 목적** | **이미지: Leonardo AI** — 미니멀 브랜드 엔딩 화면 생성<br><br>**영상: Runway ML** — 수면 파동 효과로 텍스트가 잔잔하게 일렁이다 정지하는 클로징 연출<br><br>**오디오: ElevenLabs** — 'Tim' 목소리(warm·calm·husky)를 한국어 언어 설정으로 TTS 처리. 브랜드명 + CTA 클로징 내레이션 |

#### 🎨 이미지 프롬프트 (Leonardo AI)

```text
pure white background, centered bold text "Claro" in dark charcoal,
small blue filled circle above the text,
tagline "Think Clear." in light gray below,
small text "Download for free" at the bottom,
ultra minimal, premium tech brand design
```

> Model: **Flux Schnell** | Dimensions: **1376 × 768**
> ⚠️ "Claro" 텍스트가 오타·변형되면 재생성 (토큰 소모 적음)

#### 🎬 영상 프롬프트 (Runway ML)

```text
The text "Claro" and tagline subtly ripple and wave
as if seen through a water surface disturbed by an invisible droplet,
gentle undulating distortion spreads outward from the center of the text
then slowly calms to perfectly still,
no water visible, no droplet, only the ripple effect on the text itself,
calm and elegant.
```

> Image to Video → Gen-4 Turbo → Duration: **5s**

#### 🔊 내레이션 스크립트 (ElevenLabs)

```text
Claro. 지금 다운로드하세요!
```

> **목소리 설정:** ElevenLabs 'Tim' 목소리(warm·calm·husky)에 언어를 한국어로 설정해 TTS 처리.
> 음성 생성용 텍스트 프롬프트는 없으며, 목소리 선택 + 설정값(Speed 0.9 / Stability 60% / Similarity 75% / 언어 한국어 / 출력 mp3 44.1kHz 128kbps)으로 전 씬 동일 유지.

| **입력 프롬프트 원문** | 위 이미지/오디오 프롬프트 |
|---|---|
| **출력 결과 요약** | 미니멀 브랜드 엔딩 화면 확보 + 클로징 내레이션 + BGM 페이드아웃 |
| **결과 파일명** | `scene-4.jpg` / `scene-4.mp4` / `scene-4-narration.mp3` |

---

## 04. 프롬프트 수정 전/후 기록 (전 씬 실제 이터레이션)

> 📌 과제 필수 항목 + 실제 제작 과정에서 발생한 모든 프롬프트 수정 기록

---

### Scene 1 — 총 5회 수정

#### V1 → V2: 배치 방식 수정

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `flat lay, white background, many semi-transparent notification bubbles and sticky notes overlapping randomly, muted pastel colors, no text, top-down view, clean minimal style` |
| **V1 결과** | 스티커 메모들이 화면 가장자리에 예쁘게 정렬된 액자 형태. 중앙이 텅 비어 혼돈감 전혀 없음 |
| **수정 이유** | `overlapping randomly`가 의도대로 작동하지 않음. "무작위 겹침"보다 "중앙 밀집"을 직접 지시해야 함을 인식 |
| **V2 프롬프트** | `many colorful sticky notes and notification cards piled on top of each other in the center, chaotic and messy, overlapping randomly, white background, pastel colors, top-down flat lay, dense and crowded` |
| **V2 결과** | 혼돈감 생김. 그러나 물리적 종이 메모 질감 → 테크 브랜드와 어울리지 않는 유치한 인상 |

#### V2 → V3: 전체 방향 전환 (물리 → 디지털)

| 구분 | 내용 |
|---|---|
| **수정 이유** | 종이 스티커 메모는 아날로그 오브젝트. AI/테크 앱 Claro의 광고에서 "정보 과부하"를 표현할 땐 디지털 UI 요소가 더 적합하다고 판단. 전체 톤앤매너를 클린·모던·디지털로 재정의 |
| **V3 프롬프트** | `dozens of overlapping notification cards with colorful app icons and red badge dots, filling the entire frame, chaotic dense arrangement, frosted glass panels, white background, vivid pastel colors pink blue green, top-down view, high contrast` |
| **V3 결과** | Twitter 새 로고, Apple 로고, Instagram 아이콘 등 실제 브랜드 로고 대거 등장 → 저작권 문제 발생. 핑크 색상 과다로 브랜드 톤과 불일치 |

#### V3 → V4: 저작권 문제 해결

| 구분 | 내용 |
|---|---|
| **수정 이유** | `app icons` 키워드가 AI에게 실제 앱 아이콘(상표 등록된 로고)을 생성하도록 유도함. 명시적으로 `no logos, no brand icons` 추가 및 추상 요소로 교체 필요 |
| **V4 프롬프트** | `many overlapping semi-transparent rectangular panels and notification windows, pure white background, no logos, no brand icons, no text, abstract shapes only, subtle drop shadows, cool blue and light gray tones, chaotic dense arrangement, top-down flat lay, minimalist tech style` |
| **V4 결과** | 저작권 문제 해결, 클린한 파란 패널 생성. 단, `no text` 조건으로 인해 텍스트가 없어 빈 박스처럼 보임 → "알림 카드"로 인식되지 않음 |

#### V4 → V5: 텍스트 힌트 추가

| 구분 | 내용 |
|---|---|
| **수정 이유** | 텍스트가 없으면 알림 카드가 아닌 단순 사각형으로 인식됨. "읽기 어렵지만 내용이 있다는 힌트"를 주기 위해 illegible text 추가 |
| **V5 프롬프트** | `many overlapping frosted glass notification cards with tiny illegible text lines inside each card, pure white background, no logos, cool blue and light gray tones, dense chaotic scattered arrangement, subtle drop shadows, minimalist tech style, text content too small to read clearly` |
| **V5 결과** | 카드 안에 작은 텍스트가 생겨 "메시지·알림 카드" 맥락이 명확해짐. 저작권 이슈 없음. 브랜드 톤(클린·디지털) 유지 |

> ⚠️ **이후 영상 변환 단계에서 최종 교체:** V5 이미지(밀집 흩뿌림 구도)는 Runway에서 카드가 움직이지 않고 카메라만 움직이는 문제가 있어, 카드를 카메라 가까이 공중에 흩뿌린 mid-air 구도(`close to the camera, large cards filling the entire frame` 추가)로 재생성해 최종 확정. **최종 이미지 프롬프트는 Section 03 참조** (아래 Runway 영상 프롬프트 수정 로그 참고)

---

### Scene 2 — 총 2회 수정

#### V1 → V2: 브랜드명 삽입 + 제품 목업 전환

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `minimalist mobile app task list UI, white background, 3 simple list items with small blue dot on the left of each, clean sans-serif font, no clutter, centered, soft drop shadow` |
| **V1 결과** | 앱 UI가 폰 없이 평면적으로 생성. 텍스트가 모두 gibberish(AI 할루시네이션). "Claro" 브랜드 전혀 없음 |
| **수정 이유** | ① 앱이 폰 안에 있어야 "제품 등장" 느낌이 남 → 폰 목업 추가 ② 브랜드명이 없으면 광고 맥락이 연결되지 않음 → "Claro" 및 실제 태스크 내용 명시 |
| **V2(최종) 프롬프트** | `smartphone app screen mockup floating on pure white background, app screen shows title "Claro" at the top, clean task list with exactly 3 items: "Team standup 3PM", "Review proposal", "Send report", small blue filled circle on the left of each item, soft drop shadow under phone, centered composition, generic phone with no brand logos or markings` |
| **V2 결과** | "Claro" 타이틀이 굵게 표시됨. 태스크 항목 일부 오타 있으나 형식(체크리스트) 명확히 전달. 제품 목업 느낌으로 Scene 2 목적 달성 ✅ |

---

### Scene 3 — 총 1회 수정

#### V1 → V2: 블랙 스크린 → 앱 콘텐츠 삽입

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `close-up of hands holding a slim smartphone, pure white background, soft studio lighting from above, shallow depth of field, premium product photography, no text on screen, clean and minimal, warm skin tones, centered` |
| **V1 결과** | 손 자세는 자연스럽고 프리미엄한 느낌이었으나, 화면이 검정(꺼진 상태)으로 생성됨. "앱을 사용하는 집중 순간" 맥락이 전혀 전달되지 않음 |
| **수정 이유** | `no text on screen` 조건이 AI에게 아예 화면을 끄도록 지시한 것으로 해석됨. "Claro 앱이 켜진 상태"를 표현하려면 화면 내용을 명시해야 함 |
| **V2(최종) 프롬프트** | `close-up of one hand holding a smartphone, pure white background, phone screen showing a minimalist task list app with title "Claro" at top and 3 short task items in clean sans-serif text, soft studio lighting, shallow depth of field, premium product photography, warm skin tones, centered` |
| **V2 결과** | "Claro" 앱 타이틀이 화면에 표시되고 태스크 리스트가 보임. "앱을 사용 중인 집중 상태" 맥락 명확히 전달 ✅ |

---

### Scene 1 — Runway ML 영상 프롬프트 수정

#### V1 → V2: 정적 줌인 → 카드 쌓임 동적 효과

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `Camera slowly and smoothly zooms in toward the center. Gentle forward motion, no shake.` |
| **V1 결과** | 정적 이미지를 단순 확대하는 카메라 줌인만 발생. 카드 자체 움직임 없음 |
| **수정 이유** | 이미 카드가 쌓인 이미지를 첫 프레임으로 주면 Runway가 오브젝트를 움직이지 않고 카메라만 움직임. 새로운 이미지(카드가 공중에 흩어진 구도)로 교체하고 모션 프롬프트도 전환 |
| **Leonardo 이미지 교체** | 탑뷰 쌓인 이미지 → 공중에 카드가 흩어진 mid-air 이미지로 변경. `close to the camera, large cards filling the entire frame` 추가로 카드 크기 확보 |
| **V2(최종) 프롬프트** | `Notification cards continuously fly in from all edges of the frame and pile up across the entire screen, cards tumbling and overlapping each other, filling from the edges toward the center, chaotic and urgent accumulation, fast-paced motion, dense layering effect.` |
| **V2 결과** | 카드들이 사방에서 날아와 화면 전체에 쌓이는 역동적인 영상 완성 ✅ |

---

### Scene 2 — Runway ML 영상 프롬프트 수정 (총 4회)

#### V1: 완전 정적

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `Fade in from white over 0.5 seconds, then hold completely still. No camera movement.` |
| **V1 결과** | 아무 움직임 없는 완전 정적 영상 |

#### V2: 360도 회전 시도 → 뒷면 액정 문제

| 구분 | 내용 |
|---|---|
| **V2 프롬프트** | `Smartphone slowly rises up from the bottom of the frame into the center, with a gentle subtle rotation, then softly floats in place.` |
| **V2 결과** | 회전 중 핸드폰 뒷면이 나타나는데 뒷면도 액정으로 생성됨. Runway가 뒷면 텍스처를 모르기 때문에 앞면 이미지를 그대로 복사하는 구조적 한계 |

#### V3: 회전 각도 제한 시도 → 여전히 뒷면 노출

| 구분 | 내용 |
|---|---|
| **V3 프롬프트** | `Smartphone slowly rises up from the bottom, screen always facing camera, gentle subtle tilt left and right up to 30 degrees, no rotation showing back.` |
| **V3 결과** | 여전히 뒷면이 보이는 문제 발생. 각도 제한만으로는 해결 불가 |

#### V4: 조명 스윕 → 빛 번쩍임 문제

| 구분 | 내용 |
|---|---|
| **V4 프롬프트** | `Smartphone slowly rises from below, soft studio light beam sweeps across the screen creating a gleaming highlight, screen always facing camera.` |
| **V4 결과** | 뒷면 노출 문제 해결됨. 단, 갑작스러운 빛 번쩍임이 과하게 표현됨 |

#### V5(최종): 부드러운 부유 효과

| 구분 | 내용 |
|---|---|
| **수정 이유** | 빛 번쩍임 제거, 5초 내내 자연스럽게 움직이도록 연속 모션 추가 |
| **최종 프롬프트** | `Smartphone slowly and gracefully rises from below into the center of the frame, then gently floats in place with a slow continuous subtle up and down drift, soft even lighting throughout with no flashes or highlights, screen always facing camera, smooth and unhurried motion filling the entire duration, premium elegant product feel.` |
| **최종 결과** | 뒷면 노출 없이 핸드폰이 부드럽게 떠오르며 자연스럽게 부유하는 영상 완성 ✅ |

---

### Scene 3 — Runway ML 영상 프롬프트 수정 없음

| 구분 | 내용 |
|---|---|
| **최종 프롬프트** | `Hand holding smartphone slowly raises up into frame from below, fingers gently scroll down on the screen with slow smooth motion, soft studio lighting, camera stays completely still, natural and calm hand movement throughout.` |
| **결과** | 손이 자연스럽게 올라오며 스크롤하는 영상 1회 완성 ✅ |

---

### Scene 4 — Runway ML 영상 프롬프트 수정 (총 3회) + 방향 전환

> 원래 계획: CapCut 페이드인만 사용. 제작 중 'o' 튀기기 애니메이션 아이디어 → 최종 수면 파동 효과로 확정

#### V1: 'o' 공 튀기기 시도 (Leonardo 새 이미지)

| 구분 | 내용 |
|---|---|
| **시도 내용** | "Clar"만 있는 새 Leonardo 이미지 생성 후 Runway에서 'o'가 위에서 떨어져 튀기는 애니메이션 시도 |
| **결과** | Leonardo가 'o'를 3D 구체 로고로 생성하거나 글자 스타일 불일치 발생. Runway도 특정 글자 하나만 정밀하게 튀기는 애니메이션 재현 불가 |
| **포기 이유** | 글자 단위 정밀 애니메이션은 Runway 구조적 한계. 전체 분위기(차분한 BGM + 내레이션)와 충격적인 낙하 효과가 맞지 않음 |

#### V2: 수면 파동 효과 (방향 전환)

| 구분 | 내용 |
|---|---|
| **V2 프롬프트** | `The text "Claro" and tagline subtly ripple and wave as if seen through a water surface disturbed by an invisible droplet, gentle undulating distortion spreads outward from the center of the text then slowly calms to perfectly still, no water visible, no droplet, only the ripple effect on the text itself, calm and elegant.` |
| **V2 결과** | 텍스트가 잔잔하게 일렁이다 정지하는 효과. 단, 양옆에 물 색깔이 살짝 보임 |

#### V3(최종): 물 색깔 제거 시도 후 V2 복귀

| 구분 | 내용 |
|---|---|
| **수정 이유** | 물 색깔 제거를 위해 `no water color, no water texture` 추가했으나 효과가 V2보다 나빠짐 |
| **최종 결정** | V2 프롬프트 유지. 양옆 물 색깔은 미세하게 보이지만 전체 분위기에 적합하다고 판단 ✅ |

---

### BGM (Suno) — 총 1회 수정

#### V1 → V2: 음침한 분위기 → 밝고 가벼운 사운드로 전환

| 구분 | 내용 |
|---|---|
| **V1 프롬프트** | `minimalist ambient, soft piano, no vocals, slow tempo, clean, 10 seconds, modern tech feel` |
| **V1 결과** | 차분하지만 음침하고 무거운 피아노 사운드 생성. 내레이션 목소리(Tim, 따뜻하고 허스키한 톤)와 분위기 불일치 |
| **수정 이유** | Tim의 따뜻·허스키한 목소리에는 어둡고 묵직한 피아노보다 밝고 공기감 있는 사운드가 적합. 목소리와 주파수대가 겹치지 않으면서 가볍게 받쳐주는 방향으로 전환 |
| **V2(최종) 프롬프트** | `bright minimalist ambient, airy synth pads, light and clean, uplifting but subtle, no vocals, slow tempo, modern tech advertisement, soft high notes, spacious and breathable` |
| **V2 결과** | 밝고 가벼운 앰비언트 사운드 생성. 내레이션 목소리와 자연스럽게 어울림 ✅ |

---

### Scene 4 — 수정 없음

| 구분 | 내용 |
|---|---|
| **프롬프트** | `pure white background, centered bold text "Claro" in dark charcoal, small blue filled circle above the text, tagline "Think Clear." in light gray below, small text "Download for free" at the bottom, ultra minimal, premium tech brand design` |
| **결과** | AI가 "claro"의 'o'를 파란 원으로 대체하는 로고 디자인을 자발적으로 생성. "Think Clear.", "Download for free" 텍스트 정확. 첫 시도에 브랜드 엔딩 화면 완성 ✅ |

---

## 05. 사용 도구 목록 & 선택 이유

| 분류 | 도구 | 대체 도구 | 선택 이유 |
|---|---|---|---|
| 이미지 생성 | **Leonardo AI** (Flux Schnell) | Adobe Firefly, Ideogram | 150 토큰/일 무료. Flux Schnell 모델로 크레딧 절약하면서 과제 수준 품질 충분. 미드저니 무료 플랜 종료로 대체 채택 |
| 영상 생성/변환 | **Runway ML Gen-4 Turbo** | Kling AI, Pika | Image→Video 카메라 모션 제어 정밀. Gen-4 Turbo로 일반 Gen-4 대비 크레딧 절약 |
| 내레이션 | **ElevenLabs** | GPT-4o mini TTS, Gemini 2.5 Pro TTS | 월 10,000자 무료. 한국어 발음 자연스럽고 목소리 선택 다양 |
| BGM | **Suno** | Udio, Mubert | 무료 티어로 앰비언트 BGM 생성 가능. 상업적 목적 아닌 교육용 사용 |
| 영상 편집 | **CapCut** | DaVinci Resolve | 초심자 친화적 타임라인. H.264/AAC 내보내기 지원 |

**도구 선택 우선순위:** 이 프로젝트에서는 **비용(무료 한도) > 접근성 > 품질** 순으로 우선순위를 두었다. 크레딧이 제한된 교육 환경에서 재생성 여유를 확보하는 것이 결과물 완성도보다 선행 조건이었기 때문이다. 품질이 중요한 씬(Scene 2 제품 등장)에는 Runway 크레딧을 집중 배분하고, 정적 씬(Scene 4)은 CapCut 편집으로 크레딧 소모를 줄였다.

---

## 06. 크레딧 예상 소모량

| 도구 | 작업 | 예상 소모 | 무료 한도 | 여유 |
|---|---|---|---|---|
| Leonardo AI | 이미지 4장 (Flux Schnell, 1376×768) | ≈ 40~60 토큰 | 150/일 | ✅ 충분 |
| Runway ML | Scene 1~4 영상 변환 (Gen-4 Turbo, 5s×4) | ≈ 100 크레딧 | 125 (일회성) | ⚠️ 1회 변환만 진행 |
| ElevenLabs | 내레이션 4줄 | ≈ 50자 | 10,000자/월 | ✅ 매우 여유 |
| Suno | BGM 1곡 | 1곡 | 50곡/일 | ✅ 매우 여유 |

> ⚠️ **Runway 주의:** 이미지 4장 완전 확정 후 영상 변환 시작.
> Scene 4는 CapCut 페이드인으로 대체해 크레딧 절약.

---

## 07. 일관성 유지 전략

| 항목 | 전략 |
|---|---|
| **스타일 고정** | 모든 씬 프롬프트에 동일 스타일 키워드(`pure white background`, `cool blue and light gray tones`, `minimalist`)를 공통 명시하고, 동일 모델(Flux Schnell)·동일 해상도로 생성해 씬 간 톤을 고정 |
| **컬러 팔레트** | 모든 프롬프트에 `pure white background` 공통 명시. 포인트 컬러는 blue 단일 유지 |
| **비율 통일** | 전 씬 1376×768 (16:9). Runway도 동일 비율 출력 설정 |
| **오디오 일관성** | ElevenLabs 4줄을 동일 Voice·Stability·Similarity 설정으로 한 세션에 생성 (세션 분리 시 톤 차이 발생) |

---

## 08. 소스 출처 선언 (저작권)

본 광고의 모든 시각·청각 소스는 생성형 AI 도구를 통해 직접 생성한 결과물만 사용하였다.

| 구분 | 소스 유형 | 도구 | 비고 |
|------|---------|------|------|
| 이미지 | AI 생성 | Leonardo AI (Flux Schnell) | 직접 촬영/스톡 이미지 미사용 |
| 영상 | AI 생성 | Runway ML Gen-4 Turbo | 유료 스톡 영상 미사용 |
| 내레이션 | AI 생성 | ElevenLabs | 실제 녹음 미사용 |
| BGM | AI 생성 | Suno | 라이선스 음원 미사용, 교육 목적 사용 |

직접 촬영 영상, 유료 스톡 영상(Shutterstock·Getty 등), 기성 음원은 일절 사용하지 않았다.

---

## 09. 제작 파이프라인 설계

**파이프라인 순서:** 기획 확정 → 이미지 생성 → 영상 변환 → 오디오 생성 → 최종 편집

```text
[1단계] 기획 확정 (스토리보드 작성)
        브랜드 아이덴티티·씬 구성·내레이션·프롬프트 초안을 모두 확정한 뒤 다음 단계 진입
        → 이유: 영상 변환은 크레딧 소모가 크므로, 이미지 확정 전 변환 금지

[2단계] 이미지 생성 (Leonardo AI)
        씬 1→2→3→4 순서로 키비주얼 생성. 각 씬 이미지가 확정될 때까지 반복 이터레이션
        → 이유: 비디오 변환 전 시각 방향을 100% 고정해야 재작업 최소화

[3단계] 영상 변환 (Runway ML)
        확정된 이미지 4장을 한 번에 Image→Video 변환 (Gen-4 Turbo, 5s×4)
        → 이유: 크레딧 일괄 소모 방지. 이미지 재변경 가능성 제거 후 진행

[4단계] 오디오 생성 (ElevenLabs + Suno)
        내레이션 4줄을 동일 세션에서 연속 생성. BGM은 내레이션 톤 확인 후 Suno 생성
        → 이유: 세션을 분리하면 ElevenLabs 목소리 톤이 미세하게 달라질 수 있음

[5단계] 최종 편집 (CapCut)
        scene-1~4.mp4 순서로 연결 → 내레이션 타이밍 맞춤 → BGM 믹스 → 페이드아웃 적용
        → 이유: 편집은 AI 생성 완료 후 "통합" 목적으로만 사용, 핵심 비주얼 생성에 관여 안 함
```

이 순서를 지킨 핵심 이유는 **크레딧 역방향 소모 방지**다. 이미지가 확정되지 않은 상태에서 영상 변환을 먼저 시도하면, 이미지 수정 시 영상도 재변환해야 해 크레딧이 2배로 소모된다.

---

## 10. 파일 네이밍 규칙

```text
scene-{n}.jpg              키비주얼 이미지 (n = 씬 번호)
scene-{n}.mp4              씬별 영상 클립
scene-{n}-narration.mp3    씬별 내레이션 오디오
bgm.mp3                    전체 공통 BGM (씬 번호 없음 — 전 씬에 걸쳐 사용)
claro-brand-ad.mp4         최종 편집본
```

**규칙 설계 의도:**

- `scene-{n}` 접두사로 씬 번호를 파일명에 고정 → CapCut 타임라인에서 씬 순서를 파일명만으로 즉시 파악 가능
- 미디어 타입(이미지/영상/오디오)은 확장자로 구분 → 같은 씬의 소스를 한 폴더에서 타입별로 찾을 수 있음
- `narration` 접미사를 명시해 BGM(`bgm.mp3`)과 혼동 방지
- 최종 편집본은 브랜드명을 포함한 별도 파일명으로 제출용과 소스용을 분리

---

## 11. Text-to-Image → Image-to-Video 역할 분담

| 구분 | Text-to-Image (T2I) | Image-to-Video (I2V) |
|------|--------------------|--------------------|
| **입력** | 텍스트 프롬프트 | 확정된 이미지 + 모션 프롬프트 |
| **제어 수준** | 구도·색감·피사체를 프롬프트로 완전 제어 | 첫 프레임이 이미 고정되어 있어 구도 변경 불가 |
| **일관성** | 생성할 때마다 결과가 달라짐 | 첫 프레임 기반이므로 씬 전환 시 스타일 유지 쉬움 |
| **크레딧** | 저렴 (Leonardo Flux Schnell ≈ 10토큰/장) | 고가 (Runway Gen-4 Turbo ≈ 25크레딧/5s) |
| **모션 품질** | 해당 없음 | 카메라 무빙·오브젝트 모션 자연스러움 |

**이 프로젝트에서는 T2I와 I2V를 택일하지 않고 둘 다 순차로 사용했다.** T2I(Leonardo)로 키비주얼을 먼저 확정하고, 그 이미지를 I2V(Runway)에 넣어 모션을 입히는 파이프라인이다. 즉 위 표는 "둘 중 하나를 고르기 위한 비교"가 아니라, 두 방식이 각각 어떤 역할을 맡는지를 정리한 것이다.

**역할을 이렇게 나눈 이유:**

T2I만으로(매 프레임을 텍스트로) 영상을 만들면 프레임마다 스타일이 달라져 광고 전체의 톤앤매너 일관성이 무너진다. 그래서 구도·색감·피사체는 저렴한 T2I로 완전히 확정해두고, 비싼 I2V는 그 확정된 첫 프레임에 모션만 더하는 용도로 한정했다. 이렇게 하면 ① 첫 프레임이 고정되어 씬 간 스타일 불일치 위험이 줄고, ② 이미지가 100% 확정된 뒤에만 I2V를 돌려 재생성(=크레딧 낭비)을 최소화할 수 있다. T2I는 "무엇을 보여줄지"를, I2V는 "그것을 어떻게 움직일지"를 담당하는 분업 구조다.

---

## 12. 스타일 일관성 제어 상세

**스타일 일관성 제어 설정 (프롬프트 + 모델 고정 방식)**

| 항목 | 설정값 | 이유 |
|------|--------|------|
| 공통 스타일 키워드 | `pure white background`, `cool blue and light gray tones`, `minimalist` | 모든 씬 프롬프트에 동일하게 포함해 톤·색감을 고정 |
| 모델 고정 | Flux Schnell | 동일 모델로 생성해 씬 간 화풍 차이 방지 |
| 해상도·비율 고정 | 1376×768 (16:9) | 씬 간 화질·비율 차이 방지, Runway 출력도 동일 비율 |
| 포인트 컬러 고정 | blue 단일 | 강조색을 하나로 제한해 시각적 통일 |

> 📌 별도의 텍스트 프롬프트가 붙는 게 아니라 위 키워드를 매 씬 프롬프트에 공통 포함하는 방식으로 일관성을 확보했다. (Leonardo의 Image/Style Reference 기능 사용 여부는 생성 히스토리에서 확인 후, 실제 사용했다면 reference 타입·강도를 여기에 추가 기재할 것)

**씬 간 불일치 발생 여부**

실제 제작 과정에서 씬 간 색감·밝기 불일치는 발생하지 않았다. 모든 씬에 `pure white background`와 동일한 컬러 키워드를 명시하고, 동일 모델(Flux Schnell)·동일 해상도로 생성했기 때문에 CapCut 편집 단계에서 별도 색보정 없이 통합이 가능했다. ElevenLabs 내레이션도 동일 Voice·동일 세션에서 연속 생성해 씬 간 톤 차이가 없었다.

---

## 13. 대체 도구 비교 예측

동일 스토리보드를 다른 도구로 제작했을 때 예상되는 차이:

**영상 생성: Runway ML → Kling AI**

Kling AI는 피사체의 자세·동작 유지 능력이 강해 Scene 3(손 스크롤)에서 손 모양 왜곡이 더 적었을 가능성이 높다. 반면 카메라 무빙 제어(Scene 2 스마트폰 부유)는 Runway Gen-4 Turbo가 더 정밀하다는 평가가 많아 Scene 2 품질은 떨어질 수 있다. 크레딧 단가는 Kling이 저렴한 편이라 예산 부담은 줄어든다.

**영상 생성: Runway ML → Pika**

Pika는 짧은 루프 모션(1~3초)에 강하지만 5초짜리 연속 모션에서는 Runway보다 일관성이 낮을 수 있다. Scene 1(카드 쌓임 동적 효과)처럼 오브젝트가 복잡하게 움직이는 장면에서 품질 저하가 예상된다. 인터페이스가 단순해 초심자에게 접근성은 더 좋다.

**이미지 생성: Leonardo AI → Adobe Firefly**

Firefly는 상업적 저작권이 명확하게 보장되는 것이 장점이나, Flux Schnell 대비 생성 속도가 느리고 무료 크레딧 한도가 낮다. 스타일 일관성 측면에서는 Firefly의 Style Reference 기능이 Leonardo의 Image Reference와 유사하게 동작한다.

---

## 14. 크레딧 부족 시 대응 전략

Runway ML 크레딧(125, 일회성)이 부족해지는 경우 아래 우선순위로 전략을 조정한다.

**전략 1 — 씬 수 축소 (권장)**

Scene 1(혼돈)과 Scene 4(브랜드 각인)는 광고의 기·결에 해당해 생략 불가. Scene 2(앱 등장)를 정지 이미지 + CapCut 줌인 모션으로 대체하고 Scene 3(손 스크롤) 영상만 Runway로 생성해 크레딧을 약 25개 절약한다.

**전략 2 — 정지 이미지 + 패닝/줌 대체**

Runway 영상 변환 대신 CapCut의 Ken Burns 효과(슬로우 줌인/아웃)를 사용해 정지 이미지에 모션감을 부여한다. 광고의 미니멀·프리미엄 톤에서는 과도한 모션보다 정적인 줌이 브랜드 감성에 오히려 잘 맞는다.

**전략 3 — Gen-4 Turbo 유지, 씬 길이 단축**

5초 × 4씬 대신 3초 × 4씬으로 줄이면 크레딧 소모가 약 40% 감소한다. 단, Runway 최소 생성 단위(보통 3~5초) 확인 필요.

---

## 15. 최종 영상 스펙

| 항목 | 내용 |
|---|---|
| **파일명** | `claro-brand-ad.mp4` |
| **총 길이** | 약 20초 (Scene1~4 각 5s, Runway 최소 생성 단위 유지) |
| **해상도** | 1920×1080 (1080p — CapCut 내보내기 설정) |
| **프레임레이트** | 30fps |
| **비디오 코덱** | H.264 |
| **오디오 코덱** | AAC |
| **편집 순서** | scene-1.mp4 → scene-2.mp4 → scene-3.mp4 → scene-4.mp4 (각 5초) |
| **오디오 믹스** | 내레이션 4개 (볼륨 100%) + bgm.mp3 (볼륨 20~30%, Scene 4 끝에서 페이드아웃) |
| **영상 엔딩** | Scene 4 마지막 클립에 페이드아웃 효과 적용 (CapCut 아웃 애니메이션, 1~1.5초) |
| **편집 도구** | CapCut |
