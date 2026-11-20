# Responsible-AI-Labs/rail-score-js

⭐ 10 · TypeScript · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Responsible-AI-Labs/rail-score-js) · [官网](https://www.npmjs.com/package/@responsible-ai-labs/rail-score) · 组织维护

**开发者用的 LLM 内容评测与合规 SDK（8 维度评分）**

RAIL Score 的官方 JavaScript/TypeScript SDK，调用其托管 API 对内容进行 safety、privacy、fairness 等 8 个维度评分，并提供安全重新生成、6 种合规框架检查（GDPR/CCPA/HIPAA/EU AI Act/印度 DPDP 等）、Agent 工具调用风险评估、提示注入检测与本地策略引擎。支持 OpenAI/Anthropic/Google 封装、Langfuse 与 OpenTelemetry 可观测性。通过 npm 安装，需 RAIL Score API key，评估在服务端执行。

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

- 8 维度内容评分与 per-dimension 解释、问题与改进建议
- Agent 评估：工具调用前后风险评估、提示注入检测、计划评估、会话模式检测
- 多框架合规检查与印度 DPDP 专用命名空间（含零延迟本地 PII 扫描器）
- 内置 OpenAI/Anthropic/Google Generative AI 封装与 Langfuse/OTEL 可观测性

## 适用场景

- 给 LLM 应用上线前的内容做安全与合规评分
- 为 Agent 工具调用加预/后风险检查与注入检测
- 按 GDPR/HIPAA/DPDP 等框架核查内容的合规性
- 通过策略引擎自动拦截或重新生成违规内容

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: Official JavaScript/TypeScript SDK for the RAIL Score API — evaluate and generate responsible AI content with compre
> L21: - **Policy Engine** — Configurable content enforcement (log, block, regenerate, custom)

## 星数曲线

```mermaid
xychart-beta
    title "Responsible-AI-Labs/rail-score-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `c3133deed097` · [字段定义](../../DATASET.md)*
