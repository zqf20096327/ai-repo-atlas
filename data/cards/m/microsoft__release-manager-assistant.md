# microsoft/release-manager-assistant

⭐ 28 · Python · MIT · 推送 2026-02-14 · [GitHub](https://github.com/microsoft/release-manager-assistant) · 组织维护

**微软出品的 AI 发布管理助手：多智能体协同辅助软件发布决策**

微软开源的解决方案加速器，面向企业发布经理：通过多智能体编排（Planner、JIRA、Azure DevOps、可视化、Fallback）集成 JIRA 与 Azure DevOps，提供依赖映射、发布健康评估、就绪度报告与交互式图表等实时决策支持。基于 Azure AI Foundry、Microsoft Agent Framework 与 MCP 协议构建，使用 Redis 做会话管理与消息队列。当前仅支持自带 AI（BYOAI）场景，需 Azure 订阅、Azure OpenAI 与 AI Foundry 访问权限；部署到 Azure 订阅或使用 Codespaces/Dev Containers，需 Python 3.12、Node.js 20+ 与 Docker 运行时。附合成数据的 MCP Server 可在无真实 JIRA/DevOps 环境下试用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Planner Agent 按用户意图路由到 JIRA/Azure DevOps/可视化/Fallback 等智能体
- 通过 MCP 集成 Azure DevOps（工作项、构建、PR、迭代等），支持 Azure CLI 与 PAT 认证
- 内置合成数据的 JIRA/Azure DevOps MCP Server，可脱离真实环境运行
- 发布时间线分析与经用户确认的安全更新机制

## 适用场景

- 发布经理跨 JIRA 与 Azure DevOps 查询发布健康与依赖状况
- 自动汇总跨系统数据生成发布就绪度报告
- 通过对话让智能体创建/更新工作项并生成可视化图表

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: The **Release Manager Assistant (RMA)** is a solution accelerator designed to augment release managers with AI-driv
> L19: - **Multi-Agent Orchestration System**: Intelligent planning agent that coordinates between:
> L25: - **Azure AI Foundry Service**: Cloud-based agents with integrated tools (Code Interpreter, SharePoint)

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/release-manager-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `55403e64ee17` · [字段定义](../../DATASET.md)*
