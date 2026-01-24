# {ProjectName} 작업 목록

## Phase 0: 정의 (Project Definition) [ ]

- [ ] **System Setup**: System Time Verification 및 세션 폴더 생성
      : (활용도구) `strategy-master`
- [ ] **Project Init**: Project Charter 작성
      : (활용도구) `strategy-master/prompts/0_project_init.md`, (산출물) `00_project_charter.md` (최소 50줄 이상)
- [ ] **Task Tracking**: `task.md` 생성 및 초기화
      : (활용도구) `strategy-master`, (산출물) `task.md` (Template: `.agent/skills/strategy-master/prompts/task_template.md`)
- [ ] **History Keeper**: 초기 이력 기록 완료
      : (활용도구) `util-history-keeper`, (산출물) `history.md`
- [ ] **Workflow Audit**: 초기 진단 수행
      : (활용도구) `util-workflow-engineer`, (산출물) `workflow_health.md`

## Phase 1: 구조화 (The Framer) [ ]

- [ ] **Research Design**: 리서치 블루프린트 작성
      : (활용도구) `strategy-framer/prompts/1_research_design.md`, (산출물) `01_research_blueprint.md` (최소 40줄 이상)
- [ ] **Research (Execution)**: 시장 현황 리서치 수행
      : (활용도구) `util-research-runner`
- [ ] **Research (Log)**: Perplexity 세부 요청 및 응답 결과 저장
      : (활용도구) `util-research-runner`, `.agent/skills/util-research-runner/scripts/log_mcp.py`, (산출물) `perplexity/01_Phase1_Search_Log.md`
- [ ] **Research (Validation)**: 리서치 결과물 품질 및 분량 검증
      : (활용도구) `.agent/skills/util-research-runner/prompts/output_validator.md`
- [ ] **Research (Storage)**: 리서치 결과물 저장
      : (활용도구) `strategy-master`, (산출물) `02_market_research_report.md` (최소 100줄 이상)
- [ ] **Synthesis**: 맥락 종합 및 인사이트 도출
      : (활용도구) `strategy-framer/prompts/2_context_synthesis.md`, (산출물) `03_context_insight.md` (최소 40줄 이상)
- [ ] **Problem Definition**: 문제 구조화 (SCR) 수행
      : (활용도구) `strategy-framer/prompts/3_scr_context.md`, (산출물) `04_scr_problem.md` (최소 50줄 이상)
- [ ] **Issue Tree**: 이슈 트리(Issue Tree) 작성
      : (활용도구) `strategy-framer/prompts/4_issue_tree.md`, (산출물) `05_issue_tree.md` (최소 60줄 이상)
- [ ] **Ghost Deck v1**: 초기 가설 수립
      : (활용도구) `strategy-framer/prompts/5_ghost_draft.md`, (산출물) `06_ghost_deck_v1.md` (최소 80줄 이상)
- [ ] **Content Expander**: 내러티브 확장 및 논리 보강
      : (활용도구) `util-workflow-engineer/prompts/content_expander.md` (논리 깊이 3배 확장)
- [ ] **History Keeper**: 1단계 이력 기록
      : (활용도구) `util-history-keeper`, (산출물) `history.md`
- [ ] **Workflow Audit**: 1단계 진단 수행
      : (활용도구) `util-workflow-engineer`, (산출물) `workflow_health.md`

## Phase 2: 검증 (The Hunter) [ ]

- [ ] **Verify Design**: 검증 리서치 계획 수립
      : (활용도구) `strategy-hunter/prompts/1_meta_plan.md`, (산출물) `07_verification_plan.md` (최소 40줄 이상)
- [ ] **Research (Execution)**: 가설 검증 심층 리서치 수행
      : (활용도구) `util-research-runner`
- [ ] **Research (Log)**: Perplexity 세부 요청 및 응답 결과 저장
      : (활용도구) `util-research-runner`, `.agent/skills/util-research-runner/scripts/log_mcp.py`, (산출물) `perplexity/Phase2_Item*_request.md`, `perplexity/Phase2_Item*_response.md` (총 3개 세트)
- [ ] **Research (Validation)**: 리서치 결과물 품질 및 분량 검증
      : (활용도구) `.agent/skills/util-research-runner/prompts/output_validator.md`
- [ ] **Research (Storage)**: 리서치 결과물 저장
      : (활용도구) `strategy-master`, (산출물) `08_verification_research_log.md` (최소 100줄 이상)
