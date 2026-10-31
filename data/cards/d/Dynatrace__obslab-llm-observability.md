# Dynatrace/obslab-llm-observability

⭐ 19 · HTML · Apache-2.0 · 推送 2026-08-25 · [GitHub](https://github.com/Dynatrace/obslab-llm-observability) · [官网](https://dynatrace.github.io/obslab-llm-observability/) · 组织维护

**Dynatrace 的旅行建议 LLM 演示应用，展示 AI 可观测性**

由 Dynatrace 提供的演示应用：用 Python 编写，接收目的地输入并经 Amazon Bedrock 大模型生成旅行建议，通过 OpenTelemetry 输出可观测性信号，可配合 Dynatrace Playground 的示例仪表盘查看。支持 GitHub Codespaces 在线体验、本地运行（配置 AWS 模型环境变量）以及本地 K8S 集群部署（需 Docker/Podman 与 kind）。声明该产品非 Dynatrace 官方支持项目，面向希望了解 AI 可观测性接入方式的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Amazon Bedrock 模型生成目的地旅行建议
- 通过 OpenTelemetry 产出可观测性信号
- 支持 GitHub Codespaces、本地运行与本地 K8S（kind）三种体验方式

## 适用场景

- 在 Dynatrace 平台上观察 LLM 应用的可观测性信号
- 参考示例接入 AI 可观测性到自有环境
- 在本地 K8S 集群中运行带 Bedrock 调用的演示应用

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Demo application for giving travel advice written in Python. Observability signals by OpenTelemetry.
> L5: Uses Amazon Bedrock to generate advice for a given destination.

## 星数曲线

```mermaid
xychart-beta
    title "Dynatrace/obslab-llm-observability 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7293250ae4aa` · [字段定义](../../DATASET.md)*
