# Carer-Healthcare-AI/Hospilot

⭐ 17 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/Carer-Healthcare-AI/Hospilot) · 组织维护

**医院运营的多智能体 AI 操作层，读 HIS 数据并协调执行**

Carer Healthcare AI 开源的医院运营智能体平台：通过 Fabric（FHIR R5 翻译层，支持 change API/轮询/Kafka 接入）实时读写既有 HIS 数据，LLM 规划器将自然语言目标拆解为智能体 DAG 管道；内置 14 个领域智能体覆盖床位、急诊分诊、ICU 容量、排班、药房、计费等，关键动作在执行图中暂停等待人工审批。编排基于 LangGraph（Temporal 可选默认关闭），临床数据不落库。需 Python 3.11+/Docker，且需自备带 Hasura 的 Postgres。预测 AI、数字孪生等仅在路线图中未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 规划器将目标转为智能体 DAG 管道，含 14 个领域智能体
- Fabric 以 FHIR R5 实时读写 HIS API，自身不存储临床数据
- 人工审批内嵌于执行图，关键动作持久等待决策
- 智能体清单系统声明各智能体可访问的数据范围

## 适用场景

- 急诊高峰期协调分诊与床位收治
- ICU 容量紧张时评估转出与收治方案
- 排查全院床位周转与出院延迟瓶颈
- 护理排班缺口与药房优先级核查

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L46: This repo contains **Fabric** and the **Agentic Framework**, end to end and runnable on
> L56: - **Multi-Agent Coordination** — the planner wires one goal into a DAG of exactly the
> L203: |**LLM**|Anthropic Claude, or any OpenAI-compatible endpoint (e.g. local Ollama)|

## 星数曲线

```mermaid
xychart-beta
    title "Carer-Healthcare-AI/Hospilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `998289d1592a` · [字段定义](../../DATASET.md)*
