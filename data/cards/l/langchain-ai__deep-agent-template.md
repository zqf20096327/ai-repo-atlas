# langchain-ai/deep-agent-template

⭐ 21 · Python · 推送 2026-10-14 · [GitHub](https://github.com/langchain-ai/deep-agent-template) · 组织维护

**开发者部署 deep agent 的 LangGraph 项目模板**

基于 create_deep_agent 构建的深度智能体部署模板：提供可部署的 agent graph、显式工作流提示（plan/delegate/critique/finalize）、researcher 与 critic 两个预定义子智能体，以及在 execute 和 write_file 上的人工审批中断。工程由 uv 管理，附 Makefile 包装与测试（集成测试需 ANTHROPIC_API_KEY）。部署依赖 LangSmith 账号（Plus 及以上），通过 langgraph deploy 或 LangSmith UI 完成。面向使用 LangChain 生态构建智能体的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 含 plan/delegate/critique/finalize 显式工作流提示的可部署 agent graph
- researcher 与 critic 两个预定义子智能体
- execute 与 write_file 节点的人工在环中断
- uv 管理的本地工作流、Makefile 包装与测试

## 适用场景

- 快速起步一个带子智能体与人工审批的深度智能体项目
- 通过 LangSmith 部署与迭代智能体服务
- 作为团队智能体工程的结构化项目骨架

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Deployment template for a deep agent built with `create_deep_agent(...)`.
> L7: - A deployable deep agent graph at `src/deep_agent/graph.py`.

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/deep-agent-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2d3817c8d3b8` · [字段定义](../../DATASET.md)*
