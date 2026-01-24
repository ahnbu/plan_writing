---
name: strategy-pt-planner
description: 전략 수립 4단계(시각화)를 수행합니다. 내러티브 설계, 슬라이드 기획, PPTX 파일 생성.
tools: [read_file, write_file, run_command]
---

# Phase 4: The PT Planner (시각화 및 제작)

**목표**: 최종 보고서를 설득력 있는 PPT 슬라이드 설계도로 변환하고 실제 파일로 제작합니다.

## Workflow

1.  **내러티브 설계**: `.agent/skills/strategy-pt-planner/prompts/1_narrative_design.md` 실행
    - 결과: Storyline -> **저장**: `16_storyline.md`
2.  **슬라이드 상세 설계**: `.agent/skills/strategy-pt-planner/prompts/2_slide_plan.md` 실행
    - 결과: Slide-by-Slide Plan -> **저장**: `17_slide_plan.md`
3.  **PPTX 파일 생성**:
    - 스크립트 실행: `.agent/skills/strategy-pt-planner/scripts/generate_pptx_strategy.py`
    - **주의**: 스크립트 내부에 입력 파일 경로(`17_slide_plan.md`)가 올바르게 설정되어 있는지 확인해야 합니다. 필요 시 인자로 경로를 전달하도록 스크립트를 수정하거나 실행 시 경로를 확인하십시오.
4.  **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 사용하여 단계 기록
