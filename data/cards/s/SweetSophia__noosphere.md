# SweetSophia/noosphere

⭐ 29 · TypeScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/SweetSophia/noosphere) · [官网](https://noosphere-memory.com) · 个人维护

**AI agent 的自托管记忆与知识层，兼作人类 Markdown wiki**

自托管的知识/记忆服务，供 AI agent 与人共用同一数据：agent 通过 MCP 工具或 REST 读写项目记忆（草稿保存后由人策展为 wiki 文章），人通过 Web UI 浏览、编辑、检索 Markdown 文章。基于 PostgreSQL（含 Redis 加速），支持主题层级、修订历史、scoped API key 权限、Obsidian 导入导出；集成 OpenClaw、Codex CLI、Hermes Agent、OpenCode、Kilo Code 等，可选 pgvector 混合检索与 llama.cpp 本地 embedding。经校验安装器以 Docker Compose 部署。当前分支为 1.15.1 发布候选，因 Zod 依赖资质问题处于 hold 状态，公开版本仍为 1.15.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 与人共享同一 PostgreSQL 记忆库，草稿记忆经人工策展进 wiki
- Codex CLI 提供 5 个原生 MCP 工具与 npx 独立安装
- scoped API key 按范围限制读写权限
- 可选 pgvector/RRF 混合检索与 llama.cpp 本地 embedding

## 适用场景

- 给多个 agent 工具（OpenClaw/Codex/OpenCode 等）挂接同一份项目记忆
- 把 agent 自动记忆策展为可浏览的团队 wiki
- 通过 Obsidian 同步在 Markdown 工作流中使用记忆数据

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L4: Noosphere is a self-hosted knowledge and memory layer for AI agents and humans.
> L14: - **Agent memory**: recall relevant project context, save draft memory
> L160: ## Choose an Integration

## 星数曲线

```mermaid
xychart-beta
    title "SweetSophia/noosphere 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-29 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `36a7de89f4f2` · [字段定义](../../DATASET.md)*
