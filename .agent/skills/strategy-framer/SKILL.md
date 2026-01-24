---
name: strategy-framer
description: 전략 수립 1단계(구조화)를 수행합니다. 문제 정의, 이슈 트리 작성, 초기 가설(Ghost Deck) 수립.
tools: [read_file, write_file, perplexity_ask]
---

# Phase 1: The Framer (구조화)

**목표**: 문제를 정의하고 가설을 수립하여 'Ghost Deck'을 설계합니다.

## Workflow

1.  **초기 설정**: 출력 폴더 및 리서치 폴더 생성 (`output/YYYYMMDD_{keyword}/research/`)
2.  **리서치 설계**: `.agent/skills/strategy-framer/prompts/1_research_design.md` 실행
    - 결과: Research Blueprint -> **저장**: `01_research_blueprint.md`
3.  **리서치 실행 (Util 호출)**: `util-research-runner` 스킬을 사용하여 리서치 수행
    - 참조: `.agent/skills/util-research-runner/SKILL.md`
    - 결과: Research Report & Logs -> **저장**: `research/01_Phase1_Research_Report.md`
4.  **맥락 종합**: `.agent/skills/strategy-framer/prompts/2_context_synthesis.md` 실행
    - 결과: Context Insight -> **저장**: `03_context_insight.md`
5.  **문제 정의**: `.agent/skills/strategy-framer/prompts/3_scr_context.md` 실행
    - 결과: SCR Problem Statement -> **저장**: `04_scr_problem.md`
6.  **구조화**: `.agent/skills/strategy-framer/prompts/4_issue_tree.md` 실행
    - 결과: Issue Tree -> **저장**: `05_issue_tree.md`
7.  **가설 수립**: `.agent/skills/strategy-framer/prompts/5_ghost_draft.md` 실행
    - 결과: **저장**: `06_ghost_deck_v1.md`
8.  **Content Expander (Conditional)**:
    - **품질 검증**: `06_ghost_deck_v1.md` 분량 확인
    - **실행 조건**: 120줄(목표 80줄의 150%) 미만일 경우에만 실행
    - **실행**: `.agent/skills/util-workflow-engineer/prompts/content_expander.md`
    - **기준 충족 시**: ⏭️ 생략하고 다음 단계로 (충분히 깊이 있음)
9.  **📋 Task Progress Update (Mandatory)**: `task.md` 파일을 열어 Phase 1에서 완료한 모든 항목의 체크박스를 `[ ]` → `[✅]`로 변경하고, Phase 1 헤더를 `[ ]` → `[✅ Done]`으로 업데이트하십시오.
10. **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 사용하여 단계 기록
