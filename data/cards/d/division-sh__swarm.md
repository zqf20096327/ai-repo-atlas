# division-sh/swarm

⭐ 23 · Go · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/division-sh/swarm) · [官网](https://www.division.sh) · 组织维护

**以确定性引擎运行多 LLM Agent 编排的自托管框架**

用 Go 编写的多 Agent 系统运行时：开发者以 YAML 声明状态机、事件、Agent 与策略，由确定性引擎调度成百上千个实体，负责状态持久化、事务提交、隔离、成本计量与崩溃恢复；路由由订阅与 CEL 条件决定，LLM 不参与控制流。事件溯源日志支持任意运行的回放与分叉，人通过持久化邮箱作为一等参与者介入。本地默认 SQLite（单二进制、无需凭据即可启动 agent-free 流程），生产可选 Postgres；支持 Anthropic API、Claude CLI、OpenAI 兼容端点等多种 LLM 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性控制循环：路由由订阅与 CEL 条件决定，LLM 不决定系统状态
- 事件溯源持久化：任意运行可逐轮回放、审计或从日志分叉
- Agent 隔离：作用域会话与 per-entity Docker 工作区
- 单 Go 二进制，本地默认 SQLite，生产可选 Postgres

## 适用场景

- 把订单、工单等业务建模为多 Agent 状态机流程并持久化运行
- 需要可回放、可审计、可分叉重试的 Agent 生产工作流
- 在编排中保留人工审批节点的人机协同场景

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: Swarm runs fleets of LLM agents as a durable, stateful system. You declare it in YAML and a deterministic engine ru
> L17: Single Go binary, local/dev SQLite by default with Postgres as a production opt-in. Multiple LLM backends ship toda
> L155: A contract bundle is verified by the static analyzer, then loaded into the engine, which starts the event loop. Fr

## 星数曲线

```mermaid
xychart-beta
    title "division-sh/swarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6f1bd892b933` · [字段定义](../../DATASET.md)*
