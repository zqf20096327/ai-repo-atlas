# JoeJiang-927117/Super-Knowledge-Base

⭐ 8 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/JoeJiang-927117/Super-Knowledge-Base) · [官网](https://joejiang-927117.github.io/Super-Knowledge-Base/) · 个人维护 · 中文 README

**本地 Markdown 知识库编译器：PDF/Office 汇入可审计 Wiki，带 MCP 供 Claude/Cursor 检索**

面向工程、运维、合规与项目交付团队的本地知识库桌面应用（Electron + React + Node/SQLite + Git）：将 PDF/DOCX/XLSX/PPTX/Markdown 编译为结构化 Markdown Wiki，引用摘录回溯原文行/页定位，不可验证内容被丢弃。AI 产出走 Draft→Review→Published 审核流，删除提议进入回收站，支持 Git 回滚。内置 MCP stdio 服务器，供 Claude Code、Cursor 等检索与引用本地知识库。检索为 BM25+SQLite 向量+TF-IDF+精确 token 提升的 RRF 融合，支持三级模型路由与 Ollama/vLLM 本地后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引用摘录回溯原始行/页定位，不可验证的生成内容被丢弃
- AI 变更走声明式审核流，删除提议经 Pending Delete + 回收站拦截，Git 回滚
- 内置 MCP stdio 服务器，暴露 search/ask/propose_draft 等工具
- RRF 四信号混合检索（双语 BM25、SQLite 向量、TF-IDF 互索引、精确 token 提升）

## 适用场景

- 把散落的 PDF 规范、Word SOP、Excel 台账编译成可审计的团队 Wiki
- 合规场景下要求 AI 产出经人工审核后才发布、禁止静默改动正式文档
- 通过 Claude Code/Cursor 的 MCP 检索与引用本地已审核知识库
- 内网部署用 Ollama/vLLM 本地模型处理涉密文档问答

## 场景标签

`文档问答` `知识库管理` `RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5:  Drop a messy folder of PDFs, Word, Excel, PPT &amp; Markdown. Get an auditable local Markdown Wiki + Git history + 
> L51: 2. **Two-Stage Knowledge Compilation & Excerpt Verification**: Structure-aware chunking, zero-bloat OOXML parsing, 
> L68: ZHIXU ships a zero-dependency **Model Context Protocol (MCP)** stdio server (`out/main/mcp.js`) so **Claude Code, C


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `8824599c90c6` · [字段定义](../../DATASET.md)*
