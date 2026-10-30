# redouble-ai/nucleo

⭐ 18 · Java · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/redouble-ai/nucleo) · [官网](https://docs.redouble.ai) · 组织维护

**嵌入 Java 应用进程内运行 AI agent 的运行时**

面向 Java 开发者的 in-process agent 运行时：以 Maven Central 构件（nucleo-core 及各 provider 模块）嵌入应用，agent 与业务代码运行在同一 JVM、同一安全边界内。核心机制包括 Tool（类型化输入输出）、Thinker/Doer（选择与执行工具的 agent）、Scope/Guardrail（代码级边界）、Artifact（跨 agent 字节一致数据）、基于虚拟线程的 JobDispatcher（准入与限流、单 JVM 内数百 agent），并发布全量事件流。提供 Spring Boot starter 与 Quarkus 集成、MCP 连接器，及文献检索（PubMed/PMC/bioRxiv）与专利检索（EPO/USPTO）扩展。要求 Java 25（LTS），不支持旧版 JDK；文档位于 docs.redouble.ai。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tool/Thinker/Doer 抽象：类型化工具调用与多步任务 agent
- Scope/Guardrail 在代码中设定 agent 边界
- 虚拟线程上的 JobDispatcher，支持准入、限流与费用上限
- 发布每个 job、工具调用与模型调用的事件流

## 适用场景

- 把模型判断嵌入现有 Java 业务进程，不外发给外部运行时
- 在 Spring Boot/Quarkus 应用内运行与治理大量 agent
- 在配额与费用上限内并行运行多模型工作负载

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Nucleo is a runtime for AI agents that live inside your Java application: in-stack,
> L11: Authoring frameworks give an engineer a way to write an agent. Nucleo is the layer those
> L126: Nucleo is Apache-2.0 and complete on its own: everything above ships here and works with

## 星数曲线

```mermaid
xychart-beta
    title "redouble-ai/nucleo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `39021f61dca6` · [字段定义](../../DATASET.md)*
