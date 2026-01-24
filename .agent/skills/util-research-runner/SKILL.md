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
2.  **Execute Search**: `perplexity_ask` 툴을 사용하여 심층 검색 수행
    - **Prompt**: `.agent/skills/util-research-runner/prompts/research_runner.md` (Role definition 역할)
3.  **Report**: 검색 결과를 구조화하여 지정된 경로에 저장
