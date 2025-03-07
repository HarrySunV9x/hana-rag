import requests
import json

from rag import rag

url = "http://localhost:11434/api/generate"


def llm_invoke(prompt_string):
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt_string,
        "stream": True
    }

    response = requests.post(url, json=payload)
    # 手动解析返回的多行 JSON 数据
    results = ""
    for line in response.text.splitlines():
        try:
            json_obj = json.loads(line)
            results += json_obj["response"]
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON response", "invalid_line": line}
    print(results)


if __name__ == '__main__':
    rag()