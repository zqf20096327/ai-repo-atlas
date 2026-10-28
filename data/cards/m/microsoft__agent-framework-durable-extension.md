# microsoft/agent-framework-durable-extension

⭐ 24 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/agent-framework-durable-extension) · 组织维护

**为 Microsoft Agent Framework 提供 Durable Task 扩展的仓库**

微软 Agent Framework 的持久化任务扩展源码仓库，覆盖 .NET 与 Python 两个语言栈：提供 durable agents 与 durable workflows（控制台/容器/AKS 自托管）、Azure Functions 托管（.NET isolated worker 与 Python v2），以及测试、示例与包构建元数据。通过 NuGet 与 PyPI 的 prerelease 包安装，依赖 Durable Task Scheduler、Azurite、Redis 等本地基础设施运行集成测试。完整 Agent Framework 本体在 microsoft/agent-framework 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .NET 与 Python 双语言栈的 durable agents/workflows 扩展
- 支持自托管（console/容器/AKS）与 Azure Functions 两种托管模型
- NuGet（Microsoft.Agents.AI.DurableTask 等）与 PyPI（agent-framework-durabletask 等）发包
- 包含单元/集成测试、示例与 CI 工作流

## 适用场景

- 为 Agent Framework 构建的 agent 增加持久化工作流能力
- 在 Azure Functions 上托管 durable agents
- 查阅 durable 扩展的示例与测试了解用法

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repository contains the Durable Task extensions for Microsoft Agent Framework across .NET and Python.
> L9: - Python Durable Task integration for Microsoft Agent Framework.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/agent-framework-durable-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5af46c080d69` · [字段定义](../../DATASET.md)*
