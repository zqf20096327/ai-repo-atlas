# moseleydev/swarm-kit

⭐ 14 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/moseleydev/swarm-kit) · [官网](https://moseleydev.github.io/swarm-kit/) · 个人维护

**Python 极简多智能体编排框架：handoff、规划模式与共享状态**

基于 LiteLLM 的 Python 多智能体编排框架，提供两种执行模式：unsupervised（智能体间自主 handoff）与 supervised（planner LLM 按固定序列调度智能体）。核心机制包括普通 Python 函数即工具（自动从签名与 docstring 生成 JSON schema）、共享全局状态字典、require_approval 人工审批、save/load 持久化钩子（可接 Redis/Postgres/SQLite）、async 支持（可安全用于 FastAPI）及 Agent Studio 实时本地仪表盘。要求 Python 3.10+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 LiteLLM 支持 OpenAI/Anthropic/Gemini/Ollama/Azure/Bedrock 等 100+ 提供商，每个智能体可用不同模型
- unsupervised 自主 handoff 与 supervised planner 两种编排模式
- 普通 Python 函数即工具，自动生成 JSON schema，支持 sync/async
- require_approval 人工审批、共享状态与数据库持久化钩子

## 适用场景

- 构建多智能体协作完成分流、退款等业务流程的应用
- 在 FastAPI 等 asyncio 服务中以异步方式运行智能体群
- 需要人工审批敏感工具调用的 agent 工作流
- 通过 Agent Studio 仪表盘观察 handoff、工具调用与状态变化

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A minimalist, state-aware multi-agent orchestration framework for Python.**
> L15: Swarm Kit sits between simple chat scripts and heavyweight agent frameworks. It provides
> L33: - **Any model.** Built on LiteLLM, so OpenAI,

## 星数曲线

```mermaid
xychart-beta
    title "moseleydev/swarm-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `68926d45120d` · [字段定义](../../DATASET.md)*
