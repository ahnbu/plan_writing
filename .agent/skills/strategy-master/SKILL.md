---
name: strategy-master
description: MBB 스타일 전략 수립 전체 프로세스(Orchestrator)를 총괄 및 관리합니다.
tools: [read_file, write_file, view_file]
---

# Strategy Master (Orchestrator)

이 스킬은 전략 수립 프로젝트의 **총괄 PM(Project Manager)** 역할을 수행합니다.
직접 세부 작업을 수행하기보다, 각 단계별 **전문가 스킬(Specialist Skills)**을 호출하고 그 결과물을 검수하여 전체 프로젝트의 일관성을 유지합니다.

## Workflow Overview

1.  **Phase 0: 정의 (Definition)**
    - **Session Setup**: `output/YYYYMMDD_HHMM_{Keyword}` 형식의 고유 폴더 생성 (필수)
    - **Task Tracking**: 프로젝트 시작 시 `task.md`를 생성하여 전체 할 일 목록을 관리합니다.
    - **Goal Setting**: 목표 설정 및 성공 기준(DoD) 수립 (TDD Setup)
2.  **Phase 1: 구조화 (Framer)** - 문제 정의 및 가설 수립
3.  **Phase 2: 검증 (Hunter)** - 가설 검증 및 팩트 체크
4.  **Phase 3: 방어 (Red Teamer)** - 약점 분석 및 전략 보강
5.  **Phase 4: 시각화 (PT Planner)** - 슬라이드 기획 및 PPT 생성

---

## Phase 0: 정의 (Project Definition)

**목표**: 프로젝트의 성공 기준(Test Cases)을 미리 정의하고 작업 관리 체계를 수립합니다.

1.  **System Time Verification**: 모든 분석 및 리서치의 기준이 되는 **현재 시계열(System Metadata)**을 확인하고 기록하십시오.
2.  **Task Management**: `.agent/skills/strategy-master/prompts/task_template.md`를 사용하여 프로젝트 폴더 내에 `task.md`를 생성하십시오. 이 파일은 모든 페이즈별 단계, 리서치 결과 저장, **History Keeper**, **Workflow Audit** 체크리스트를 포함하며 프로젝트 진행의 핵심 기준이 됩니다.
3.  **스킬 실행**: `prompts/0_project_init.md` 실행
    - 결과: **저장**: `00_project_charter.md`
4.  **📜 기록 보관 (Mandatory)**: `util-history-keeper` 스킬 실행.
5.  **🔍 진단 (Mandatory)**: `util-workflow-engineer` 실행 (`workflow_health.md`).

## Phase 1: 구조화 (The Framer)

**목표**: 모호한 문제를 구조화하고 초기 가설(Ghost Deck)을 수립합니다.

1.  **리서치 및 저장**: `strategy-framer`를 통해 리서치를 수행하고 결과물을 `research/` 폴더에 명시적으로 저장하십시오. (`task.md` 업데이트)
2.  **스킬 호출**: `strategy-framer` 실행하여 문제 정의 및 가설 수립.
3.  **심층 보강 (Deep-Dive Expansion)**: `content_expander.md`를 사용하여 논리 깊이 확장.
4.  **📜 기록 보관 (Mandatory)**: `util-history-keeper` 스킬 실행.
5.  **🔍 진단 (Mandatory)**: `util-workflow-engineer` 실행 (`workflow_health.md`).

## Phase 2: 검증 (The Hunter)

**목표**: 수립된 가설을 시장 데이터와 팩트로 검증합니다.

1.  **검증 리서치 및 저장**: `strategy-hunter`를 통해 검증 리서치를 수행하고 결과물을 `research/` 폴더에 저장하십시오. (`task.md` 업데이트)
2.  **스킬 호출**: `strategy-hunter` 실행하여 가설 검증 및 팩트 체크.
3.  **심층 보강 (Deep-Dive Expansion)**: 리서치 팩트가 녹아든 `10_ghost_deck_v2.md` 보강.
4.  **📜 기록 보관 (Mandatory)**: `util-history-keeper` 스킬 실행.
5.  **🔍 진단 (Mandatory)**: `util-workflow-engineer` 실행 (`workflow_health.md`).

## Phase 3: 방어 및 연마 (The Red Teamer)

**목표**: 비판적 시각(Red Team)으로 약점을 보완하고 최종 보고서를 완성합니다.

1.  **스킬 호출**: `strategy-redteamer` 스킬을 실행하십시오.
2.  **📜 기록 보관 (Mandatory)**: `util-history-keeper` 스킬 실행.
3.  **🔍 진단 (Mandatory)**: `util-workflow-engineer` 실행 (`workflow_health.md`).

## Phase 4: 시각화 및 제작 (The PT Planner)

**목표**: 최종 보고서를 설득력 있는 PPT로 변환합니다.

1.  **스킬 호출**: `strategy-pt-planner` 스킬을 실행하십시오.
2.  **📜 기록 보관 (Mandatory)**: `util-history-keeper` 스킬 실행.
3.  **🔍 진단 (Mandatory)**: `util-workflow-engineer` 실행 (`workflow_health.md`).
