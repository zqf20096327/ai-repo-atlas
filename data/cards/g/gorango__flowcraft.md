# gorango/flowcraft

⭐ 212 · TypeScript · MIT · 推送 2026-07-02 · [GitHub](https://github.com/gorango/flowcraft) · [官网](http://flowcraft.js.org/) · 个人维护

**轻量零依赖的 TypeScript 工作流引擎，编排业务流程与 AI agent**

以 npm 包形式提供的工作流编排库：通过 Fluent API、声明式 JSON 蓝图或 @flow/@step 编译器三种方式定义带节点与边的工作流，覆盖业务流程、数据管道、ETL 与 AI agent 场景。内置重试、回退、超时与取消等容错机制，支持批次、循环、子流程与 HITL 模式；同一蓝图可在内存运行或经 BullMQ、Kafka、AWS 等官方适配器扩展到分布式执行。附带蓝图静态检查、环检测、Mermaid 图生成工具，以及供 LLM 调用的 @flowcraft/tools。

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

- 零依赖、类型安全的 TypeScript 工作流引擎，三种编排方式（Fluent/声明式/编译器）
- 内置重试、回退、超时、取消与 HITL 等模式
- 同一蓝图可从内存运行扩展到 BullMQ/Kafka/AWS/GCP/Azure 等分布式后端
- 提供 @flowcraft/tools 让 LLM 以 Zod 工具形式组装与监控工作流

## 适用场景

- 编排多步骤业务流程或 ETL/数据管道
- 构建可重试、可回退的 AI agent 工作流
- 将工作流作为工具交给 LLM 组合执行与监控

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Codecov
> L75: Flowcraft includes tools to help you validate, visualize, and integrate workflows with LLMs.
> L80: - **Agent Tools**: Use `@flowcraft/tools` to give LLMs Zod-based tools for composing, running, and monitoring workf

## 星数曲线

```mermaid
xychart-beta
    title "gorango/flowcraft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 211 --> 213
    line [212, 212]
```

2026-10-18 212 → 2026-10-26 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7dd6af8ebd46` · [字段定义](../../DATASET.md)*
