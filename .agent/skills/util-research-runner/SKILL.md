---
name: util-research-runner
description: 범용 리서치 수행 스킬입니다. Blueprint를 입력받아 Perplexity로 검색하고 보고서를 작성합니다.
tools: [perplexity_ask, write_file]
---

# Research Runner (Utility)

## Role

프로젝트 전반에 걸쳐 리서치를 전담 수행하며, 모든 Perplexity 검색 과정을 자동으로 로깅합니다.

## Usage

다른 스킬에서 이 스킬을 호출할 때 다음을 입력으로 받습니다.

- **Blueprint**: 조사할 질문 리스트와 검색 의도
- **Output Folder**: 프로젝트 출력 폴더 경로
- **Phase Name**: 현재 Phase (예: Phase1, Phase2)

## Workflow (Simplified with Auto-Logging)

1.  **Read Blueprint**: 입력된 청사진 확인
2.  **Execute Research with Auto-Logging**:
    - **프롬프트 실행**: `prompts/research_with_logging.md`
    - **자동 수행 내용**:
      - Perplexity 검색 (영문 쿼리, 한글 응답)
      - `perplexity/` 폴더 자동 생성
      - 각 Item별 요청/응답 자동 로깅
    - **출력**: `perplexity/{Phase}_Item*_request.md`, `perplexity/{Phase}_Item*_response.md`
3.  **Report**: 검색 결과를 구조화하여 지정된 경로에 저장
4.  **Validation (Quality Gate)**: `prompts/output_validator.md` 실행
    - **Pass condition**: "Search Log Table" 및 "URL Sources" 포함 여부 확인
    - **If Fail**: 즉시 Step 3(Report)를 재수행하여 보고서 포맷을 수정 (User 승인 불필요)

## Key Improvement

**Before**: 수동 스크립트 실행 필요 (log_mcp.py)  
**After**: 프롬프트가 자동으로 로깅 수행 ✅

이제 별도의 로깅 단계나 스크립트 실행 없이, `research_with_logging.md` 프롬프트만 실행하면 모든 리서치와 로깅이 자동으로 완료됩니다.
