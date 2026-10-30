# flare-foundation/flare-ai-kit

⭐ 27 · Python · Apache-2.0 · 推送 2026-04-04 · [GitHub](https://github.com/flare-foundation/flare-ai-kit) · 组织维护

**在 Flare 上构建可验证 AI Agent 的 SDK，基于 TEE**

面向开发者的 Python SDK，用于在 Flare 网络上构建可验证 AI Agent：通过 GCP Confidential Space 在 Intel TDX TEE 中运行 agent 逻辑，基于 Google ADK 提供工具调用、编排与评测，支持 Agent2Agent 协议的多 agent 共识机制，并集成 Flare 的 FTSO/FDC/FAssets 等链上数据与 X/Telegram/Farcaster 社交连接器。需 uv + Python 3.12 与 Docker，部署到 Confidential Space 需 gcloud CLI。项目处于 alpha 阶段，接口可能不兼容变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在 Intel TDX TEE（GCP Confidential Space）中可验证执行 agent 逻辑
- 基于 Google ADK 的 agent 框架（工具调用/编排/评测）
- Agent2Agent 协议下多数/锦标赛/共识学习多 agent 共识
- Flare 链上数据集成（FTSO/FDC/FAssets）与社交连接器

## 适用场景

- 构建输出可被链上验证的 AI Agent
- 多 agent 共识机制实验与开发
- 接入 Flare 生态数据（FTSO/FDC/FAssets）的 agent 应用

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: SDK for building **verifiable AI Agents** on Flare using Confidential Space Trusted Execution Environments (TEEs).
> L16: - **Agent framework**: Built on Google ADK with tool-calling, orchestration and evaluation.

## 星数曲线

```mermaid
xychart-beta
    title "flare-foundation/flare-ai-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `212dce9dc0eb` · [字段定义](../../DATASET.md)*
