# fstamatelopoulos/cerefox

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/fstamatelopoulos/cerefox) · [官网](https://cerefox.org/) · 个人维护

**AI agent 共享记忆层：多工具共享可检索知识库**

基于 Postgres + pgvector 的持久化共享记忆层，供多个 AI 工具（Claude、ChatGPT、Cursor、Codex、Gemini）读写同一知识库：任一 agent 写入的知识可被其他 agent 跨会话检索。提供全文 BM25 + 语义向量的混合搜索、元数据过滤、版本治理与不可变审计日志，访问路径覆盖本地/远程 MCP、CLI、Web UI 与 GPT Actions。部署支持托管 Supabase 或本地单容器 Docker（Postgres+pgvector 打包）；嵌入默认走 OpenAI API，本地模式可选离线 ONNX 模型。支持 Markdown/.txt/.docx 摄入，不支持 PDF。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BM25+向量混合搜索与元数据过滤，跨 MCP/CLI/Web UI 访问
- 版本治理：版本归档、保留策略、diff 查看与不可变审计日志
- 并发安全写入（乐观锁）与 SHA-256 去重、部分文档编辑
- 两种部署：托管 Supabase 或单容器本地 Docker（含离线嵌入模型选项）

## 适用场景

- 在 Claude/Cursor/Codex 等多个 AI 工具间共享同一份持久知识库
- agent 在编码会话中写入决策，其他机器上的 agent 日后检索到
- 对 agent 写入操作做审计与人工审核（pending_review 工作流）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **User-owned shared memory for AI agents.** A persistent, curated knowledge layer that multiple AI tools can read an
> L17: The primary use case is **shared memory across AI agents**: knowledge written by one tool (Claude, ChatGPT, Cursor,
> L28: - **Any agent, anywhere**: local MCP (Claude Code, Codex, Cursor, Gemini, Claude Desktop); remote MCP via Supabase 

## 星数曲线

```mermaid
xychart-beta
    title "fstamatelopoulos/cerefox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `346f5e389335` · [字段定义](../../DATASET.md)*
