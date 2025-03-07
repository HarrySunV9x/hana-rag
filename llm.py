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
    while True:
        # 获取用户输入
        user_input = input("\n请输入您的问题（输入q退出）: ")

        if user_input.lower() == 'q':
            print("退出查询")
            break

        # 执行RAG查询
        print("\n正在检索相关知识...")
        rag_results = rag(user_input)

        # 构造提示词
        context = "\n".join(rag_results['documents'][0])
        prompt = f"""基于以下上下文给出专业回答，从我给的上下文之中寻找：
    {context}

    问题：{user_input}
    答案："""

        # 调用LLM生成
        print("\n生成回答中...")
        llm_invoke(prompt)