# tripolskypetr/agent-swarm-kit

⭐ 39 · TypeScript · MIT · 推送 2026-07-18 · [GitHub](https://github.com/tripolskypetr/agent-swarm-kit) · [官网](https://agent-swarm.github.io/) · 个人维护

**构建多智能体编排系统的 TypeScript 库，面向开发者**

TypeScript 多智能体编排库，不绑定特定框架：通过 addAgent/addSwarm/session 等 API 组合多个 LLM agent，支持单一聊天中混用多种模型（如 OpenAI、Grok、Claude），agent 间通过工具调用切换并共享 25 条轮换消息历史。提供单元测试框架（可覆盖工具与 agent）、MCP 远程服务器连接、Redis 状态与 RAG 存储集成、类 POSIX fork 的后台会话、结构化 JSON 输出校验及无效输出的自动重试。以 npm 包分发，附约 10 个演示工程。

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

- agent 间工具调用导航与共享轮换消息历史
- 含工具/agent 覆盖能力的单元测试框架
- Redis 持久化状态、RAG 向量检索与聊天历史
- 结构化 JSON 输出 schema 校验与自动重试

## 适用场景

- 搭建客服分诊→销售/退款的多角色 agent 工作流
- 在同一聊天中编排多个不同模型的 agent 协作
- 为多智能体系统编写可隔离运行的单元测试

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **A lightweight TypeScript library for building orchestrated, framework-agnostic multi-agent AI systems.**
> L59: The feature of this library is dependency inversion for agents injection. The agents are being lazy loaded during r
> L70: - 🤝 **Agent Orchestration**: Seamlessly switch between agents (e.g., triage → sales) with a single tool call. 🔄

## 星数曲线

```mermaid
xychart-beta
    title "tripolskypetr/agent-swarm-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cee74c243f76` · [字段定义](../../DATASET.md)*
