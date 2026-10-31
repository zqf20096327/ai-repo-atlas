# frostlogic-ab/agent-forge

⭐ 15 · TypeScript · MIT · 推送 2026-06-24 · [GitHub](https://github.com/frostlogic-ab/agent-forge) · 组织维护

**TypeScript AI agent 编排框架：构建、组队与运行 agent**

面向 TypeScript 开发者的 AI agent 框架：以装饰器（@agent/@llmProvider/@tool 等）定义 agent，支持 LLM 接入、工具系统（内置/自定义/MCP）、带管理者 agent 的层级团队、工作流串联、A2A 远程 agent 服务、基于 ChromaDB 的 RAG 检索（支持 .txt/.md/.json）、插件系统（多种生命周期钩子）与运行时间线 HTML 可视化。需 Node.js、启用 experimentalDecorators 并配置 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 装饰器方式定义 agent 配置、LLM provider 与工具
- 层级团队（管理者委派任务）与多步工作流
- A2A 远程 agent 服务端/客户端与 MCP 工具集成
- 基于 ChromaDB 的 RAG 能力（文档分块与语义检索）
- 插件系统覆盖框架/agent/LLM/工具/工作流生命周期钩子

## 适用场景

- 构建多 agent 协作的层级团队处理复杂任务
- 把 agent 暴露为 A2A 远程服务或接入远程 agent
- 为 agent 挂载自有知识库实现 RAG 问答
- 通过插件实现日志、监控、安全等横切能力

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L7: Agent Forge is a TypeScript framework for building, orchestrating, and running advanced AI agents and agent teams. I
> L390: - `@llmProvider(provider, config)`: Set LLM provider for a class.

## 星数曲线

```mermaid
xychart-beta
    title "frostlogic-ab/agent-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `87542a557b1c` · [字段定义](../../DATASET.md)*
