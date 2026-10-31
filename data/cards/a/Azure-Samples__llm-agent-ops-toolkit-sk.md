# Azure-Samples/llm-agent-ops-toolkit-sk

⭐ 19 · Python · MIT · 推送 2026-04-01 · [GitHub](https://github.com/Azure-Samples/llm-agent-ops-toolkit-sk) · 组织维护

**基于 Semantic Kernel 的 LLM Agent 应用开发与运维脚手架**

微软 Azure-Samples 提供的 LLMAgentOps Toolkit：以 Semantic Kernel（Python）构建 LLM Agent 应用的基础代码结构，内含示例 MySql Copilot，采用 StateFlow（FSM 驱动的 LLM 工作流）做群聊选路与终止。代码分为 core（Agent 实现、群聊、代码执行 Agent）与 ops（OpenTelemetry 可观测性、MySql 交互、FastAPI REST 应用、Dockerfile）两部分，配套 GitHub Actions 的 CI/CE/CD/CS 流水线，支持 LLM as Judge 与人工评测。部署依赖 Azure AI Foundry、Azure OpenAI、Azure Web App 等服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- core/ops 分层结构：Agent 核心 + 运维（可观测性/部署）代码
- StateFlow（FSM）驱动的群聊选择与终止逻辑
- GitHub Actions 提供 CI/CE/CD/CS 四类流水线
- LLM as Judge 与人工评测的实验与评估流程

## 适用场景

- 作为 LLM Agent 应用的起点，替换示例实现自己的 Agent 方案
- 在 Dev Containers 中实验并评测 Agent 方案后部署到 Azure
- 为 Agent 应用接入持续评测与安全检查流水线

## 场景标签

`Agent 框架` `LLM 可观测性` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: `LLMAgentOps` Toolkit is repository that contains basic structure of LLM Agent based application built on top of the
> L16:  - `Agent Architecture`: Designing the agent architecture for the LLM Agent based solution. For this sample we have

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/llm-agent-ops-toolkit-sk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `84f7bee49b6f` · [字段定义](../../DATASET.md)*
