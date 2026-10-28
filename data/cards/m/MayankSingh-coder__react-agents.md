# MayankSingh-coder/react-agents

⭐ 21 · Python · 推送 2025-11-09 · [GitHub](https://github.com/MayankSingh-coder/react-agents) · 个人维护

**混合 ReAct/Plan-Execute 的 AI agent 服务：自适应推理执行**

基于 LangGraph、LangChain 与 Google Gemini 构建的 AI agent 系统，按查询复杂度在 ReAct（思考-行动-观察循环）与 Plan-Execute（多步规划）两种模式间自动切换，失败时可重规划并降级。提供多层记忆（情景/向量/上下文）与上下文共享，内置数据库、Wikipedia 检索、Web 搜索、计算器、C++ 执行器等工具，支持自定义工具扩展与多 agent 框架。需 Python 3.8+ 与 Gemini API key，Serper key 为可选。以源码方式安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按查询复杂度自动选择 ReAct 或 Plan-Execute 模式，支持中途切换与重规划
- 情景/向量/上下文多层记忆与会话间上下文共享
- 内置数据库、Wikipedia、Web 搜索、计算器、C++ 执行器等工具
- 流式接口实时展示思考与工具执行过程

## 适用场景

- 需要多步规划的研究或数据处理任务
- 让 agent 联合使用搜索、计算与存储工具解决问题
- 构建并扩展自定义领域工具的 agent 应用

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A sophisticated AI agent system that combines **ReAct (Reasoning and Acting)** and **Plan-Execute** paradigms with a
> L8: - **🧠 Hybrid Intelligence**: Automatically chooses between ReAct and Plan-Execute strategies based on task complexit

## 星数曲线

```mermaid
xychart-beta
    title "MayankSingh-coder/react-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `f0db982a0b1a` · [字段定义](../../DATASET.md)*
