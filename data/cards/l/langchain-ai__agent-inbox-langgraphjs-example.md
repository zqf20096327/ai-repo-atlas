# langchain-ai/agent-inbox-langgraphjs-example

⭐ 24 · JavaScript · MIT · 推送 2026-07-15 · [GitHub](https://github.com/langchain-ai/agent-inbox-langgraphjs-example) · 组织维护

**LangGraph.js 上手 Agent Inbox 的最小示例仓库**

由 langchain-ai 维护的入门示例仓库，提供一段最简代码演示如何用 LangGraph.js 构建带人工中断（interrupt）的 agent 图，并接入 Agent Inbox（dev.agentinbox.ai）管理被中断的线程。流程为：克隆仓库、yarn 安装依赖、npx 启动 LangGraph Server，在 LangGraph Studio 中触发 humanNode 中断，再到 Agent Inbox 对中断项执行 Accept/Edit/Respond/Ignore 操作并恢复图执行。面向使用 LangGraph.js 的开发者。

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

- 提供 LangGraph.js 最小可运行示例代码
- 演示 humanNode 中断与 Agent Inbox 线程管理流程
- 在 Agent Inbox 中对中断项执行 Accept/Edit/Respond/Ignore 四种操作
- 操作后图恢复执行并返回操作类型与参数

## 适用场景

- 快速上手 Agent Inbox 与 LangGraph.js 的集成
- 学习 LangGraph 人工中断（HITL）工作流
- 作为构建自定义人工审批 agent 的起点

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: The repository contains a bare minimum code example to get started with the Agent Inbox with LangGraph.js.
> L35: Now that our LangGraph server is running, we can start a new run in the Studio. To do this, simply enter any string

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/agent-inbox-langgraphjs-example 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6697adfac6c0` · [字段定义](../../DATASET.md)*
