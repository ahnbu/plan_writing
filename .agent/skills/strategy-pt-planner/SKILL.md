---
name: strategy-pt-planner
description: 전략 수립 4단계(시각화)를 수행합니다. 내러티브 설계, 슬라이드 기획, PPTX 파일 생성 및 검증(Audit).
tools: [read_file, write_file, run_command]
---

# Phase 4: The PT Planner (시각화 및 제작)

**목표**: 최종 보고서를 설득력 있는 PPT 슬라이드 설계도로 변환하고 실제 파일로 제작하며, 무결성을 자동 검증합니다.

## Workflow

1.  **내러티브 설계**: `.agent/skills/strategy-pt-planner/prompts/1_narrative_design.md` 실행
    - 결과: Storyline -> **저장**: `16_storyline.md`
2.  **슬라이드 상세 설계**: `.agent/skills/strategy-pt-planner/prompts/2_slide_plan.md` 실행
    - 결과: Slide-by-Slide Plan -> **저장**: `17_slide_plan.md`
3.  **PPTX 파일 생성**:
    - 스크립트 실행: `.agent/skills/strategy-pt-planner/scripts/generate_pptx_v2.py`
    - 사용법: `python scripts/generate_pptx_v2.py --input "path/to/plan.md" --output "path/to/deck.pptx"`
4.  **PPT Audit (무결성 검증)**:
    - 스크립트 실행: `.agent/skills/strategy-pt-planner/scripts/audit_pptx.py`
    - 사용법: `python scripts/audit_pptx.py --pptx_path "path/to/deck.pptx" --plan_path "path/to/plan.md"`
    - **목적**: 생성된 파일의 슬라이드 개수가 기획안과 일치하는지, 내용이 비어있지 않은지 검사하여 오류 시 재작업 플래그를 띄웁니다.

5.  **📋 Task Progress Update (Mandatory)**: `task.md` 파일을 열어 Phase 4에서 완료한 모든 항목의 체크박스를 `[ ]` → `[✅]`로 변경하고, Phase 4 헤더를 `[ ]` → `[✅ Done]`으로 업데이트하십시오.
6.  **📜 기록 보관 (Util 호출)**: `util-history-keeper` 스킬 사용하여 단계 기록
