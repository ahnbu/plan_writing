---
name: strategy-redteamer
description: 전략 수립 3단계(방어 및 연마)를 수행합니다. 레드팀과 블루팀의 3단계 상호 비평 루프(Recursive Debate)를 통해 논리를 극한으로 검증합니다.
tools: [read_file, write_file, perplexity_ask, view_file]
---

# Phase 3: The Red Teamer (Recursive Debate)

**목표**: 단순한 검토가 아닌, 치열한 **"공격(Red) vs 방어(Blue)"**의 변증법적 토론을 통해 전략의 사각지대를 제거하고 완성도를 높입니다.

## Workflow: 3-Round Debate Spiral

### Round 1: The Attack (취약점 타격)

1.  **Red Team Attack**: `.agent/skills/strategy-redteamer/prompts/1_red_team_critic.md` 실행
    - 목표: 현재 전략의 가장 아픈 곳(Fatal Flaw)을 식별.
    - 결과: **저장**: `11_debate_round1_attack.md`
2.  **Blue Team Defense**: `.agent/skills/strategy-redteamer/prompts/2_blue_team_insight.md` 실행
    - 목표: 식별된 약점에 대한 즉각적인 방어 논리(Defense Logic) 수립.
    - 결과: **저장**: `12_debate_round1_defense.md`

### Round 2: The Counter-Attack (재반박)

3.  **Red Team Rebuttal**: 결과물(`12_debate_round1_defense.md`)을 읽고 재반박 수행.
    - Prompt: `.agent/skills/strategy-redteamer/prompts/2a_red_team_rebuttal.md` 실행
    - 결과: **저장**: `13_debate_round2_rebuttal.md`
4.  **Blue Team Evolution**: 재반박을 수용하여 논리를 수정(Pivot)하거나 보강.
    - Prompt: `.agent/skills/strategy-redteamer/prompts/2b_blue_team_evolution.md` 실행
    - 결과: **저장**: `14_debate_round2_evolution.md`

### Round 3: The Synthesis (통합 및 완성)

5.  **Final Synthesis**: 논쟁의 과정을 통합하여 제3의 대안을 도출.
    - 실행: `.agent/skills/strategy-redteamer/prompts/3_defense_logic.md` (통합용으로 프롬프트 활용)
    - 결과: **저장**: `14_debate_round3_synthesis.md`

### Final Output

6.  **최종 보고서 작성 (The Masterpiece)**
    - 실행: `.agent/skills/strategy-redteamer/prompts/4_final_polish.md`
    - 입력: `14_debate_round3_synthesis.md` 및 이전 리서치 자료.
    - 결과: **저장**: `15_FINAL_REPORT.md`
7.  **최종 보고서 확장 (Deep-Dive Expanded)**
    - **목적**: 작성된 `15_FINAL_REPORT.md`를 바탕으로, 논리와 근거 데이터를 3배 이상 심층적으로 보강합니다.
    - 실행: `.agent/skills/util-workflow-engineer/prompts/content_expander.md` 활용
    - 입력: `15_FINAL_REPORT.md`
    - 결과: **저장**: `15_FINAL_REPORT_expanded.md` (Deep-Dive Version)

8.  **📋 Task Progress Update (Mandatory)**: `task.md` 파일을 열어 Phase 3에서 완료한 모든 항목의 체크박스를 `[ ]` → `[✅]`로 변경하고, Phase 3 헤더를 `[ ]` → `[✅ Done]`으로 업데이트하십시오.
9.  **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 실행.
    - **Target File**: `14_debate_round3_synthesis.md` 및 `15_FINAL_REPORT_expanded.md` (논쟁의 결론 및 최종 확장본 기록)
