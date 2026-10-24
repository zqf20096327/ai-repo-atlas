# ogham-mcp/ogham-mcp

⭐ 116 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ogham-mcp/ogham-mcp) · [官网](https://ogham-mcp.dev) · 组织维护

**给 AI 编码代理的持久共享记忆 MCP 服务器**

面向 AI coding agent 的共享记忆层：以 MCP 服务器形式运行，在 Claude Code、Cursor、OpenCode 等客户端之间共享同一份持久记忆。检索机制为 pgvector + tsvector 混合搜索（RRF 融合）加类型边知识图，存储于 Postgres/Supabase/Neon 数据库（需自备数据库）。提供初始化向导、Docker 镜像、HTTP 多代理模式，以及 Obsidian/Telegram/Slack 摄入适配器、导入器、ONNX 本地嵌入等能力。需 Python 3.13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨客户端共享的持久记忆，stdio/HTTP 两种 MCP 传输
- pgvector+tsvector 混合搜索（RRF）+ 类型边知识图，单条 SQL 完成检索
- Docker 镜像与 uvx/源码安装三种途径，ogham init 配置向导
- Obsidian/Telegram/Slack 摄入适配器与多来源导入器

## 适用场景

- 让不同编码代理客户端共享同一份项目记忆与决策记录
- 代理会话间保留代码库背景，避免重复解释与调试
- 将 Obsidian 笔记、Telegram/Slack 消息沉淀进代理记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: Ogham gives your agents one shared memory that persists across sessions and clients. It is a **retrieval engine**: 
> L94: By default, Ogham runs in stdio mode -- each MCP client spawns its own server process. To let several agents share 
> L128: - **`ogham`** -- the CLI. Use this for `ogham init`, `ogham health`, `ogham search`, and other commands you run yo

## 星数曲线

```mermaid
xychart-beta
    title "ogham-mcp/ogham-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 114 --> 117
    line [115, 116, 116]
```

2026-10-18 115 → 2026-10-24 116（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6b20d2f5a20a` · [字段定义](../../DATASET.md)*
