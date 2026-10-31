# microsoft/entra-agentid-samples

⭐ 15 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/microsoft/entra-agentid-samples) · 组织维护

**微软 Entra Agent ID 的可运行示例集：为 AI agent 配置身份认证**

微软官方维护的 Microsoft Entra Agent ID（面向 AI agent 的专用身份体系）示例仓库。提供 sidecar 模式示例（agent 与 Entra SDK 认证 sidecar 部署，含本地 LLM 与 AWS Bedrock 两种版本）、PowerShell/bash 脚本用于在租户中创建 Blueprint、Agent Identity 与客户端 SPA、部署到 Azure Container Apps 的方案，以及 n8n 平台在 Azure 上的端到端集成部署。Azure 部署教程附带 .claude/skills 技能，可配合 Claude Code 与 GitHub Copilot Chat 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- sidecar 模式示例：本地 LLM（Ollama 离线）与 AWS Bedrock（Claude）两种版本
- 脚本在租户中创建 Blueprint、Agent Identity 与客户端 SPA
- 支持部署到 Azure Container Apps（App Service 与 AKS 待提供）
- n8n 平台在 Azure Container Apps 上的端到端集成部署

## 适用场景

- 为自己的 AI agent 接入 Entra Agent ID 身份体系
- 通过脚本在租户中批量创建 agent 身份对象
- 参考 sidecar 模式将认证与 agent 解耦部署

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Runnable samples for **Microsoft Entra Agent ID** — Entra's purpose-built identity for AI agents.
> L9: |`sidecar/`|Sidecar-pattern samples (agent + Entra SDK auth sidecar) with local-LLM and AWS Bedrock editions|

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/entra-agentid-samples 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 16
    line [13, 14, 15, 15]
```

2026-10-18 13 → 2026-10-31 15（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `450bf1f63239` · [字段定义](../../DATASET.md)*
