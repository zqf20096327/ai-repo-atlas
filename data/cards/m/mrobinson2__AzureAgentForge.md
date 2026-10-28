# mrobinson2/AzureAgentForge

⭐ 24 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/mrobinson2/AzureAgentForge) · 个人维护

**自托管多 Agent 平台的 Azure 部署基座：编排+运行时+记忆+成本治理**

将 PaperClip（编排与任务/工单 UI）、Hermes（agent 执行循环）、Honcho（自托管记忆）三个开源工具整合为一套可部署栈，外围加 Terraform 部署的 Azure 基础设施（Container Apps、PostgreSQL+pgvector、Key Vault、集中日志）、OpenAI 兼容的模型路由（预算、降级、封顶、成本归因）、人工审批门与危险操作防护。可在本地或自有 Azure 订阅运行，无强制厂商控制平面。文档列出各组件成熟度与未完成事项，实际部署测得 cost-optimized 配置约 83 美元/月基础设施成本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型路由统一执行预算上限、降级与封顶，按调用方归因成本
- 记忆存于自有 PostgreSQL，可选记忆治理（准入控制与信任评分）
- Terraform 一键部署 Azure 基础设施，含销毁感知的人工审批门
- 自托管优先与全 Azure 两种部署拓扑，给出实测成本画像

## 适用场景

- 在自有 Azure 订阅里运行带预算和审批控制的多 agent 团队
- 给 agent 配置私有记忆、工具权限与审计追踪
- 需要可反复拆建、成本可控的长期运行 agent 工作流

## 场景标签

`模型网关` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L42: AzureAgentForge does not invent another orchestration engine, agent runtime, or memory store. It integrates three p
> L48: Around those three it adds Terraform for the Azure foundation, PostgreSQL with pgvector, Key Vault, Foundry-first m

## 星数曲线

```mermaid
xychart-beta
    title "mrobinson2/AzureAgentForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `be29a6423751` · [字段定义](../../DATASET.md)*
