# manthanguptaa/water

⭐ 338 · Python · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/manthanguptaa/water) · [官网](https://manthanguptaa.in/posts/water/) · 个人维护

**面向生产环境的 Python agent 基础设施框架**

Water 是一个 agent harness 框架，提供 AI agent 周边的基础设施而非 agent 本身：编排（Flow 模式）、多 agent 协作、工具调用、ReAct 循环、上下文管理与分层记忆、护栏校验、审批门、沙箱执行、韧性模式（熔断/限流/重试）、可观测性、评估（含 LLMJudge）、MCP/A2A/聊天适配器集成，以及 REST 服务器与 CLI。支持 OpenAI、Anthropic 等统一 LLM 接口，兼容 LangChain、CrewAI 等任意 agent 框架。以 pip 包 water-ai 提供，附 73 个可运行示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排、韧性、护栏、审批门、沙箱与可观测性等生产基础设施
- 统一接口接入 OpenAI/Anthropic 等多种 LLM，支持故障转移链与流式输出
- MCP/A2A 协议集成与 Slack/Discord/Telegram 聊天适配器
- cookbook 提供 73 个按类别组织的可运行示例

## 适用场景

- 为已有 agent 框架补齐生产级编排与可靠性基础设施
- 构建带审批门与沙箱的高风险 agent 工作流
- 将 agent 流程通过 REST、MCP 或聊天平台对外提供服务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: Water is an agent harness framework — it provides the infrastructure *around* your AI agents, not the agents themse
> L13: Works with any agent framework: LangChain, CrewAI, Agno, OpenAI, Anthropic, or your own custom agents.

## 星数曲线

```mermaid
xychart-beta
    title "manthanguptaa/water 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 337 --> 339
    line [338, 338]
```

2026-10-18 338 → 2026-10-23 338（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f280990f49f2` · [字段定义](../../DATASET.md)*
