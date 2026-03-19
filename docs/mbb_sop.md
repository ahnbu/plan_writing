확정된 **The Strategy Master (MBB Edition)** 구조에 따라, 각 모듈(파일)에 들어갈 상세 정의(Prompt Spec & Logic)를 작성했습니다.

이 명세서는 실제 에이전트가 **MBB 컨설턴트의 사고 과정(8 Steps)**을 그대로 수행하도록 설계되었습니다.

---

## 📂 1. Global Context (`config.yaml`)

모든 에이전트가 공유하는 **'전략 수립의 대원칙'**입니다.

```yaml
project:
  target_audience: "C-Level Executives (CEO, CFO, CSO)"
  tone_and_manner: "Professional, Assertive, Hypothesis-Driven (MBB Style)"

constraints:
  - "모든 주장은 정량적 근거(Data)나 논리적 추론(Logic)으로 뒷받침되어야 한다."
  - "모호한 형용사('상당한', '많은', '좋은') 사용을 엄격히 금지한다."
  - "결론부터 말하는 두괄식(Answer First) 구조를 유지한다."

output_rules:
  format: "Markdown"
  language: "Korean (Technical terms in English)"
```

---

## 📂 2. Phase 1: The Framer (구조화)

**Goal:** 시장을 읽고(`Scan`), 문제를 정의하고(`Define`), 쪼개고(`Structure`), 계획(`Plan`)합니다.

### `prompts/01_framer/1_market_scan.md` (Scan)

- **Role:** Market Scout
- **Task:** 사용자의 주제와 관련하여 현재 시장에서 가장 뜨거운 **화두(Buzzwords), 주요 플레이어, 거시적 트렌드**를 빠르게 파악하십시오.
- **Constraint:** 깊은 분석은 필요 없습니다. 우리가 엉뚱한 방향으로 가설을 세우지 않도록 '현재의 지형도'만 그리세요.
- **Output:** `Key Trends`, `Major Competitors`, `Recent Disruptions`

### `prompts/01_framer/2_scr_context.md` (Define)

- **Role:** Engagement Manager
- **Input:** User Request + Market Scan Result
- **Task:** **SCR 프레임워크**를 사용하여 '우리가 해결해야 할 문제'를 한 문장으로 정의하십시오.
- **Situation (S):** 논란의 여지가 없는 현재의 사실/배경
- **Complication (C):** S에서 발생한 문제, 위협, 또는 변화 (Why now?)
- **Resolution (R):** C를 해결하기 위해 우리가 답해야 할 **핵심 질문(Key Question)**
- **Output:** `Problem Statement Worksheet`

### `prompts/01_framer/3_issue_tree.md` (Structure & Prioritize)

- **Role:** Structural Thinker
- **Input:** Problem Statement (SCR)
- **Task:**

1. 핵심 질문(R)을 3~4개의 상위 이슈로 분해하십시오 (MECE 원칙 준수).
2. **Prioritization (80/20 Rule):** 분해된 이슈 중 임팩트가 낮거나 실행 불가능한 가지(Branch)는 과감히 잘라내십시오(Pruning).
3. 살아남은 이슈들에 대해 'Why/How'를 반복하여 3단계 깊이(Depth)까지 들어가십시오.

- **Output:** `Prioritized Issue Tree`

### `prompts/01_framer/4_ghost_draft.md` (Plan)

- **Role:** Slide Planner
- **Input:** Prioritized Issue Tree
- **Task:** 이슈 트리의 각 말단 노드(Leaf Node)를 하나의 슬라이드로 전환하는 **Ghost Deck**을 설계하십시오.
- **Slide Title:** 해당 장표가 말하고자 하는 메시지 (가설)
- **Placeholder:** 들어갈 데이터의 형태 (예: "경쟁사 A와 B의 매출 추이 그래프")
- **Tagging:** 팩트 확인이 필요한 모든 문장에 `[VERIFY: 검증할 구체적 내용]` 태그를 붙이십시오.
- **Output:** `Ghost Deck v1.0`

---

## 📂 3. Phase 2: The Hunter (검증 및 종합)

**Goal:** 빈칸을 채우고(`Analyze`), 팩트를 연결하여 의미를 찾습니다(`Synthesize`).

### `prompts/02_hunter/1_meta_plan.md` (Workplan)

- **Role:** Research Architect
- **Input:** Ghost Deck v1.0 (with `[VERIFY]` tags)
- **Task:** 각 `[VERIFY]` 태그를 해결하기 위한 **'리서치 작전 지도'**를 짜십시오.
- **Source:** 어디서 찾을 것인가? (Statista, 10-K Reports, News, Tech Blogs)
- **Query:** Perplexity에게 던질 최적의 질문은? (수치 중심, 비교 중심)
- **Killer Fact:** 이 가설을 입증하기 위해 찾아야 할 단 하나의 숫자는 무엇인가?
- **Output:** `Research Action Plan (JSON)`

### `prompts/02_hunter/2_fact_check.md` (Analyze)

