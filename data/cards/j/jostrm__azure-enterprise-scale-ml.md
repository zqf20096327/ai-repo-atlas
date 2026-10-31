# jostrm/azure-enterprise-scale-ml

⭐ 53 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/jostrm/azure-enterprise-scale-ml) · 个人维护

**面向企业的 Azure AI 应用落地区 IaC 方案：自动部署 GenAI/ML 全套环境**

Enterprise Scale AI Factory 是部署在 Azure 上的企业级 AI 落地区（landing zone）基础设施方案：通过 BICEP 与 GitHub Actions/Azure DevOps 流水线，自动化开通 AI Foundry、Azure OpenAI、Azure Machine Learning、AI Search、Databricks 等资源，构建 Dev/Stage/Prod 多环境隔离、私有网络的 End-2-End agentic 架构。对齐微软 Well-Architected Framework，附 DataOps/MLOps/GenAIOps 模板，支持约 34 种 Azure 服务按 feature flag 增减，提供配置向导与自托管 Runner 脚本。自 2019 年设计使用，限定 Azure 云环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BICEP + GitHub Actions/Azure DevOps 自动化开通多环境隔离的 AI 落地区
- AI Foundry/AzureML/AI Search/Databricks 等 GenAI+ML 基线架构约 10 分钟部署
- 约 34 种 Azure 服务可按 feature flag 增减并增量重建
- DataOps/MLOps/GenAIOps 模板与 WAF 对齐的私有网络设计

## 适用场景

- 企业将 AI 项目从 PoC 推进到生产就绪的隔离环境
- 多团队在 Azure 上按订阅划分各自独立的 AI 工作区
- 自动化搭建带私有网络的 GenAI + ML 端到端架构

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: It is an enterprise scale solution for deploying AI Foundry with related services to create End-2-End agentic scenar
> L9: This `Enterprise Scale AI Factory` repo is a plug and play solution that automates the provisioning, deployment, and
> L12: The deployed features follow Microsoft's Well-Architected Framework WAF to establish an isolated infrastructure int

## 星数曲线

```mermaid
xychart-beta
    title "jostrm/azure-enterprise-scale-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-31 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d20b0a34f6a6` · [字段定义](../../DATASET.md)*
