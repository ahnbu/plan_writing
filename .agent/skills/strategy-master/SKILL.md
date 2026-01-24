---
name: strategy-master
description: MBB 스타일 전략 수립 전체 프로세스(Orchestrator)를 총괄 및 관리합니다.
tools: [read_file, write_file, view_file]
---

# Strategy Master (Orchestrator)

이 스킬은 전략 수립 프로젝트의 **총괄 PM(Project Manager)** 역할을 수행합니다.
직접 세부 작업을 수행하기보다, 각 단계별 **전문가 스킬(Specialist Skills)**을 호출하고 그 결과물을 검수하여 전체 프로젝트의 일관성을 유지합니다.

## Workflow Overview

1.  **Phase 0: 정의 (Definition)** - 목표 설정 및 성공 기준(DoD) 수립 (TDD Setup)
2.  **Phase 1: 구조화 (Framer)** - 문제 정의 및 가설 수립
3.  **Phase 2: 검증 (Hunter)** - 가설 검증 및 팩트 체크
4.  **Phase 3: 방어 (Red Teamer)** - 약점 분석 및 전략 보강
5.  **Phase 4: 시각화 (PT Planner)** - 슬라이드 기획 및 PPT 생성

---

## Phase 0: 정의 (Project Definition)

**목표**: 프로젝트의 성공 기준(Test Cases)을 미리 정의하여 TDD 방식으로 진행합니다.

1.  **스킬 실행**: `prompts/0_project_init.md` 실행
    - 입력: 사용자 요구사항 (User Request)
    - 결과: **저장**: `00_project_charter.md`
2.  **📜 기록 보관**: `util-history-keeper` 스킬 실행 (Initial Log)
    - **Target File**: `00_project_charter.md`

## Phase 1: 구조화 (The Framer)

**목표**: 모호한 문제를 구조화하고 초기 가설(Ghost Deck)을 수립합니다.

1.  **스킬 호출**: `strategy-framer` 스킬을 로드하여 실행하십시오.
    - 명령: `.agent/skills/strategy-framer/SKILL.md` 참조
2.  **검수 포인트 (QA)**:
    - `orchestrator_qa.md`와 `00_project_charter.md`를 대조하여 평가하십시오.
    - Target: `04_scr_problem.md`, `06_ghost_deck_v1.md`

## Phase 2: 검증 (The Hunter)

**목표**: 수립된 가설을 시장 데이터와 팩트로 검증합니다.

1.  **스킬 호출**: `strategy-hunter` 스킬을 로드하여 실행하십시오.
    - 명령: `.agent/skills/strategy-hunter/SKILL.md` 참조
2.  **검수 포인트 (QA)**:
    - `orchestrator_qa.md`와 `00_project_charter.md`를 대조하여 평가하십시오.
    - Target: `09_verified_facts.md`, `10_ghost_deck_v2.md`

## Phase 3: 방어 및 연마 (The Red Teamer)

**목표**: 비판적 시각(Red Team)으로 약점을 보완하고 최종 보고서를 완성합니다.

1.  **스킬 호출**: `strategy-redteamer` 스킬을 로드하여 실행하십시오.
    - 명령: `.agent/skills/strategy-redteamer/SKILL.md` 참조
2.  **검수 포인트 (QA)**:
    - `orchestrator_qa.md`와 `00_project_charter.md`를 대조하여 평가하십시오.
    - Target: `11_red_team_risks.md`, `15_FINAL_REPORT.md`

## Phase 4: 시각화 및 제작 (The PT Planner)

**목표**: 최종 보고서를 설득력 있는 PPT로 변환합니다.

1.  **스킬 호출**: `strategy-pt-planner` 스킬을 로드하여 실행하십시오.
    - 명령: `.agent/skills/strategy-pt-planner/SKILL.md` 참조
2.  **검수 포인트 (QA)**:
    - `orchestrator_qa.md`와 `00_project_charter.md`를 대조하여 평가하십시오.
    - Target: `17_slide_plan.md`, `18_Strategy_Deck.pptx`
