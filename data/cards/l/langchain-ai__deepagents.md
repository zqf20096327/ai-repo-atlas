# langchain-ai/deepagents

⭐ 30,420 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/langchain-ai/deepagents) · [官网](https://docs.langchain.com/deepagents) · 组织维护

**给开发者的开箱即用 agent harness，构建长程多步 agent**

LangChain 团队开源的 agent harness，基于 LangGraph 构建，提供子代理、可插拔文件系统后端、上下文管理与持久化记忆等默认组件，每个部件可覆盖或替换而不需 fork。支持任何具备工具调用能力的模型（前沿 API、开源权重或本地模型），随流式输出、检查点持久化与经 LangSmith 的追踪评估能力一同提供。提供 Python 与 JavaScript/TypeScript 两个库版本，另有终端编码代理 Deep Agents Code，通过 curl 脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.0 天,年发版 100,160 位贡献者
- 涨星:近 1 天 **+39**(自 20261016 起算)
- 平台:WINDOWS · 协议:MCP / OLLAMA

## 能力要点

- 子代理机制：将任务委派给具有独立上下文窗口的代理
- 可插拔文件系统（本地/沙箱/远程后端）与 shell 执行
- 上下文管理：摘要长对话并将工具输出落盘
- 人在回路审批、按需加载的 Skills 与任意 MCP 服务器接入

## 适用场景

- 构建需要长程规划与多步执行的生产级 agent
- 为 agent 配置子代理分工与隔离上下文
- 接入本地或开源权重模型运行 agent
- 在终端中使用预构建编码代理辅助编程

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L14: Deep Agents is an open source agent harness — an opinionated agent that runs out of the box. Extend, override, or r
> L20: - **Model-agnostic** — works with any LLM that supports tool calling: frontier, open-weight, or local
> L21: - **Production-ready** — built on LangGraph (streaming, persistence, checkpointing) with first-class tracing, evalu

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/deepagents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 30360 --> 30425
    line [30365, 30420, 30420]
```

2026-10-18 30,365 → 2026-10-21 30,420（+55）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `82b131261373` · [字段定义](../../DATASET.md)*
