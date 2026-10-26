# langchain-ai/async-deep-agents

⭐ 31 · Python · 推送 2026-10-19 · [GitHub](https://github.com/langchain-ai/async-deep-agents) · 组织维护

**LangSmith 上异步子代理编排的参考架构：监督者后台启动子代理**

基于 Deep Agents 与 LangGraph SDK 的参考实现：监督者代理通过 AsyncSubAgentMiddleware 提供五个工具，把专门化子代理（如 Researcher、Coder）作为后台任务启动，立即返回任务 ID，随后可查询进度、发送中途指令、取消任务。任务元数据存储于独立状态通道以在上下文压缩后保留。提供 Python 与 TypeScript 示例，经 ASGI（同部署进程内调用）或 HTTP（远程部署，读取 LANGSMITH_API_KEY）两种传输方式，可单命令部署到 LangSmith Deployments。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AsyncSubAgentMiddleware 向监督者 LLM 暴露 5 个工具（launch/check/update/cancel/list）
- 任务元数据存于专用状态通道，在上下文压缩后仍可恢复
- 支持 ASGI 进程内与 HTTP 远程两种传输，可同部署或拆分部署
- 提供 Python 与 TypeScript 两种语言的可用示例

## 适用场景

- 让长时间运行的研究/代码任务在后台执行，主对话不被阻塞
- 并行运行多个子代理处理可拆分的请求
- 在任务执行中途向子代理追加新指令或取消任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A reference implementation for non-blocking, background agent orchestration on LangSmith Deployments using Deep Agen
> L22: This architecture is built on LangSmith Deployments thread and run management APIs. Each background job is a standa
> L37: 1. **Supervisor** (`deep_agent`) -- The user-facing agent. Uses `AsyncSubAgentMiddleware` to manage background jobs

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/async-deep-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d0401333a271` · [字段定义](../../DATASET.md)*
