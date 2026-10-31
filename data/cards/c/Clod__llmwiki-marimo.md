# Clod/llmwiki-marimo

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Clod/llmwiki-marimo) · 个人维护

**本地优先的个人 LLM 维基：把文档编成可阅读可对话的知识库**

面向个人用户的本地维基应用：导入 PDF/Office/Markdown/纯文本，经抽取、分块、结构化概念提取生成相互链接的 Markdown 页面，形成持久化知识库，并提供带引用的对话（Wiki-first RAG：先读策展页面再回退原始分块）。内置 Agent、FastAPI+HTMX 网页界面、SQLite/FTS5 检索、每维基独立 git 仓库与历史回滚。支持任意 OpenAI 兼容端点，可拆分聊天/导入模型。附带阿根廷个人理财示例：结构化数据集可精确查询，收益计算用确定性代码完成。限制：非 Obsidian 插件，无插件生态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cite-or-refuse 落地校验：答案无工具结果支撑即替换为拒答（预检索/严格/无验证三模式）
- Wiki-first RAG：先读已编纂的策展页面，仅在需要时回退原始分块
- 域中立 datasets 引擎：结构化数据带 as_of 日期精确查询，数值计算用确定性代码而非 LLM
- 12 项 lint 自检（矛盾/过时/孤儿页等）与安全项自动修复

## 适用场景

- 把个人文档编成可长期积累、可追溯引用的知识库
- 与本地知识库对话并获得逐条引用和日期来源的回答
- 在理财等场景基于可刷新数据获得确定性计算建议

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L12: A personal, local-first wiki that ingests your documents, builds a structured knowledge base, and lets you read and
> L39: This one ships its own embedded agent: ingestion, agentic retrieval (the chat
> L111: 1. **Ingest** — in the **Ingest** tab, choose PDF, office (`.docx`, `.doc`, `.odt`, `.rtf`), Markdown (`.md`) or p

## 星数曲线

```mermaid
xychart-beta
    title "Clod/llmwiki-marimo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bf35c1f22af5` · [字段定义](../../DATASET.md)*
