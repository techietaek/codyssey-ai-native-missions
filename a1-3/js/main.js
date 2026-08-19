/* ============================================================
   취미핏 (HobbyFit) — 프론트엔드 로직
   - 모바일 메뉴 / 다크모드 토글
   - AI 추천: 사용자 입력 → fetch('/api/recommend') → 화면 렌더
   - 실패 처리 3종: 빈 입력 / API 오류(4xx·5xx) / 타임아웃
   ============================================================ */

(function () {
  "use strict";

  /* ---------- 1) 모바일 네비게이션 토글 ---------- */
  const navToggle = document.getElementById("navToggle");
  const navMenu = document.getElementById("navMenu");

  navToggle.addEventListener("click", () => {
    const open = navMenu.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(open));
  });
  // 메뉴 항목 클릭 시 자동 닫기 (모바일)
  navMenu.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      navMenu.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    })
  );

  /* ---------- 2) 다크모드 토글 (보너스: UX) ---------- */
  const themeToggle = document.getElementById("themeToggle");
  const themeIcon = themeToggle.querySelector(".theme-icon");
  const root = document.documentElement;

  // 저장된 설정 또는 OS 선호도로 초기화
  const saved = localStorage.getItem("hobbyfit-theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const initial = saved || (prefersDark ? "dark" : "light");
  applyTheme(initial);

  themeToggle.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(next);
    localStorage.setItem("hobbyfit-theme", next);
  });

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    themeIcon.textContent = theme === "dark" ? "☀️" : "🌙";
  }

  /* ---------- 3) AI 추천 폼 ---------- */
  const form = document.getElementById("recoForm");
  const submitBtn = document.getElementById("submitBtn");
  const formMsg = document.getElementById("formMsg");
  const resultArea = document.getElementById("resultArea");

  const TIMEOUT_MS = 25000; // 25초 이상 응답 없으면 타임아웃 처리

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearMsg();

    // --- 실패 처리 ①: 빈 입력(필수값 누락) ---
    const payload = {
      personality: form.personality.value.trim(),
      hours: form.hours.value.trim(),
      budget: form.budget.value.trim(),
      place: form.place.value.trim(),
      note: form.note.value.trim(),
    };
    const missing = ["personality", "hours", "budget", "place"].some(
      (k) => !payload[k]
    );
    if (missing) {
      showMsg("성향·여가시간·예산·선호 장소는 필수 항목입니다. 모두 선택해 주세요.", "error");
      return;
    }

    // 로딩 상태 (마이크로 인터랙션)
    setLoading(true);
    renderLoading();

    // --- 실패 처리 ③: 타임아웃 (AbortController) ---
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);

    try {
      const res = await fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        signal: controller.signal,
      });

      // --- 실패 처리 ②: API 오류(4xx / 5xx) ---
      if (!res.ok) {
        let detail = "";
        try {
          const err = await res.json();
          detail = err.error || "";
        } catch (_) {}
        throw new Error(detail || `서버 오류 (HTTP ${res.status})`);
      }

      const data = await res.json();
      if (!data.recommendations || !data.recommendations.length) {
        throw new Error("추천 결과를 만들지 못했어요. 입력을 조금 바꿔 다시 시도해 주세요.");
      }
      renderResults(data.recommendations);
    } catch (err) {
      if (err.name === "AbortError") {
        // 타임아웃 안내
        renderError(
          "응답이 지연되고 있어요 ⏳",
          "AI 응답이 25초 안에 도착하지 않았습니다. 네트워크 상태를 확인하고 잠시 후 다시 시도해 주세요."
        );
      } else {
        // API/기타 오류 안내
        renderError("추천을 불러오지 못했어요 😢", err.message || "잠시 후 다시 시도해 주세요.");
      }
    } finally {
      clearTimeout(timer);
      setLoading(false);
    }
  });

  /* ---------- 렌더링 헬퍼 ---------- */
  function renderLoading() {
    resultArea.innerHTML =
      '<div class="loading"><div class="spinner"></div>AI가 당신에게 맞는 취미를 고르는 중...</div>';
  }

  function renderError(title, message) {
    resultArea.innerHTML =
      '<div class="state-error"><h3>' +
      escapeHtml(title) +
      "</h3><p>" +
      escapeHtml(message) +
      "</p></div>";
  }

  function renderResults(list) {
    const cards = list
      .slice(0, 3)
      .map(
        (r) =>
          '<article class="reco-card">' +
          "<h4>" +
          escapeHtml(r.title || "추천 취미") +
          "</h4>" +
          '<p class="why">' +
          escapeHtml(r.reason || "") +
          "</p>" +
          '<p class="tip"><b>시작 팁 ·</b> ' +
          escapeHtml(r.tip || "") +
          "</p>" +
          "</article>"
      )
      .join("");
    resultArea.innerHTML =
      '<p class="result-intro">✨ 당신을 위한 취미 추천이 도착했어요!</p>' +
      '<div class="result-grid">' +
      cards +
      "</div>";
  }

  function setLoading(on) {
    submitBtn.disabled = on;
    submitBtn.textContent = on ? "추천 생성 중..." : "✨ AI 추천받기";
  }
  function showMsg(text, type) {
    formMsg.textContent = text;
    formMsg.className = "form-msg " + (type || "");
  }
  function clearMsg() {
    formMsg.textContent = "";
    formMsg.className = "form-msg";
  }
  function escapeHtml(str) {
    return String(str).replace(/[&<>"']/g, (m) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    }[m]));
  }

  /* ---------- 4) 문의 폼 (클라이언트 검증 데모) ---------- */
  const contactForm = document.getElementById("contactForm");
  const contactMsg = document.getElementById("contactMsg");

  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = contactForm.name.value.trim();
    const email = contactForm.email.value.trim();
    const message = contactForm.message.value.trim();

    if (!name || !email || !message) {
      contactMsg.textContent = "이름·이메일·내용을 모두 입력해 주세요.";
      contactMsg.className = "form-msg error";
      return;
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      contactMsg.textContent = "이메일 형식을 확인해 주세요.";
      contactMsg.className = "form-msg error";
      return;
    }
    // 데모: 실제 전송 대신 확인 메시지 (보너스로 서버 연동/노코드 자동화 확장 가능)
    contactMsg.textContent = "문의가 접수되었습니다. 감사합니다! 🙌";
    contactMsg.className = "form-msg ok";
    contactForm.reset();
  });
})();
