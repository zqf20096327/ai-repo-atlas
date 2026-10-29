# ITSpecialist111/HASS-AI-Orchestrator

⭐ 58 · Python · 推送 2026-07-11 · [GitHub](https://github.com/ITSpecialist111/HASS-AI-Orchestrator) · [官网](https://github.com/ITSpecialist111/HASS-AI-Orchestrator) · 个人维护

**Home Assistant 的多 agent 推理与策略编排层**

面向 Home Assistant 的自主多 agent 编排系统：本地 LLM（Ollama/gemma）以 Rapid/Balanced/Deep 三档推理档位调研实时家居状态，把自然语言目标转为可审查的精确执行计划；默认 dry-run、敏感服务门控、变更需人工批准后确定性重放执行。运行时负责工具校验、并发安全、重试边界与审计持久化。附带 RAG 与情景记忆（ChromaDB + 本地嵌入），以 HA 插件形式部署，提供 React 仪表盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 Ollama 模型三档推理档位调研实时 HA 状态
- 变更调用先拦截为精确计划，批准后确定性重放
- 默认 dry-run、敏感服务门控、生成仪表盘沙箱化运行
- ChromaDB + 本地嵌入的 RAG 与情景记忆

## 适用场景

- 用自然语言目标审计全屋能耗、安全或舒适度
- 把难以写成静态规则的模糊家居目标转为可审查计划
- 通过仪表盘审批和重放 AI 提出的设备操作

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L12: **AI Orchestrator is an attempt to combine those strengths without allowing the model to become the safety system.*
> L32: - **Today:** run local `gemma4:e4b` in Rapid, Balanced, or Deep mode; investigate live HA state; create exact plans
> L151: Optional RAG and episodic memory use ChromaDB plus local Ollama embeddings to store:

## 星数曲线

```mermaid
xychart-beta
    title "ITSpecialist111/HASS-AI-Orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-29 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f85377df2b81` · [字段定义](../../DATASET.md)*
