# 28naem-del/mnemosyne

⭐ 151 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/28naem-del/mnemosyne) · [官网](https://mnemosy.ai) · 个人维护

**AI agent 的本地长期记忆：单 SQLite 文件 + 证据溯源**

面向 AI agent 的 local-first 长期记忆系统：以一个 SQLite 文件存储记忆及其来源证据，通过 MCP server、TypeScript SDK、CLI 和带鉴权的 HTTP 服务供宿主接入。核心机制包括证据挂钩的记忆存取（16 个 memory_* MCP 工具）、来源被更正时自动退役依赖该来源的记忆、跨 agent 的检查点/恢复交接、证据把关的技能试验，以及 BM25 默认 + 可选向量混合检索与重排。Local Engine 无需模型 API key、数据库服务器或 Docker；要求 Node.js ≥22.16。当前为 2.0.0-rc.10 发布候选，README 明示两个 Tier 1 目标未达标并公布未命中题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 SQLite 文件的本地记忆引擎，无需 API key、服务器或 Docker
- 来源更正时退役依赖记忆，支持 asOf/knownAt 时间查询
- 16 个 memory_* MCP 工具，接入 Claude Code 与 Cursor
- LongMemEval-S 409/500，未命中题目与 COMPARISON.md 对比数据公开

## 适用场景

- 给 Claude Code/Cursor 等 MCP 客户端挂一个可长期积累的本地记忆
- 跨会话/跨 agent 交接：checkpoint 恢复目标、决策与下一步
- 需求变更后自动退役过时的流程记忆，避免重复失效经验
- 证据把关的技能库：试验失败或证据变更即退役

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Mnemosyne is local-first, long-term memory for AI agents: one SQLite file that keeps what an agent learned togeth
> L41: The server exposes 16 `memory_*` tools (`memory_store`, `memory_recall`, `memory_context`, `memory_correct`, `memor

## 星数曲线

```mermaid
xychart-beta
    title "28naem-del/mnemosyne 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 149 --> 152
    line [150, 151, 151]
```

2026-10-18 150 → 2026-10-28 151（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `81668ece222e` · [字段定义](../../DATASET.md)*
