# mongodb-developer/mongodb-vector-search-rag

⭐ 32 · Python · 推送 2026-04-24 · [GitHub](https://github.com/mongodb-developer/mongodb-vector-search-rag) · 组织维护

**用 MongoDB Vector Search + RAG 构建问答应用的 Python 脚本集**

提供两个 Python 脚本：load_data.py 用 DirectoryLoader 读取目录文档，经 OpenAI text-embedding-ada-002 生成向量嵌入并存入 MongoDB 集合；extract_information.py 用 Gradio 生成界面，通过 MongoDB Vector Search 做 KNN 检索、以 LangChain RetrievalQA 链和 gpt-3.5-turbo 对数据做问答。面向使用 MongoDB Atlas 的开发者，需付费 OpenAI API key 与 MongoDB URI，以 pip 安装依赖、git clone 源码方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档目录批量加载并生成 1536 维向量嵌入存入 MongoDB
- MongoDBVectorSearch 封装 KNN 向量检索
- Gradio 生成问答用户界面
- LangChain RetrievalQA 问答链

## 适用场景

- 把本地文档做成可问答的知识库
- 体验 MongoDB Vector Search 的 RAG 检索问答流程
- 作为 Atlas 向量搜索 + LangChain 的参考示例工程

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: The Python scripts in this repo use MongoDB Vector Search with Retrieval-Augmented Generation (RAG) architecture to 
> L19:  - **load_data.py**: This script will be used to load your documents and ingest the text and vector embeddings, in 
> L20:  - **extract_information.py**: This script will generate the user interface and will allow you to perform question-

## 星数曲线

```mermaid
xychart-beta
    title "mongodb-developer/mongodb-vector-search-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `be8f5463c74d` · [字段定义](../../DATASET.md)*
