# datarobot-community/datarobot-agent-templates

⭐ 19 · Python · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/datarobot-community/datarobot-agent-templates) · [官网](https://www.datarobot.com) · 组织维护

**DataRobot 多智能体工作流模板集，用于搭建与部署 agentic 应用**

由 DataRobot 社区维护的智能体工作流模板仓库，提供 CrewAI、LangGraph、LlamaIndex、NeMo Agent Toolkit 四种框架模板及一个可自定义的通用基础模板，每个模板内置含两个 Agent、三个任务的示例工作流。支持本地开发测试与经 Pulumi 部署到 DataRobot 生产环境，部署与本地测试均需 DataRobot API token 与端点，安装仅兼容 macOS/Linux。仓库已声明废弃，指引转向新的 DataRobot Agent Application 模板。

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

- 覆盖 CrewAI/LangGraph/LlamaIndex/NeMo Agent Toolkit 四种框架模板
- task start 辅助脚本完成环境配置与模板选择
- 通过 task deploy（Pulumi）部署到 DataRobot 生产环境
- 本地测试与 LLM 通信均依赖 DataRobot 连接

## 适用场景

- 基于熟悉的多智能体框架快速搭建 DataRobot 工作流
- 本地开发并测试 agentic 工作流后部署到生产
- 参考通用基础模板定制自有框架的工作流

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L23: This repository provides ready-to-use templates for building and deploying agentic workflows with multi-agent frame
> L34: This repository includes templates for four popular agent frameworks and a generic base template that can be adapte

## 星数曲线

```mermaid
xychart-beta
    title "datarobot-community/datarobot-agent-templates 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1dea42795320` · [字段定义](../../DATASET.md)*
