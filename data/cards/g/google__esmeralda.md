# google/esmeralda

⭐ 23 · HCL · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/google/esmeralda) · 组织维护

**面向 Google Cloud 的企业级 AI Agent 生产化参考蓝图**

Google 维护的单仓蓝图，用于在 GCP 上将自主 AI Agent 与 MCP 服务器部署到生产环境：上层 /apps 供开发者用 Google ADK 构建 Gemini 驱动的 orchestrator 与 specialist agent（A2A/MCP 协议），下层 /infrastructure 用 Terragrunt/Terraform 维护零信任基础设施（Shared VPC、SPIFFE Agent 身份、Agent Gateway、Model Armor、FinOps）。参考用例为抵押贷款审批助手。需 gcloud、terraform、terragrunt 与 uv，通过 make 目标逐层部署。部分功能默认未启用（Cloud SQL 任务存储、Model Armor）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 应用与基础设施解耦的单仓结构（/apps 与 /infrastructure）
- A2A 协作 + MCP 工具生态，经 Central Agent Gateway 授权每跳调用
- SPIFFE Agent 身份、私有网络与零信任治理
- 分层 Terragrunt 部署（L0-L5）与 OpenTelemetry/FinOps 可观测性

## 适用场景

- 企业在 GCP 上参考该蓝图落地多 Agent 生产部署
- 平台团队复用其零信任基础设施与 CI/CD 模板
- 学习 Agent 网关、注册表与治理架构的组织方式

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L20: **ESMERALDA** is an opinionated, commercial-grade reference blueprint designed to accelerate the journey of autonom
> L23: * **Above (`/apps`):** AI and software engineers focus purely on intelligence, Gemini-powered reasoning, and tool i

## 星数曲线

```mermaid
xychart-beta
    title "google/esmeralda 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5bb7cb464f22` · [字段定义](../../DATASET.md)*
