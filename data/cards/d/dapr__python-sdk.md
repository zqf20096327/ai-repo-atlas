# dapr/python-sdk

⭐ 274 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/dapr/python-sdk) · [官网](https://docs.dapr.io/developing-applications/sdks/python/) · 组织维护

**Dapr 的 Python SDK：构建有状态 AI agent 与分布式应用的客户端库**

为 Dapr 分布式运行时提供的 Python SDK，实现 Virtual Actor 模型，包含客户端、配置、序列化器与 gRPC 自动生成客户端等包；以 extras 形式提供 FastAPI/Flask/gRPC 集成、Durable Workflow 编排、Databricks Lakeflow 流式 sink、LangGraph checkpoint 持久化与 Strands agent 会话管理等扩展。前置要求为安装 Dapr standalone 模式与 Python 3.10+，通过 pip 安装官方包，旧独立包已迁移为 extras（跳过迁移会触发 FutureWarning）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Virtual Actor 模型实现，可本地、容器或分布式环境运行
- LangGraph checkpoint 持久化与 Strands agent 会话管理扩展
- Durable workflow 编排与 Databricks Lakeflow 流式 sink 扩展
- 旧独立包已合并为 dapr 包 extras，提供迁移指引

## 适用场景

- 在 Python 微服务中接入 Dapr 的 actor、状态、发布订阅等构建块
- 为 LangGraph/Strands agent 应用提供 checkpoint 与会话持久化
- 编写 Dapr durable workflow 实现容错的长时间任务编排

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L14: Dapr is a portable, event-driven, serverless runtime for building distributed applications across cloud and edge.
> L32: * dapr.ext.langgraph: LangGraph checkpoint persistence — `pip install "dapr[langgraph]"`
> L33: * dapr.ext.strands: Strands agent session management — `pip install "dapr[strands]"`


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9391098b051a` · [字段定义](../../DATASET.md)*
