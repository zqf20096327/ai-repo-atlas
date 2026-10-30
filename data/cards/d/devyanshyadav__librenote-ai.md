# devyanshyadav/librenote-ai

⭐ 18 · TypeScript · MIT · 推送 2026-08-23 · [GitHub](https://github.com/devyanshyadav/librenote-ai) · [官网](https://librenote-ai.vercel.app) · 个人维护

**自托管的 NotebookLM 替代品：上传资料对话并生成学习产物**

基于 Next.js + Supabase/PostgreSQL + pgvector 的自托管笔记本应用：用户上传 PDF、Word、网页、YouTube、音频等来源，系统切块、嵌入并存入用户自己的数据库，聊天回答带可跳转的引文；Studio 可从同一来源生成思维导图、闪卡、测验、报告、数据表、Mermaid 图、播客式音频等 8 类产物。模型通过 OpenRouter 接入（需 API key）。一键 bun run setup 依赖 Docker Desktop 与 Bun，支持多用户与按账户数据隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 PDF/Word/网页/YouTube/音频等多来源上传与带引文的有据对话
- Studio 生成 8 类产物：思维导图、闪卡、测验、报告、数据表、图、音频、笔记
- 通过 OpenRouter 选择任意模型，数据存于用户自己的 Postgres/Supabase
- 一条命令 bun run setup 完成安装与启动

## 适用场景

- 想自托管、掌控数据地使用类 NotebookLM 的资料问答
- 把研究资料转成闪卡、测验和思维导图用于学习
- 在个人服务器上部署多用户笔记本并隔离各账户数据

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13:  Upload your sources, chat with grounded citations, and generate studio artifacts — flashcards, quizzes, mind maps,
> L90: LibreNote AI is built around **notebooks and sources** — not one-off chats. Your files are chunked, embedded, and s

## 星数曲线

```mermaid
xychart-beta
    title "devyanshyadav/librenote-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3147d0de702b` · [字段定义](../../DATASET.md)*
