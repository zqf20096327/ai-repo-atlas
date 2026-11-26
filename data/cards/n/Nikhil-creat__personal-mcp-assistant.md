# Nikhil-creat/personal-mcp-assistant

⭐ 3 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Nikhil-creat/personal-mcp-assistant) · [官网](https://nikhil-creat.github.io/personal-mcp-assistant/) · 个人维护

**面向个人的 MCP 智能体：用自然语言管理日历、笔记与扫描件**

基于 Groq 的 ReAct 智能体，通过 Model Context Protocol 暴露 12 个工具，覆盖日历事件增改与冲突检测、笔记混合检索（pgvector + tsvector + RRF）、扫描图像的 CNN/OCR 摄取，以及长期记忆与反思校验。提供两种运行方式：GitHub Pages 纯浏览器静态版（BYOK Groq key）与 Docker Compose 全栈版（MCP 服务器 + Postgres/pgvector + Python CNN worker），另有无 UI 的 CLI 模式，可接 MCP Inspector 或 Claude Desktop。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 12 个 MCP 工具覆盖日历、笔记、视觉文档摄取与长期记忆
- 混合检索：pgvector 向量 + tsvector 关键词 + RRF 融合
- 浏览器内运行的静态版（本地混合 RAG、in-browser CNN/OCR）
- Docker Compose 一键编排 MCP 服务器、Postgres 与 CNN worker

## 适用场景

- 通过对话创建、改期日历事件并检测日程冲突
- 混合检索个人笔记并生成跨上下文摘要
- 摄取扫描文档并纳入可检索知识
- 在 Claude Desktop / MCP Inspector 中调试个人 MCP 工具

## 场景标签

`Agent 记忆` `知识库管理` `RAG` `OCR` · 领域:Agent 开发

## 证据(README 行号)

> L5: Groq-powered ReAct agent over your calendar, notes and scanned images, exposed through the Model Context Protocol. H
> L8: - **Static site (GitHub Pages):** `docs/` — no build, runs fully in the browser (Groq BYOK, local hybrid RAG, in-bro

## 星数曲线

```mermaid
xychart-beta
    title "Nikhil-creat/personal-mcp-assistant 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `6d5cc6299a0d` · [字段定义](../../DATASET.md)*
