# ZeroDot1/LLMWikiNG

⭐ 44 · Python · AGPL-3.0 · 推送 2026-10-08 · [GitHub](https://github.com/ZeroDot1/LLMWikiNG) · 个人维护

**本地隐私优先的 AI 维护个人 Wiki 平台（OKF v0.2）**

基于 Karpathy LLM-Wiki 模式的本地知识库平台：将原始文档一次性编译为结构化、互链的 Markdown Wiki，由本地 LLM 与 agent 生成摘要、更新页面、记录矛盾，替代逐次 RAG 检索。支持 OKF v0.2 摄取（含 EPUB/PDF），提供 wiki.sh CLI（ingest/search/lint/history 等约 18 个命令）与 FastAPI Web 界面（WYSIWYG 编辑器、交互式知识图谱、BM25 跨 Wiki 搜索、标签云、周报邮件、审计日志、用户/API Key/MCP Key 管理、Tailscale 集成）。AI 后端通过 Ollama 端点配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档一次性编译为互链 Markdown Wiki，LLM 增量更新并记录矛盾
- OKF v0.2 摄取支持 WebUI/REST API/MCP，含 EPUB 与 PDF
- wiki.sh CLI 覆盖 ingest、FTS5 搜索、lint、版本历史等操作
- Web 界面含知识图谱、跨 Wiki BM25 搜索、审计日志与用户/密钥管理

## 适用场景

- 把文章、PDF、笔记沉淀为可持续更新的个人知识库
- 在浏览器中阅读、搜索、编辑本地 Wiki 并可视化页面关系
- 通过 REST API 或 MCP 远程提交文档自动生成摘要入 Wiki

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L9: A complete pattern for building and maintaining a personal knowledge base (wiki) following the standardized Open Kno
> L19: Instead of searching documents ad-hoc via RAG (Retrieval-Augmented Generation) on every query and regenerating know
> L34: * `./wiki.sh ingest ` – Reads a new source, archives it in `raw/`, generates an AI summary, creates/updates the wik

## 星数曲线

```mermaid
xychart-beta
    title "ZeroDot1/LLMWikiNG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `40d0b8c4ff9b` · [字段定义](../../DATASET.md)*
