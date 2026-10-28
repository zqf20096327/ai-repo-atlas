# demml/opsml

⭐ 42 · Rust · NOASSERTION · 推送 2026-05-16 · [GitHub](https://github.com/demml/opsml) · [官网](https://docs.demml.io/opsml) · 组织维护

**面向传统 ML 与 agentic 系统的 AI 生命周期治理平台**

OpsML 以 card 为核心抽象，对数据、模型、实验、提示词、agent 与服务做版本化、加密与注册管理，涵盖从训练到生产部署的 lineage、监控与可观测性。Card 可用 Python 或 YAML 创建，持久化到 Rust 服务器，并在 SvelteKit UI 中可视化。支持多数据库（SQLite/PostgreSQL/MySQL）与多云存储（S3/GCS/Azure Blob），通过 Scouter 做漂移检测，提供 OpenTelemetry 可观测性与离线/在线 GenAI 评测（beta）。pip 安装，CLI 管理 agent 与服务部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- card 抽象统一版本化/加密/注册数据、模型、提示词、agent 与服务
- Rust 核心 + PyO3 绑定，SvelteKit UI 编译进服务器二进制
- 支持 SQLite/PostgreSQL/MySQL 与 S3/GCS/Azure Blob 存储
- 基于 Scouter 的漂移检测与数据画像，OpenTelemetry 可观测性（beta）

## 适用场景

- 团队对数据集、模型与实验做统一版本管理与溯源
- 注册、评测并治理跨 provider 的 agent 与提示词
- 将模型+提示词+agent 打包为版本化服务部署

## 场景标签

`MLOps` `LLM 可观测性` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: OpsML is an AI lifecycle management platform built for the governance of both traditional ML and agentic AI systems
> L22: - **Agentic** — manage and version prompts, create, register, and evaluate agents across providers (OpenAI, Anthrop
> L23: - **Agents** — register, version, and govern agents with `AgentCard`; define specs in YAML and manage the full life

## 星数曲线

```mermaid
xychart-beta
    title "demml/opsml 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-28 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbf022b56a45` · [字段定义](../../DATASET.md)*
