# skhalidmahmud/RAG-Knowledge-Engine

⭐ 19 · MIT · 推送 2026-05-07 · [GitHub](https://github.com/skhalidmahmud/RAG-Knowledge-Engine) · 个人维护

**基于私有文档的 RAG 问答系统，减少无据回答**

一个检索增强生成（RAG）应用：用户上传 PDF 或文本文件，系统读取并向量化存储到 ChromaDB；提问时先在文档中检索相关内容，再由 LLM 基于检索结果生成回答，以此减少凭空猜测。技术栈为 OpenAI GPT-4o 作为 LLM、LangChain 构建 AI 逻辑、ChromaDB 作为向量存储。README 仅描述原理与技术栈，未给出安装或运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持上传 PDF 与文本文件作为知识来源
- 提问前先检索文档再生成回答
- 技术栈：OpenAI GPT-4o + LangChain + ChromaDB

## 适用场景

- 我需要让 AI 基于自己的文档回答问题
- 快速检索大型文档中的具体内容

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AI is great, but it often makes things up (hallucinations). I built this "Knowledge Engine" to make AI more reliable
> L6: You can upload PDFs or text files, and the system "reads" them. When you ask a question, the AI searches your docume

## 星数曲线

```mermaid
xychart-beta
    title "skhalidmahmud/RAG-Knowledge-Engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8ccb08f66c65` · [字段定义](../../DATASET.md)*
