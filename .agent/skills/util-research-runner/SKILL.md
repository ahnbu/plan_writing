---
name: util-research-runner
description: 범용 리서치 수행 스킬입니다. Blueprint를 입력받아 Perplexity로 검색하고 보고서를 작성합니다.
tools: [perplexity_ask, write_file]
---

# Research Runner (Utility)

## Role

프로젝트 전반에 걸쳐 리서치를 전담 수행합니다.

## Usage

다른 스킬에서 이 스킬을 호출할 때 다음을 입력으로 받습니다.

- **Blueprint**: 조사할 질문 리스트와 검색 의도

## Workflow

1.  **Read Blueprint**: 입력된 청사진 확인
2.  **Execute Search**: `perplexity_ask` 툴을 사용하십시오.
    - **Language Protocol (Mandatory)**:
      - 쿼리(Query)는 고해상도 정보 확보를 위해 **영문(English)**으로 작성하십시오.
      - 응답 요청 시 반드시 **"Respond in Korean"** 지시어를 추가하여 로그의 가독성을 확보하십시오.
    - **Fragmented Search Policy (Mandatory)**:
      - 여러 주제가 섞인 일괄 검색(Batch Search)을 엄격히 금지합니다.
      - 청사진(`blueprint`)의 각 조사 항목별로 최소 1회 이상의 독립적인 `perplexity_ask` 호출을 수행하십시오.
    - **Raw Logging Protocol (Mandatory)**:
      1. 도구 응답 원문을 프로젝트 출력 폴더 내 임시 파일(`{output_path}/temp/raw_res.txt`)에 저장하십시오.
      2. `scripts/log_mcp.py`를 실행하여 원문을 `{output_path}/perplexity/` 폴더에 아카이빙하십시오.
      3. **절대 AI가 응답을 요약하거나 편집하여 로그 파일에 직접 쓰지 마십시오.**
3.  **Report**: 검색 결과를 구조화하여 지정된 경로에 저장하십시오.
4.  **Validation (Quality Gate)**: `prompts/output_validator.md` 실행
    - **Pass condition**: "Search Log Table" 및 "URL Sources" 포함 여부 확인
    - **If Fail**: 즉시 Step 3(Report)를 재수행하여 보고서 포맷을 수정 (User 승인 불필요)
