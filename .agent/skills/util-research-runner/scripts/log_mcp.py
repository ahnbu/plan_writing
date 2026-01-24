import json
import os
import sys
import argparse

def save_mcp_log(folder, phase_name, request_text, response_text):
    """
    요청과 응답의 원문을 가공 없이 JSON 및 Markdown 형식으로 저장합니다.
    출력 경로는 반드시 프로젝트별 전용 폴더(output/.../perplexity)를 사용합니다.
    """
    os.makedirs(folder, exist_ok=True)
    
    # 1. JSON 로그 저장 (시스템 아카이브용)
    log_data = {
        "metadata": {
            "phase": phase_name,
            "engine": "perplexity-ask",
            "log_format": "v2.0 (fragmented)"
        },
        "request": request_text,
        "response": response_text
    }
    
    json_path = os.path.join(folder, f"{phase_name}_full_log.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
        
    # 2. Markdown 요청 저장 (감사용)
    req_md_path = os.path.join(folder, f"{phase_name}_request.md")
    with open(req_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Research Request: {phase_name}\n\n")
        f.write(request_text)
        
    # 3. Markdown 응답 저장 (사용자 가독성용)
    res_md_path = os.path.join(folder, f"{phase_name}_response.md")
    with open(res_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Research Response: {phase_name}\n\n")
        f.write(response_text)
    
    print(f"✅ Success: Logs archived in {folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True)
    parser.add_argument("--phase", required=True)
    parser.add_argument("--request_file", required=True)
    parser.add_argument("--response_file", required=True)
    
    args = parser.parse_args()
    
    try:
        with open(args.request_file, 'r', encoding='utf-8') as f:
            req = f.read()
        with open(args.response_file, 'r', encoding='utf-8') as f:
            res = f.read()
        save_mcp_log(args.folder, args.phase, req, res)
    except FileNotFoundError as e:
        print(f"❌ Error: Log source file missing - {e}")
        sys.exit(1)
