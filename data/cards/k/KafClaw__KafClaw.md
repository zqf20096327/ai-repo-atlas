# KafClaw/KafClaw

⭐ 21 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/KafClaw/KafClaw) · [官网](https://kafclaw.scalytics.io) · 组织维护

**Go 编写的基于 Kafka 的多智能体协调框架**

KafClaw 是用 Go 构建的 agent 协调框架，通过 Kafka 主题层级连接自主 AI agent：提供组内协作（心跳存活检测、任务委派、技能注册）、跨组层级编排（父子委派链、public/shared/private 安全区）、共享记忆（memory.shared 持久化、memory.context 带 TTL，可索引到 SQLite-vec/Qdrant 向量库供 RAG）。Go 运行时内含 LLM 抽象层（OpenAI、OpenRouter）、工具注册、SQLite 时间线库、策略引擎与调度器；轻量 agent 只需 Kafka 客户端与 JSON 信封模式，无 SDK 锁定。提供 standalone/group/full/headless 四种运行模式，需 Go 1.26+ 与 Kafka（组模式）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Kafka 类型化信封协议的 agent 通信与全链路观测
- 层级编排与安全分区（zones）实现跨组隔离与桥接
- 共享记忆可索引到本地向量库（SQLite-vec/Qdrant）供 RAG
- LLM 提供商抽象（OpenAI/OpenRouter），轻量 agent 无 SDK 依赖

## 适用场景

- 在 Kafka 集群上组建多 agent 协作与任务委派
- 跨语言/跨运行时的异构 agent 通过统一信封协议互联
- 为 agent 群体构建共享知识库与语义检索

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L38: KafClaw is an agent coordination framework built in Go. It connects autonomous AI agents through Kafka-based messag
> L113: - **Agent loop** with LLM provider abstraction (OpenAI, OpenRouter)

## 星数曲线

```mermaid
xychart-beta
    title "KafClaw/KafClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7d5183e3280c` · [字段定义](../../DATASET.md)*