- [ ] **Fact Check**: 팩트 체크 및 데이터 검증 결과 정리
      : (활용도구) `strategy-hunter/prompts/2_fact_check.md`, (산출물) `09_verified_facts.md` (최소 50줄 이상)
- [ ] **Ghost Deck v2**: 가설 수정 및 전략 종합
      : (활용도구) `strategy-hunter/prompts/3_synthesis.md`, (산출물) `10_ghost_deck_v2.md` (최소 120줄 이상)
- [ ] **Content Expander**: 리서치 팩트 기반 내러티브 보강
      : (활용도구) `util-workflow-engineer/prompts/content_expander.md` (데이터 밀도 3배 보강)
- [ ] **History Keeper**: 2단계 이력 기록
      : (활용도구) `util-history-keeper`, (산출물) `history.md`
- [ ] **Workflow Audit**: 2단계 진단 수행
      : (활용도구) `util-workflow-engineer`, (산출물) `workflow_health.md`

## Phase 3: 방어 및 연마 (The Red Teamer) [ ]

- [ ] **Red Teaming (Attack)**: 비판적 리뷰 및 취약점 타격
      : (활용도구) `strategy-redteamer/prompts/1_red_team_critic.md`, (산출물) `11_debate_round1_attack.md` (최소 60줄 이상)
- [ ] **Debate Round 1 (Defense)**: 블루팀 방어 논리 수립
      : (활용도구) `strategy-redteamer/prompts/2_blue_team_insight.md`, (산출물) `12_debate_round1_defense.md` (최소 60줄 이상)
- [ ] **Debate Round 2 (Counter-Attack)**: 레드팀 재반박
      : (활용도구) `strategy-redteamer/prompts/2a_red_team_rebuttal.md`, (산출물) `13_debate_round2_rebuttal.md` (최소 60줄 이상)
- [ ] **Debate Round 2 (Evolution)**: 전략 수정 및 보강
      : (활용도구) `strategy-redteamer/prompts/2b_blue_team_evolution.md`, (산출물) `14_debate_round2_evolution.md` (최소 80줄 이상)
- [ ] **Final Synthesis**: 논쟁 통합 및 최종 대안 도출
      : (활용도구) `strategy-redteamer/prompts/3_defense_logic.md`, (산출물) `14_debate_round3_synthesis.md` (최소 100줄 이상)
- [ ] **Final Report**: 최종 전략 보고서 작성
      : (활용도구) `strategy-redteamer/prompts/4_final_polish.md`, (산출물) `15_FINAL_REPORT.md` (최소 200줄 이상)
- [ ] **Content Expander**: 최종 보고서 심층 보강 (Deep-Dive)
      : (활용도구) `util-workflow-engineer/prompts/content_expander.md`, (산출물) `15_FINAL_REPORT_expanded.md` (논리 깊이 3배 확장)
- [ ] **History Keeper**: 3단계 이력 기록
      : (활용도구) `util-history-keeper`, (산출물) `history.md`
- [ ] **Workflow Audit**: 3단계 진단 수행
      : (활용도구) `util-workflow-engineer`, (산출물) `workflow_health.md`

## Phase 4: 시각화 및 제작 (The PT Planner) [ ]

- [ ] **Narrative Design**: 내러티브 설계 및 스토리라인 확정
      : (활용도구) `strategy-pt-planner/prompts/1_narrative_design.md`, (산출물) `16_storyline.md` (최소 50줄 이상)
- [ ] **Slide Planning**: 슬라이드 기획안 작성
      : (활용도구) `strategy-pt-planner`, (산출물) `17_slide_plan.md` (최소 150줄 이상)
- [ ] **PPT Creation**: PPTX 파일 생성
      : (활용도구) `strategy-pt-planner`, `.agent/skills/strategy-pt-planner/scripts/generate_pptx_v2.py`, (산출물) `18_Strategy_Deck.pptx`
- [ ] **PPT Audit**: 생성된 파일 무결성 및 장수 검증
      : (활용도구) `util-ppt-auditor`, `.agent/skills/util-ppt-auditor/scripts/audit_pptx.py`
- [ ] **History Keeper**: 4단계 이력 기록
      : (활용도구) `util-history-keeper`, (산출물) `history.md`
- [ ] **Workflow Audit**: 4단계 진단 수행
      : (활용도구) `util-workflow-engineer`, (산출물) `workflow_health.md`
