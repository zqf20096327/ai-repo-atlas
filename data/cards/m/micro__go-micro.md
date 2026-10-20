# micro/go-micro

⭐ — · [GitHub]() · 组织维护

**Go 分布式系统开发框架，含 Agent 与工作流支持**

面向 Go 语言的分布式系统开发框架，提供 RPC（含流式）、服务发现、消息、存储与配置五类核心能力，每个组件以 Go 接口加默认实现的方式组织，可替换。在服务层之上提供 Agents（模型、对话历史、工具与 agent 执行）与 Workflows（有序步骤、重试、检查点），agent 将服务作为工具调用。通过 go get 安装，附 quickstart、services 与 agent 指南文档，采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.8 天,年发版 58,186 位贡献者
- 涨星:近 1 天 **+0**(自 20261016 起算)

## 能力要点

- 提供 RPC（含流式）、服务发现、消息、存储与配置
- Agents：模型、对话历史、工具与 agent 执行
- Workflows：有序步骤、重试与检查点
- 组件均为可替换默认实现的 Go 接口

## 适用场景

- 用 Go 构建微服务/分布式系统
- 开发以服务为工具的 AI Agent
- 编排带重试与检查点的多步工作流

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: Go Micro is a Go framework for distributed systems development.
> L6: Agents use services as tools; workflows coordinate service calls and agent tasks.
> L12: - **Agents:** models, conversation history, tools, and agent execution.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `c89bb1e51837` · [字段定义](../../DATASET.md)*
