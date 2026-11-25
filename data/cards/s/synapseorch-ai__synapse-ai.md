# synapseorch-ai/synapse-ai

⭐ 343 · Python · AGPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/synapseorch-ai/synapse-ai) · [官网](https://synapseorch.com) · 组织维护

**给开发者的可审批固定路径 AI 工作流编排应用**

SynapseOrch 是一个自托管的 AI 工作流构建与运行应用：用户用自然语言描述任务，内置的 Synapse AI 助手生成步骤计划（含每步模型选择、成本预估与人工签核点），经用户批准后按固定 DAG 路径运行，模型不决定步骤走向。支持 Slack/Telegram 等渠道签核、每步成本展示与单次运行支出上限。提供 Web UI、CLI、REST API、MCP server 与 OpenAI 兼容端点，Scale 模式提供 Redis 队列、worker 与 Postgres 检查点。AGPL-3.0，无账号与遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述生成计划，批准后按固定路径运行
- 人工签核步骤与每步成本预估、支出上限
- 支持 MCP server、REST API 与 OpenAI 兼容端点
- Scale 模式：Redis 队列、多 worker、Postgres 检查点

## 适用场景

- 搭建每次运行行为一致的定时 AI 自动化流程
- 在关键工具调用处插入人工审批
- 通过本地模型（Ollama）让数据不出机器地跑工作流步骤

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L96: |**SynapseOrch**|An app that builds and runs AI workflows, with a UI, REST API, CLI and MCP server|Describing it (S
> L14: **It's for** developers and automation builders, working for their own team or for clients, who need an AI workflow

## 星数曲线

```mermaid
xychart-beta
    title "synapseorch-ai/synapse-ai 星数(近 15 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-25"]
    y-axis "stars" 330 --> 344
    line [331, 332, 333, 334, 335, 336, 337, 332, 338, 339, 340, 341, 342, 343, 343]
```

2026-10-23 331 → 2026-11-25 343（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `d858cdc4fc6f` · [字段定义](../../DATASET.md)*
