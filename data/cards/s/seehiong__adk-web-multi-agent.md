# seehiong/adk-web-multi-agent

⭐ 37 · Jupyter Notebook · 推送 2025-11-03 · [GitHub](https://github.com/seehiong/adk-web-multi-agent) · [官网](https://seehiong.github.io/posts/2025/11/adk-web-multi-agent-system/) · 个人维护

**用 Google ADK 与 OpenRouter 模型构建的多 Agent 数据查询示例系统**

演示型多 Agent 系统：基于 Google ADK 构建，采用 Coordinator/Dispatcher 模式，由协调 Agent 管理 postgres_agent 与 datacommons_agent 两个子 Agent，分别通过 MCP Toolbox 查询本地 PostgreSQL 中的 HDB 转售数据、通过 Data Commons MCP API 获取全球统计数据，模型经 OpenRouter 接入，用户以自然语言提问获得数据回答。运行需本地 PostgreSQL（127.0.0.1:5432）、Data Commons MCP Server、Toolbox 工具服务器及 uv 管理的 Python 环境，最终以 `adk web` 启动。面向学习 Agent 层级架构与多数据源接入的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Coordinator/Dispatcher 模式路由查询到专职子 Agent
- 经 MCP Toolbox 查询 PostgreSQL，经 Data Commons MCP API 获取全球统计
- 模型通过 OpenRouter 接入，依赖以 uv 管理（google-adk/litellm/toolbox-core）

## 适用场景

- 学习 Google ADK 多 Agent 层级与协调模式的搭建方式
- 用自然语言查询本地 PostgreSQL 与 Data Commons 两类数据源
- 参考 MCP 工具服务器（Toolbox/Data Commons）与 Agent 的集成做法

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repository demonstrates building a multi-agent system using **Google's ADK (Agent Development Kit)**. The syste
> L43: This project structure requires a **Coordinator Agent** (defined in the main execution logic) that hierarchically m

## 星数曲线

```mermaid
xychart-beta
    title "seehiong/adk-web-multi-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a64793301002` · [字段定义](../../DATASET.md)*
