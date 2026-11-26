# andresdelcampo/GPTYourData

⭐ 12 · C# · MIT · 推送 2026-11-23 · [GitHub](https://github.com/andresdelcampo/GPTYourData) · 个人维护

**面向本地文件问答的 C# 向量搜索引擎，基于 OpenAI 生成嵌入**

用 C# 实现的向量搜索工具：将本地文本或 PDF 文件转为嵌入并存入本地 Embeddings 目录，再基于这些嵌入回答问题。提供命令行工具（pdf2txt/Embed/Query）和网页界面两种方式，网页界面支持上传文件并自动执行嵌入流程。运行需要 .NET 7 与有效的 OpenAI API Key，密钥写入项目根目录的 '.openai' 文件。嵌入只需生成一次，之后 Query 工具基于已有嵌入返回相关答案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地 txt/PDF 文件并生成嵌入，构建本地向量数据库
- 提供 pdf2txt 工具将 PDF 转为文本
- 命令行（Query）与网页（QueryWeb, localhost:5000）两种查询方式
- 网页界面支持上传新文件并自动执行嵌入，扩展知识库

## 适用场景

- 对本地文档库提问并获取基于嵌入检索的答案
- 通过网页上传文件持续扩展可查询的知识库
- 部署到局域网地址供外部访问查询

## 场景标签

`RAG` `语义搜索` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L2: Welcome to GPTYourData! This project is a simple but fast and effective C# vector search engine that utilizes OpenAI
> L19: * Put all the text or PDF files you want to query in the Inputs folder.

## 星数曲线

```mermaid
xychart-beta
    title "andresdelcampo/GPTYourData 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-11-25 12 → 2026-11-26 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `e8014ad6a0fb` · [字段定义](../../DATASET.md)*
