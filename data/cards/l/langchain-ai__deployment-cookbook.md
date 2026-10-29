# langchain-ai/deployment-cookbook

⭐ 19 · TypeScript · MIT · 推送 2026-10-01 · [GitHub](https://github.com/langchain-ai/deployment-cookbook) · [官网](https://docs.langchain.com/langsmith/deployment) · 组织维护

**LangChain agent 生产部署参考实现集（多平台全栈示例）**

由 LangChain 官方维护的部署示例集：每个目录是一个自包含的全栈聊天应用（流式 UI、子 agent、线程历史），基于同一 Agent Streaming Protocol，分别部署到 LangSmith、Cloudflare Workers、Next.js/Vercel、SvelteKit、Deno、Nuxt 等平台。统一架构包含 agent 运行时（LangGraph 或 deepagents，配 checkpointer）、实现 /api/threads 端点的协议服务器、会话与运行管理、基于框架绑定（React/Vue/Svelte/Angular）的聊天前端。所有示例共用同一演示 agent（coordinator 委派 researcher 与 math-whiz 子 agent，工具为 mock）。各目录自带 README、环境配置与部署说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 Agent Streaming Protocol，跨 6 个托管平台的可对比全栈示例
- 四个组成部分的参考架构：agent 运行时/协议服务器/会话管理/前端
- 生产持久化选项：Redis、Postgres、SQLite 或平台存储替换内存 checkpointer
- LangSmith 两种部署路径：自持 LangGraph Agent Server 与 Managed Deep Agent（工具转为 MCP 服务器）

## 适用场景

- 需要上线 agent 产品的团队选取匹配托管环境的起步模板
- 学习 Agent Streaming Protocol 服务端端点与 SSE 流式实现
- 比较不同平台（Cloudflare/Next.js/Deno/Nuxt 等）上部署 agent 的方式

## 场景标签

 · 领域:LLM 基础设施/agent 部署

## 证据(README 行号)

> L3: Reference implementations for running LangChain agents in production. Each example is a full-stack chat app — stream
> L13: The agent itself, typically a LangGraph graph or `deepagents` coordinator, with tools, optional subagents, and midd
> L102: All examples share the same demo agent: a coordinator that delegates to `researcher` and `math-whiz` subagents wit

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/deployment-cookbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9a731b544ca4` · [字段定义](../../DATASET.md)*
