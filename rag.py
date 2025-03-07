from glob import glob
import chromadb

def rag(query_text):
    # 初始化部分（每次调用都重新加载数据，仅示例用）
    text_lines = []
    ids = []
    id = 1
    for file_path in glob("note/*.md", recursive=True):
        with open(file_path, "r", encoding="utf-8") as file:
            file_text = file.read()
        text_lines += file_text.split("# ")  # 按标题分割内容

    # 生成唯一ID
    for i in range(len(text_lines)):
        ids.append(f"id{id}")
        id += 1

    # 创建Chroma集合并添加文档
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")
    collection.add(documents=text_lines, ids=ids)

    # 执行查询
    results = collection.query(
        query_texts=[query_text],  # 使用传入的查询文本
        n_results=2
    )
    return results

