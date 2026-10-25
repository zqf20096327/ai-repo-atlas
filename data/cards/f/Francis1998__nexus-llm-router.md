# Francis1998/nexus-llm-router

⭐ 123 · Python · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/Francis1998/nexus-llm-router) · 个人维护

**多 LLM 路由中间件：按任务选模型、控成本、带回退的 OpenAI 兼容 API**

面向 AI 基础设施工程师的 LLM 路由中间件：向应用暴露单一 OpenAI 兼容 API，将模型选择、回退、预算、审计与路由理由下沉到中间件层。机制包括按 prompt 复杂度分级路由（简单任务走低价低延迟模型）、成本感知路由、按用户预算护栏与 Prometheus 成本指标。README 主体列出数十个离线 HITL Advisor（如 FSM blowup、MoE dropout storm、KV 换页等比率监测顾问），各配 docs/guides 下的指南文档，多标注可用 GPT-5.5/Claude/Gemini/Kimi 抛光。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 OpenAI 兼容 API 后面做任务感知路由与回退
- prompt 复杂度分级：简单任务路由到低成本低延迟模型
- 按用户预算护栏与 Prometheus 成本指标
- 数十个离线 HITL 指标 Advisor（FSM blowup、KV steal、prompt-cache poison 等）

## 适用场景

- 多模型生产流量中按任务难度自动分配模型以控成本
- 为按用户的 LLM 预算设置护栏并导出成本指标
- 在应用与多家模型服务商之间加一层稳定网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: > Intelligent multi-LLM routing middleware with task-aware model selection, cost optimization, fallback safety, and 
> L248: Most teams start with one LLM endpoint. That works until traffic grows, latency starts swinging, finance asks why 
> L250: Nexus is designed for AI infrastructure engineers running multi-model production pipelines where quality, latency,

## 星数曲线

```mermaid
xychart-beta
    title "Francis1998/nexus-llm-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-25 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2408cc605911` · [字段定义](../../DATASET.md)*
