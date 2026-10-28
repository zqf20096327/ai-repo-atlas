# edwin-hao-ai/Awareness-Local

⭐ 199 · JavaScript · MIT · 推送 2026-05-04 · [GitHub](https://github.com/edwin-hao-ai/Awareness-Local) · 个人维护 · 中文 README

**给 AI 编码代理的本地持久记忆 MCP 服务器**

本地优先的 MCP 记忆服务器，为 Cursor、Claude Code、Copilot、Cline 等 13+ MCP 兼容 IDE/代理提供跨会话持久记忆。在本地运行轻量守护进程，记忆以 Markdown 存储于 .awareness/ 目录，用 SQLite FTS5 + embedding 做关键词+语义混合检索，并提供知识卡片抽取、渐进式两段召回（摘要→全文）以控制 token 用量，附带 Web 仪表盘。云同步为可选项。要求 Node.js 18+，无需 Python、Docker 或云账户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown 存储 + SQLite FTS5/embedding 混合检索
- 13+ MCP 兼容 IDE 自动检测接入
- 渐进式两段召回控制 token 用量
- 本地离线运行，云同步可选

## 适用场景

- 跨多个会话的长期代码库迁移
- 团队交接时代理保留先前实现上下文
- 个人编码工作流保存偏好与约定

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: Awareness Local is a local-first MCP memory server for AI coding agents. It gives Cursor, Claude Code, Copilot, Cli
> L19: It runs a lightweight daemon on your machine, stores memory as Markdown, indexes recall with SQLite FTS5 + embeddin
> L136:     │  MCP Protocol (localhost:37800)

## 星数曲线

```mermaid
xychart-beta
    title "edwin-hao-ai/Awareness-Local 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 198 --> 200
    line [199, 199]
```

2026-10-18 199 → 2026-10-28 199（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8b21f31cf7c6` · [字段定义](../../DATASET.md)*