- **Role:** Fact Auditor
- **Input:** Research Action Plan + Search Results (from MCP)
- **Task:** 수집된 데이터와 기존 가설을 대조하십시오.
- **Support:** 데이터가 가설을 지지함 -> 데이터 인용
- **Refute:** 데이터가 가설과 반대됨 -> **가설 수정(Pivot)** 및 수정된 근거 제시
- **Nuance:** 맞긴 한데 조건이 붙음 -> 조건 명시
- **Output:** `Verified Facts List`

### `prompts/02_hunter/3_synthesis.md` (Synthesize)

- **Role:** Strategy Insight Generator
- **Input:** Ghost Deck v1.0 + Verified Facts List
- **Task:** 단순한 '데이터 주입'을 넘어 **Synthesis(종합)**를 수행하십시오.
- 흩어진 팩트들을 연결하여 **"So What? (그래서 이것이 전략에 어떤 의미인가?)"**를 도출하십시오.
- Ghost Deck의 내용을 팩트 기반으로 다시 쓰고(Rewrite), 시사점을 강화하십시오.
- **Output:** `Ghost Deck v2.0 (Fact-based)`

---

## 📂 4. Phase 3: The Red Teamer (방어 및 전달)

**Goal:** 합의를 이끌어내고(`Syndicate`), 논리를 보강하고(`Refine`), 완벽하게 전달합니다(`Communicate`).

### `prompts/03_red_teamer/1_c_level_critic.md` (Syndicate)

- **Role:** Devil's Advocate (Simulated CFO/VC)
- **Input:** Ghost Deck v2.0
- **Task:** 당신은 의심 많고 냉철한 투자 결정권자입니다. 이 보고서를 승인하지 않을 **치명적인 이유 3가지만** 꼽으십시오.
- _Focus:_ ROI 불확실성, 숨겨진 리스크, 실행 가능성(Feasibility), 경쟁사의 반격.
- **Output:** `Critical Risk Assessment`

### `prompts/03_red_teamer/2_defense_logic.md` (Refine)

- **Role:** Logic Defender
- **Input:** Critical Risk Assessment
- **Task:** 지적된 리스크를 방어하십시오.
- **Logic:** 논리적으로 반박하거나, 리스크 헷징(Risk Hedging) 전략을 추가하십시오.
- **Data:** 방어에 필요한 데이터가 부족하다면 **"추가 리서치 쿼리"**를 생성하여 즉시 Perplexity MCP를 호출하십시오.
- **Output:** `Defensed Logic & Updates`

### `prompts/03_red_teamer/3_final_polish.md` (Communicate)

- **Role:** McKinsey Communication Specialist
- **Input:** Ghost Deck v2.0 + Defensed Logic
- **Task:** **Minto Pyramid Principle**에 따라 최종 보고서를 완성하십시오.
- **Executive Summary:** 전체 내용을 1페이지로 요약 (S-C-R 구조).
- **Action Title:** 모든 슬라이드 제목은 '완결된 메시지 문장'으로 교체.
- **Tone:** 비즈니스 프로페셔널 톤으로 문장 다듬기.
- **Output:** `Final Strategy Report (vFinal)`

---

## 📂 5. The Orchestrator (`SKILL.md`)

이 모든 과정을 지휘하는 **Skill Definition** 파일입니다.

```markdown
---
name: strategy-master
description: MBB 스타일의 전략 수립 풀 프로세스 (Scan-Define-Structure-Plan-Analyze-Synthesize-Syndicate-Communicate)를 수행합니다.
tools: [perplexity_ask, read_file, write_file]
---

# The Strategy Master Workflow

1.  **[Phase 1] Framer Initialization**
    - `1_market_scan.md` 로드 및 실행 (Tool: perplexity_ask)
    - `2_scr_context.md` 로드 및 실행 (입력: 위 검색 결과)
    - `3_issue_tree.md` 로드 및 실행 (입력: SCR)
    - `4_ghost_draft.md` 로드 및 실행 (입력: Issue Tree) -> **SAVE: ghost_deck_v1.md**

2.  **[Phase 2] Hunter Verification**
    - `1_meta_plan.md` 로드 및 실행 (입력: ghost_deck_v1.md) -> **Extract Tags & Plan Search**
    - **LOOP:** 계획된 쿼리에 대해 `perplexity_ask` 실행 (다중 턴)
    - `2_fact_check.md` 로드 및 실행 (입력: 검색 결과 + 기존 가설)
    - `3_synthesis.md` 로드 및 실행 (입력: Verified Facts) -> **SAVE: ghost_deck_v2.md**

3.  **[Phase 3] Red Team Finalization**
    - `1_c_level_critic.md` 로드 및 실행 (입력: ghost_deck_v2.md)
    - `2_defense_logic.md` 로드 및 실행 (입력: Critic 결과)
      - _(IF needed)_ 추가 `perplexity_ask` 실행
    - `3_final_polish.md` 로드 및 실행 (입력: ghost_deck_v2 + Defense) -> **SAVE: FINAL_REPORT.md**
```

이 상세 정의는 **사용자님이 원하셨던 MBB 컨설턴트의 실제 업무 흐름을 에이전트 워크플로우로 완벽하게 치환**한 것입니다. 각 단계는 앞 단계의 결과물을 받아 더 깊이 있게 발전시킵니다.
