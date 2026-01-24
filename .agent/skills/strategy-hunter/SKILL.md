---
name: strategy-hunter
description: 전략 수립 2단계(검증)를 수행합니다. 심층 리서치, 팩트 체크, 근거 기반의 가설 검증.
tools: [read_file, write_file, perplexity_ask]
---

# Phase 2: The Hunter (검증)

**목표**: 팩트를 찾아 가설을 검증하고 의미를 도출합니다.

## Workflow

1.  **검증 리서치 설계**: `.agent/skills/strategy-hunter/prompts/1_meta_plan.md` 실행
    - 결과: Research Blueprint -> **저장**: `07_verification_plan.md`
2.  **리서치 실행 (Util 호출)**: `util-research-runner` 스킬을 사용하여 리서치 수행
    - 참조: `.agent/skills/util-research-runner/SKILL.md`
    - 결과: Verification Evidence & Logs -> **저장**: `research/02_Phase2_Verification_Log.md`
3.  **팩트 체크**: `.agent/skills/strategy-hunter/prompts/2_fact_check.md` 실행
    - 결과: Verified Facts List -> **저장**: `09_verified_facts.md`
4.  **전략 종합**: `.agent/skills/strategy-hunter/prompts/3_synthesis.md` 실행
    - 결과: **저장**: `10_ghost_deck_v2.md`
5.  **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 사용하여 단계 기록
