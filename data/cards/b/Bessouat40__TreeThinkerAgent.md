# Bessouat40/TreeThinkerAgent

⭐ 21 · JavaScript · MIT · 推送 2026-02-11 · [GitHub](https://github.com/Bessouat40/TreeThinkerAgent) · 个人维护

**将任意 LLM 编排为自主多步推理 agent 的轻量层**

轻量级 agent 编排层：由 AgentManager 驱动自主规划循环，LLM 提出推理步骤、执行工具并记录为可探索的推理树，最终合成针对原始查询的报告。内置 DuckDuckGo Lite 搜索与 HTML 抽取，工具以 @tool 装饰 Pydantic 校验的可调用对象注册，可运行时扩展。LLM 后端可通过环境变量在 OpenAI、Ollama、Mistral 间切换。明确不依赖 LangChain/LlamaIndex 等库，定位为极简探索性项目，自带 FastAPI 后端与前端，前端需 npm 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AgentManager 自主规划循环，推理过程以树结构暴露
- @tool 装饰器 + Pydantic 校验的工具注册框架
- LLM_PROVIDER 环境变量切换 OpenAI/Ollama/Mistral 后端
- 内置 DuckDuckGo Lite 搜索与 HTML 内容抽取工具

## 适用场景

- 让任意 LLM 自主拆解多步研究问题并生成报告
- 可视化探索 agent 的逐步推理过程
- 以最小依赖学习或试验自主 agent 规划机制

## 场景标签

`Agent 框架` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: TreeThinkerAgent is a lightweight orchestration layer that turns any LLM into an autonomous multi-step reasoning age
> L14: - **Autonomous planning loop** – The `AgentManager` asks the LLM to propose reasoning steps, executes the required 

## 星数曲线

```mermaid
xychart-beta
    title "Bessouat40/TreeThinkerAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `576942c5eea1` · [字段定义](../../DATASET.md)*
