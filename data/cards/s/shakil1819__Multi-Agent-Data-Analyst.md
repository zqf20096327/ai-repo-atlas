# shakil1819/Multi-Agent-Data-Analyst

⭐ — · [GitHub]() · 个人维护

**多智能体数据分析系统：将复杂分析任务拆分并分派给专用 Agent**

基于 LangChain/LangGraph 构建的 Agentic 数据分析系统：由 Agent Orchestrator 统一协调，将复杂数据分析任务拆分为子任务，分派给 Data Analyst Agent、SQL Data Analyst Agent 等专用智能体处理，并由 Visualization Server 负责结果可视化。以 FastAPI 提供 API（默认端口 8080），需配置 OPENAI_API_KEY。安装使用 uv 管理依赖，通过 python main.py 运行，附 pytest 测试与覆盖率命令。README 未展示具体演示或部署细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent Orchestrator 协调多个专用智能体（数据分析、SQL 分析）
- 拆解复杂数据分析任务为子任务并委派
- FastAPI 提供交互端点（localhost:8080）
- 提供 pytest 测试与覆盖率运行命令

## 适用场景

- 通过 API 提交复杂数据分析任务由多智能体协作完成
- SQL 数据分析子任务交由专用智能体处理
- 查看分析结果的可视化输出

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L27: This Agentic system is designed to handle complex data analysis tasks by breaking them down into smaller subtasks a
> L31: - **Agent Orchestrator**: The main controller that coordinates the work of the agents.

## 星数曲线

```mermaid
xychart-beta
    title "shakil1819/Multi-Agent-Data-Analyst 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ae5ce1ac3cec` · [字段定义](../../DATASET.md)*
