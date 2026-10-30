# ORNL/flowcept

⭐ 40 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/ORNL/flowcept) · 组织维护

**分布式科学与 AI 工作流的运行时溯源与数据观测系统**

面向 ML 训练、agentic 工作流、HPC 作业与边缘到云流水线，通过装饰器/上下文管理器或适配器（PyTorch、Dask、MLflow、TensorBoard 等）捕获任务输入输出、耗时、资源消耗与产物血缘。记录可从本地 JSONL 起步，经 Redis/RabbitMQ/Kafka/Mofka 消息队列流式传输，落库 MongoDB/LMDB 供查询。提供 Web UI、Python API/CLI/REST 查询、可导出 Markdown/PDF 的工作流卡片，以及基于 LangChain 的 Flowcept Agent 用自然语言查询溯源，并可作为 MCP server 接入外部助手。由橡树岭国家实验室（ORNL）以 MIT 许可开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 装饰器/上下文管理器/适配器多种捕获方式，含 PyTorch、Dask、MLflow、TensorBoard
- JSONL→MQ 流式→MongoDB/LMDB 分级存储，支持离线与在线分布式运行
- Flowcept Agent 以自然语言查询溯源，支持 Web 聊天与 MCP server 两种模式
- 生成可复现用途的工作流卡片（Markdown/PDF），遵循 W3C PROV 模型

## 适用场景

- 记录分布式 ML 训练或 HPC 作业的运行时溯源与资源消耗
- 追踪 agentic 工作流中 agent/tool 执行、LLM 调用与数据血缘
- 实验复现与评审时导出结构化的工作流卡片
- 通过对话式 Agent 查询仍在运行中的工作流数据

## 场景标签

`LLM 可观测性` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L35: Flowcept is a lightweight runtime provenance data management and data observability system for AI, scientific, and 
> L59: - **Plugin-friendly capture**: instrument native code or use adapters, including PyTorch, Dask, MLflow, TensorBoard
> L61: - **Agentic workflow lineage**: capture agent/tool execution, LLM usage, prompts, responses, and runtime provenance

## 星数曲线

```mermaid
xychart-beta
    title "ORNL/flowcept 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-30 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `50532bdf2fc2` · [字段定义](../../DATASET.md)*
