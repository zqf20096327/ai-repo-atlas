# Altaflux/agent-mimir

⭐ 112 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/Altaflux/agent-mimir) · 个人维护

**基于 LangchainJS 的 LLM agent 管理器：Discord/命令行客户端**

面向终端用户的命令行与 Discord 聊天客户端及 LLM agent 管理器，基于 LangchainJS 构建，可使用任何与其兼容的模型与工具。提供多步任务系统（参考 Auto-GPT/BabyAGI 的计划-迭代-复查模式）、自定义 agent 配置（人格/职业/模型）、MCP 服务器接入、Python 代码解释器、网页浏览、搜索与计算器插件。通过 git clone 源码安装，需 NodeJS 18+ 与 OpenAI API key；提示词当前在 GPT-4/GPT-3.5 上调优。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 LangchainJS，兼容其全部工具与模型
- Auto-GPT/BabyAGI 式多步计划任务系统
- 支持 Claude MCP 服务器（Tools/Prompts/Resources）
- 提供代码解释器、网页浏览、搜索、计算器等插件

## 适用场景

- 在 Discord 或命令行中与自定义人格的 AI agent 对话
- 让 agent 执行多步骤任务并调用工具
- 通过 MCP 服务器扩展 agent 可用的工具与资源

## 场景标签

`聊天机器人` `AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agent Mimir is a command line and Discord chat client "agent" manager for LLM's like Chat-GPT that provides the mode
> L7: Agent Mimir is based on LangchainJS, every tool or LLM that works on Langchain should also work with Mimir. The prom
> L9: The tasking system is based on Auto-GPT and BabyAGI where the agent needs to come up with a plan, iterate over its s

## 星数曲线

```mermaid
xychart-beta
    title "Altaflux/agent-mimir 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-26 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `416ef416658e` · [字段定义](../../DATASET.md)*
