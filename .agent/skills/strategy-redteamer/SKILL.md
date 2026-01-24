---
name: strategy-redteamer
description: 전략 수립 3단계(방어 및 연마)를 수행합니다. 비판적 분석(Red Teaming), 반론 방어, 최종 보고서 작성.
tools: [read_file, write_file, perplexity_ask]
---

# Phase 3: The Red Teamer (방어 및 연마)

**목표**: 비판적/창의적 시각으로 완성도를 높이고 최종 전략 보고서를 작성합니다.

## Workflow

1.  **약점 분석 (Red Team)**: `.agent/skills/strategy-redteamer/prompts/1_red_team_critic.md` 실행
    - 결과: Critical Risks -> **저장**: `11_red_team_risks.md`
2.  **관점 전환 (Blue Team)**: `.agent/skills/strategy-redteamer/prompts/2_blue_team_insight.md` 실행
    - 결과: Visionary Insights -> **저장**: `12_blue_team_insights.md`
3.  **방어 논리 보강**: `.agent/skills/strategy-redteamer/prompts/3_defense_logic.md` 실행
    - 결과: Defense & Evolution Plan -> **저장**: `13_defense_plan.md`
4.  **리서치 실행 (Util 호출)**: 필요 시 `util-research-runner` 스킬을 사용하여 추가 증거 수집
    - 결과: Defense Evidence & Logs -> **저장**: `research/03_Phase3_Defense_Log.md`
5.  **최종 보고서 작성**: `.agent/skills/strategy-redteamer/prompts/4_final_polish.md` 실행
    - 결과: **저장**: `15_FINAL_REPORT.md`
6.  **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 사용하여 단계 기록
