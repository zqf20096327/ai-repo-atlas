# esagduyu/project-tiro

⭐ 14 · Python · MIT · 推送 2026-07-03 · [GitHub](https://github.com/esagduyu/project-tiro) · 个人维护

**本地优先的个人阅读系统：网页/邮件存为 Markdown 并生成 AI 摘要**

面向个人用户的本地优先阅读工具：将网页文章与邮件通讯保存为干净的 Markdown，存于本机 SQLite 与 ChromaDB。调用 Anthropic API（Opus 4.6 做深度推理、Haiku 做自动标签/实体/摘要抽取）生成每日摘要、跨文档矛盾发现、偏见检测，并根据用户评分学习阅读偏好分级文章。提供 FastAPI 后端、Web 阅读界面、Chrome 扩展、MCP 服务器（供 Claude Desktop/Code 查询文库）与全文导出。本仓库为已冻结的黑客松提交版本，后续开发转移至 esagduyu/tiro。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 网页/.eml 邮件保存为 Markdown，本地 SQLite + ChromaDB 存储
- Opus 4.6 生成每日摘要（按重要性/主题/实体三种）并发现跨文档矛盾
- 基于评分学习阅读偏好，将文章分为必读/略读/丢弃三档
- 内置 MCP 服务器，可被 Claude Desktop/Code 查询与保存内容

## 适用场景

- 把常读的网页文章和邮件通讯集中保存、清理成 Markdown 阅读
- 每天用 AI 摘要掌握所读内容并发现来源间的矛盾
- 在 Claude Desktop/Code 中查询自己的阅读文库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: Tiro saves web pages and email newsletters as clean markdown on your machine, enriches them with AI-extracted tags,
> L23: - **Local-first** — Your data lives on your machine as plain markdown files, SQLite, and ChromaDB. No cloud, no loc

## 星数曲线

```mermaid
xychart-beta
    title "esagduyu/project-tiro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `481a055381d5` · [字段定义](../../DATASET.md)*
