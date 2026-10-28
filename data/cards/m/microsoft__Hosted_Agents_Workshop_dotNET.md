# microsoft/Hosted_Agents_Workshop_dotNET

⭐ 25 · Bicep · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/Hosted_Agents_Workshop_dotNET) · 组织维护

**微软官方 .NET 10 实操工坊：构建并部署 Foundry 托管 Agent**

面向初学者的动手教程仓库（Lab 0–5），用 .NET 10 构建一个 Microsoft Foundry Hosted Agent（场景为托管 Agent 就绪教练），实现 OpenAI Responses 兼容的 /responses 端点（端口 8088），业务逻辑用三个确定性本地工具。流程覆盖本地运行、Copilot 配置、GitHub Actions CI、azd ai agent 一键部署到 Azure（init→run→provision→deploy→invoke），以及 Blazor 聊天 UI 集成；保留手动 ACR+SDK 路线作为可选附录。需要 Azure 订阅与 Foundry 项目访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个递进式 Lab，命令可直接复制粘贴
- azd ai agent 单命令流程：脚手架→资源组→容器镜像→注册托管 Agent
- 三个确定性本地工具（无需 LLM 调用）+ /responses 端点本地可验证
- GitHub Actions CI 与 ACR 云构建（az acr build）部署路径

## 适用场景

- 初次接触 Foundry 托管 Agent 的开发者按 Lab 顺序学习全流程
- 团队评估 prompt agent 与 hosted agent 的选型问题
- 把本地验证过的 agent 经 CI 部署到 Azure 并接入 Blazor 聊天 UI

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository is a beginner-friendly workshop for building a Microsoft Foundry Hosted Agent with .NET 10.
> L5: If you are new to Microsoft Foundry hosted agents, follow the labs in order from Lab 0 to Lab 5. Each lab builds on 
> L15: By the end of the workshop, you will have worked through the full development path for a simple hosted agent:

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Hosted_Agents_Workshop_dotNET 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e68d1c597d63` · [字段定义](../../DATASET.md)*
