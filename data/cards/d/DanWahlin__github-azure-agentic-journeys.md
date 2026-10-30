# DanWahlin/github-azure-agentic-journeys

⭐ 38 · MIT · 推送 2026-07-29 · [GitHub](https://github.com/DanWahlin/github-azure-agentic-journeys) · [官网](https://aka.ms/agentic-journeys) · 个人维护

**教开发者用 Copilot agent 与技能构建并部署应用到 Azure 的实践教程集**

一组自包含的“agentic journey”动手教程：开发者选定技术栈（Node.js/Python/.NET/Java），用 GitHub Copilot 等 agentic 编码工具从规格文档生成 API、数据库与前端，再由 agent 生成 Bicep 基础设施并部署到 Azure Static Web Apps、Container Apps、Functions 或 AKS，部分旅程接入 Microsoft Foundry 的 AI 搜索与聊天。包含 6 个旅程（WeatherView、Grafana、n8n、Superset、AIMarket、SmartTodo），并给出各旅程留存运行的月度费用估算与 azd down 清理步骤。面向想在 Azure 上采用 agentic AI 开发流程的开发者与团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 个自包含旅程，覆盖从规格到全栈应用与 OSS 应用部署
- 通过 Azure 插件（microsoft/azure-skills）接入 GitHub Copilot CLI/应用/IDE
- agent 生成 Bicep + azd 部署到 Static Web Apps/Container Apps/Functions/AKS
- 每个旅程附费用估算与清理命令（azd down --force --purge）

## 适用场景

- 学习用 AI agent 从规格生成代码并部署到 Azure
- 评估 agent 与 skills 如何融入团队开发流程
- 把 n8n、Grafana、Superset 等 OSS 应用快速部署到 Azure

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: What if you could go from idea to running in Azure and stay focused on your actual product the entire time? With ag
> L16: You pick a stack, write a spec, and hand it to your AI coding assistant, which scaffolds your API, database, and da
> L27: - Build an API, database, and frontend from a spec document using GitHub Copilot

## 星数曲线

```mermaid
xychart-beta
    title "DanWahlin/github-azure-agentic-journeys 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b8024a30da7e` · [字段定义](../../DATASET.md)*
