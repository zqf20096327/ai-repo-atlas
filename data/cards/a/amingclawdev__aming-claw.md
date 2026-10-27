# amingclawdev/aming-claw

⭐ 29 · Python · NOASSERTION · 推送 2026-10-06 · [GitHub](https://github.com/amingclawdev/aming-claw) · 个人维护

**给开发者的本地优先 AI 编码治理层：推送式引导与审计 Agent 改动**

面向 AI 编码开发的本地治理运行时：在 Agent 行动前推送当前角色、契约、下一合法动作、所需证据与验证门（push 而非 pull），并以 Facts+Rules→Guide 的机制约束 Agent。提供 MCP 工具供 Agent 查询实时项目状态、提交绑定的项目图与事件溯源证据、本地仪表盘（backlog/图/Review 队列）、并行工作路径与人工审核队列（AI 提案等待接受/拒绝）。通过 aming-claw CLI 与 pip 安装，提供 Claude Code / Codex 插件接入与可选 Docker 演示镜像；采用 FSL 1.1（MIT 变更日期）许可。已知限制在 README 中显式列出（如图 API 文件较大仅做有界测试）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 推送式引导运行时：Agent 行动前下发角色、契约、下一合法动作与验证门
- MCP 工具让 Agent 查询实时项目状态而非依赖会话记忆
- 本地仪表盘：活动流、backlog、提交绑定项目图、Review 队列
- 人工审核队列：AI 提案等待接受/拒绝

## 适用场景

- 治理本地 AI 编码 Agent，防止其越权或漂移
- 审计 AI 对代码库的每次改动并做人审
- 在契约约束下运行并行多 worker 开发与有序合并

## 场景标签

 · 领域:开发者工具/AI 编码治理

## 证据(README 行号)

> L5: Aming Claw is a local-first governance layer for AI-coded development. It
> L28: - MCP tools for agents to query live project state instead of relying on chat
> L222: ```text

## 星数曲线

```mermaid
xychart-beta
    title "amingclawdev/aming-claw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e770c25d9a0b` · [字段定义](../../DATASET.md)*
