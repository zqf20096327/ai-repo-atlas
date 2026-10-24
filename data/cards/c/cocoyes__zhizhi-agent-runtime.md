# cocoyes/zhizhi-agent-runtime

⭐ 180 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/cocoyes/zhizhi-agent-runtime) · [官网](https://deepyou.top) · 个人维护 · 中文 README

**Go 编写的模型无关 agent 执行运行时，覆盖规划、工具编排与恢复**

面向生产环境的 Go agent 运行时库：将普通 Go 函数转为带 JSON Schema 校验的类型化工具，通过模型规划器构建依赖图并调度并行批次、条件分支与证据绑定，失败后执行有界重规划。提供 MCP 集成（含 allow-list 与能力提供者模式）、副作用确认门与 ActionReceipt、检查点挂起恢复、重试/预算/超时等可靠性控制，以及 JSONL 追踪与 OpenTelemetry 可选集成。要求 Go 1.25+ 与任意 OpenAI 兼容端点，经 go get 安装，附 13 个示例。

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

- 类型化工具自动生成 JSON Schema 并做运行时输入输出校验
- 依赖图规划、并行批次、条件分支与有界重规划
- MCP 集成含能力提供者模式（大工具舰队按需连接）
- 副作用确认门、检查点版本化挂起恢复与可靠性预算控制

## 适用场景

- 在 Go 应用中构建多步骤、带工具调用的 agent 任务
- 通过 MCP 接入外部工具并做信任边界控制
- 对含写操作的 agent 流程做确认、挂起与恢复
- 以 JSONL/OTel 追踪 agent 执行全过程

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Production-grade Go runtime for agents that plan, act, recover, and remain auditable.
> L21: Zhizhi is a model-agnostic execution layer for real applications. It turns ordinary Go functions into validated too


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7e20068badb1` · [字段定义](../../DATASET.md)*
