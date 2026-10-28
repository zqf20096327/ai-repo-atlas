# dynatrace-oss/dt-evals

⭐ 52 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/dynatrace-oss/dt-evals) · 组织维护

**面向 Dynatrace 用户的 LLM 评测 CLI 与工具集**

Dynatrace 开源的 LLM 端到端评测工具集，含 CLI（dt-evals）、TypeScript 库（dt-eval-lib）、部署资源（dt-eval-deploy）与 Python 摄取库（dt-ai-ingest）。核心机制：从 Dynatrace 环境拉取生产 gen_ai.* spans，在内存中脱敏，用 LLM judge（OpenAI/Anthropic/Vertex/Bedrock/Azure OpenAI）按 15 个内置评估器打分，结果以业务事件写回 Dynatrace，与 trace/指标/告警/仪表盘同处一处。限制：需 Node.js≥20、Dynatrace 环境与平台 token；项目自述处于早期开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 拉取生产 GenAI spans 并以 LLM judge 评分，结果写回 Dynatrace 业务事件
- 15 个内置评估器（faithfulness、hallucination、pii-leakage 等）+ 漂移检测
- 支持 OpenAI/Anthropic/Vertex Gemini/Bedrock/Azure OpenAI 五类 judge 提供商
- 支持 CI 门禁（--ci）、定时调度与 AWS/GCP/Azure 无服务器部署

## 适用场景

- 在生产 GenAI 流量上运行忠实度、幻觉、PII 泄露等评测
- 在 CI（GitHub Actions）中对评测指标设阈值门禁
- 将第三方 LLM span 与评测结果摄取进 Dynatrace 统一观测

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: End-to-end LLM evaluation toolkit for Dynatrace AI Observability.
> L12: `dt-evals` is the main interface. It pulls live `gen_ai.*` spans from your Dynatrace environment, masks sensitive d
> L25: |`dt-evals`|CLI — configure, run, schedule, inspect, and deploy evals|

## 星数曲线

```mermaid
xychart-beta
    title "dynatrace-oss/dt-evals 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-28 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `464048aee083` · [字段定义](../../DATASET.md)*
