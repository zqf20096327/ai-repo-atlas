# Aurite-ai/aurite-agents

⭐ 17 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/Aurite-ai/aurite-agents) · [官网](https://aurite-ai.github.io/aurite-agents) · 组织维护

**配置驱动的 Python AI agent 构建与编排框架**

Aurite Agents 是一个 Python 框架，用于构建、测试和运行 AI agent。通过 Workspace→Project 层级配置组织组件，以 JSON/YAML 声明 agent、LLM、MCP 服务器与工作流；经 Model Context Protocol (MCP) 接入外部工具与资源，支持 linear_workflows 顺序链与 custom_workflows 自定义 Python 编排。交互方式包括 CLI、两个 TUI、FastAPI REST API 与 React Web 界面（Aurite Studio），另有 TypeScript API 客户端包。LLM 提供商经 LiteLLM 接入 OpenAI、Anthropic、Google 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Workspace→Project 层级配置，JSON/YAML 声明式定义 agent/LLM/工具/工作流
- 经 MCP 协议接入本地与远程工具服务器
- linear_workflows 顺序编排与 custom_workflows 自定义 Python 编排
- 提供 CLI、TUI、FastAPI REST API 与 React Web 界面（Aurite Studio）

## 适用场景

- 构建和编排多 agent 工作流应用
- 通过 MCP 接入外部工具自动化多步骤任务
- 以 REST API 或 Web 界面可视化管理和监控 agent 执行

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A Python framework for building, testing, and running AI agents.
> L9: **Aurite Agents** is a powerful, configuration-driven framework designed for building and orchestrating sophisticate
> L19: - **Flexible Orchestration:** Chain agents together in `linear_workflows` for sequential tasks or write custom Pyth

## 星数曲线

```mermaid
xychart-beta
    title "Aurite-ai/aurite-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7bda94171b5a` · [字段定义](../../DATASET.md)*
