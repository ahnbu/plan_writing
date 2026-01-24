---
name: strategy-master
description: MBB 스타일의 전략 수립 풀 프로세스 (Scan-Define-Structure-Plan-Analyze-Synthesize-Syndicate-Communicate)를 수행합니다.
tools: [perplexity_ask, read_file, write_file]
---

# The Strategy Master Workflow

이 스킬은 4단계(구조화 -> 검증 -> 방어 -> 시각화)로 구성된 전략 기획 프로세스를 수행합니다.

## 산출물 관리 (Output Management)

모든 산출물은 `output/YYYYMMDD_{keyword}/` 폴더에 저장됩니다.
리서치 원본 데이터는 `output/YYYYMMDD_{keyword}/research/` 폴더에 별도 보관됩니다.

## 1단계: 구조화 (The Framer)

**목표**: 문제를 정의하고 가설을 수립하여 'Ghost Deck'을 설계합니다.

1. **초기 설정**: 출력 폴더 및 리서치 폴더 생성 (`output/YYYYMMDD_{keyword}/research/`)
2. **리서치 설계**: `prompts/01_framer/1_research_design.md` 실행
   - 결과: Research Blueprint -> **저장**: `01_research_blueprint.md`
3. **리서치 실행**: `prompts/00_utils/research_runner.md` 실행
   - 결과: Research Report & Logs -> **저장**: `research/01_Phase1_Research_Report.md`
4. **맥락 종합**: `prompts/01_framer/2_context_synthesis.md` 실행
   - 결과: Context Insight -> **저장**: `03_context_insight.md`
5. **문제 정의**: `prompts/01_framer/3_scr_context.md` 실행
   - 결과: SCR Problem Statement -> **저장**: `04_scr_problem.md`
6. **구조화**: `prompts/01_framer/4_issue_tree.md` 실행
   - 결과: Issue Tree -> **저장**: `05_issue_tree.md`
7. **가설 수립**: `prompts/01_framer/5_ghost_draft.md` 실행
   - 결과: **저장**: `06_ghost_deck_v1.md`
8. **📜 기록 보관**: `prompts/00_utils/history_keeper.md` 실행

## 2단계: 검증 (The Hunter)

**목표**: 팩트를 찾아 가설을 검증하고 의미를 도출합니다.

1. **검증 리서치 설계**: `prompts/02_hunter/1_meta_plan.md` 실행
   - 결과: Research Blueprint -> **저장**: `07_verification_plan.md`
2. **리서치 실행**: `prompts/00_utils/research_runner.md` 실행
   - 결과: Verification Evidence & Logs -> **저장**: `research/02_Phase2_Verification_Log.md`
3. **팩트 체크**: `prompts/02_hunter/2_fact_check.md` 실행
   - 결과: Verified Facts List -> **저장**: `09_verified_facts.md`
4. **전략 종합**: `prompts/02_hunter/3_synthesis.md` 실행
   - 결과: **저장**: `10_ghost_deck_v2.md`
5. **📜 기록 보관**: `prompts/00_utils/history_keeper.md` 실행

## 3단계: 방어 및 연마 (The Red Teamer)

**목표**: 비판적/창의적 시각으로 완성도를 높이고 최종 전략 보고서를 작성합니다.

1. **약점 분석 (Red Team)**: `prompts/03_red_teamer/1_red_team_critic.md` 실행
   - 결과: Critical Risks -> **저장**: `11_red_team_risks.md`
2. **관점 전환 (Blue Team)**: `prompts/03_red_teamer/2_blue_team_insight.md` 실행
   - 결과: Visionary Insights -> **저장**: `12_blue_team_insights.md`
3. **방어 논리 보강**: `prompts/03_red_teamer/3_defense_logic.md` 실행
   - 결과: Defense & Evolution Plan -> **저장**: `13_defense_plan.md`
4. **리서치 실행**: `prompts/00_utils/research_runner.md` 실행
   - 결과: Defense Evidence & Logs -> **저장**: `research/03_Phase3_Defense_Log.md`
5. **최종 보고서 작성**: `prompts/03_red_teamer/4_final_polish.md` 실행
   - 결과: **저장**: `15_FINAL_REPORT.md`
6. **📜 기록 보관**: `prompts/00_utils/history_keeper.md` 실행

## 4단계: 시각화 기획 (PT Planner)

**목표**: 최종 보고서를 설득력 있는 PPT 슬라이드 설계도로 변환합니다.

1. **내러티브 설계**: `prompts/04_presentation/1_narrative_design.md` 실행
   - 결과: Storyline -> **저장**: `16_storyline.md`
2. **슬라이드 상세 설계**: `prompts/04_presentation/2_slide_plan.md` 실행
   - 결과: Slide-by-Slide Plan -> **저장**: `17_slide_plan.md`
3. **📜 기록 보관**: `prompts/00_utils/history_keeper.md` 실행
