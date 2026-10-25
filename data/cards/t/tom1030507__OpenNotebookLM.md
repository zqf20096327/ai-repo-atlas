# tom1030507/OpenNotebookLM

⭐ 68 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/tom1030507/OpenNotebookLM) · 个人维护

**自托管的 NotebookLM 替代：导入文档问答并带引用溯源**

基于 FastAPI + Next.js 的自托管文档问答应用，定位为 Google NotebookLM 的替代：导入 PDF/txt/md、网页与 YouTube 字幕，抽取为 Markdown 并按标题结构分块，嵌入与对话数据存于本地 SQLite。检索为 sqlite-vec 稠密候选与 FTS5/BM25 关键词候选经倒数排名融合，词法端含 CJK 字符二元组支持中文检索。回答附带指向文档与章节路径的引用；LLM 可接 Claude、任意 OpenAI 兼容服务或本地 Ollama/llama.cpp/vLLM，未配置时退化为抽取式回答。支持多账户隔离与 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- sqlite-vec 稠密检索与 FTS5/BM25 关键词检索的倒数排名融合，BM25 分词含 CJK 字符二元组
- 回答逐块引用来源文档与章节路径
- 可接 Claude、OpenAI 兼容服务或本地 Ollama/llama.cpp/vLLM，未配置 LLM 时返回抽取式回答
- 文档、嵌入与对话存储在本地 SQLite，含多账户项目隔离

## 适用场景

- 私有化部署一套针对自己文档的问答系统并核验引用出处
- 本地/离线环境（Ollama）下对 PDF 和网页做带引用的问答
- 按项目组织资料并生成报告、音频摘要、概念图等产出

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5:  A self-hosted alternative to Google's NotebookLM.
> L6:  Import your documents, ask questions about them, and get answers with citations
> L35: |🔌|**Any LLM, or none**|Claude, OpenAI, anything speaking the OpenAI chat-completions API (Groq, OpenRouter, DeepSe

## 星数曲线

```mermaid
xychart-beta
    title "tom1030507/OpenNotebookLM 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-25"]
    y-axis "stars" 65 --> 69
    line [66, 67, 68, 68]
```

2026-10-18 66 → 2026-10-25 68（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3b05e63e9e0e` · [字段定义](../../DATASET.md)*
