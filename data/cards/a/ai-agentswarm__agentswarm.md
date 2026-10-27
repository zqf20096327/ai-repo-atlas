# ai-agentswarm/agentswarm

⭐ 25 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/ai-agentswarm/agentswarm) · [官网](https://ai-agentswarm.github.io/agentswarm/) · 组织维护

**多智能体编排框架：以类型安全函数与共享存储构建 Agent**

Python 编写的自主智能体编排框架，将 Agent 定义为强类型异步函数（基于 Pydantic 与泛型），通过函数调用形成编排而非节点/边图。机制包括：每次调用子 Agent 从空白上下文开始（Tabula Rasa）以避免上下文污染；Agent 间通过共享 Key-Value Store（含 Gathering/Transformer/Merge 三类管理 Agent）交换数据引用而非原始文本；ReActAgent 引擎自动并行执行工具并聚合结果；MapReduceAgent 支持递归分解与动态克隆。计划支持 MCP 与 A2A 协议，可包装 LangChain 工具，Agent 可本地或远程（AWS/Google Cloud）执行。README 未给出安装命令。

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

- Agent 即强类型异步函数，输入输出运行时校验并由类型提示自动生成 LLM JSON schema
- Tabula Rasa 执行：子 Agent 从空白上下文开始，只接收所需输入
- 共享 Key-Value Store 模式，Agent 间仅交换 Key 引用
- MapReduceAgent 递归分解任务并动态实例化并行克隆

## 适用场景

- 构建需要递归与 Map-Reduce 分解的多 Agent 系统
- 避免子 Agent 继承父级全部对话历史导致的上下文污染
- 用共享存储在多 Agent 间传递与变换大规模数据

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A Recursive, Functional, and Type-Safe Framework for Autonomous AI Agents.**
> L11: Unlike chat-based frameworks (like AutoGen) or static graph frameworks (like LangGraph), AgentSwarm treats agents a
> L42: Every agent is a class inheriting from `BaseAgent[Input, Output]`. There are no "nodes" or "edges" to manually defi

## 星数曲线

```mermaid
xychart-beta
    title "ai-agentswarm/agentswarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4277b4e218bc` · [字段定义](../../DATASET.md)*
