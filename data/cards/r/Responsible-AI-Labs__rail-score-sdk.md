# Responsible-AI-Labs/rail-score-sdk

⭐ 15 · Python · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Responsible-AI-Labs/rail-score-sdk) · [官网](https://pypi.org/project/rail-score-sdk/) · 组织维护

**RAIL Score API 官方 Python SDK：8 维 LLM 评测与合规检查**

面向开发者的 Python 客户端库，封装 RAIL Score API：对 AI 生成内容按公平性、安全性、可靠性等 8 个维度（0-10 分）评分，支持 basic/deep 两种模式；提供策略引擎在低于阈值时阻断，安全再生成循环（服务端 RAIL_Safe_LLM 或外部自有模型），GDPR/HIPAA/EU AI Act 等 6 套合规框架检查，以及 agent 工具调用的前置/后置风险评估与提示注入检测。附带 OpenAI/Anthropic/Gemini 包装器、OpenTelemetry 遥测、Langfuse 与 LiteLLM 网关集成。需 API key，依赖托管 API 服务。

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

- 8 维度（0-10 分）内容评测，basic/deep 双模式
- 6 套合规框架检查（GDPR/CCPA/HIPAA/EU AI Act 等）
- agent 工具调用前置/后置安全评估与提示注入检测
- OpenTelemetry 遥测、Langfuse 与 LiteLLM 网关集成

## 适用场景

- 对 LLM 应用输出做责任 AI 评分与阈值拦截
- 检查 AI 内容是否符合 GDPR/HIPAA 等法规框架
- 为 agent 工具调用做调用前风险拦截与提示注入检测

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Official Python client library for the RAIL Score API for evaluating AI-generated content across 8 dimensions of Res
> L15: The SDK sits between your application and the RAIL Score API, providing sync/async clients, policy enforcement, LLM
> L204: Drop-in wrappers that automatically evaluate every LLM response via RAIL Score.

## 星数曲线

```mermaid
xychart-beta
    title "Responsible-AI-Labs/rail-score-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `da0da47cbff5` · [字段定义](../../DATASET.md)*
