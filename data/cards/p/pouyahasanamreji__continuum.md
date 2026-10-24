# pouyahasanamreji/continuum

⭐ 92 · TypeScript · 推送 2026-05-14 · [GitHub](https://github.com/pouyahasanamreji/continuum) · 个人维护

**面向编码 agent 的本地 MCP 服务器：共享向量记忆与编排**

以 NestJS + SQLite（sqlite-vec）实现的本地 MCP 服务器，供 Claude Code / Codex / Cline / Cursor 等客户端接入。功能包括：将 agent 任务中产生的经验存为 768 维向量（默认内置 Snowflake arctic-embed 模型，可选 Ollama / TEI / OpenAI 兼容 embedder）、以 PLOT.md 种子化四阶段调度协议（Intake→Research→Verify→Handoff）、多 agent 注册表与保留路径状态机避免并行冲突，并附 Astro + React 网页面板。单 SQLite 文件存储，无 SaaS、无遥测。提供 Docker Compose 启动或 pnpm 裸机运行（需 Node>=22.12.0、pnpm 10.33+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- sqlite-vec 向量记忆，语义检索（metadata 先行、按需取正文）
- PLOT.md 四阶段调度协议与多 agent 注册表、保留路径冲突检测
- 客户端无关：标准 MCP / Streamable HTTP，支持各类 MCP 客户端
- 本地优先：单 SQLite 文件（WAL），默认进程内 ONNX 嵌入模型

## 适用场景

- 让多个 Claude Code / Codex 会话共享项目经验与教训
- 通过 MCP 客户端调度隔离 git worktree 中的新 agent 执行任务
- 在并行 agent 间协调文件保留路径、避免互相覆盖

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: One MCP server. Tell any client to read the plot — it becomes the orchestrator.
> L21: > Point any MCP client at Continuum and tell it to read the plot. The client becomes an orchestrator — it researche
> L42: |🔌 **Client-agnostic**|Standard MCP / Streamable HTTP. Works with Claude Code, Codex, Cline, Cursor, or anything th

## 星数曲线

```mermaid
xychart-beta
    title "pouyahasanamreji/continuum 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-24 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2d614e31e645` · [字段定义](../../DATASET.md)*
