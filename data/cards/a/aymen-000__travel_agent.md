# aymen-000/travel_agent

⭐ 21 · TypeScript · 推送 2025-11-13 · [GitHub](https://github.com/aymen-000/travel_agent) · 个人维护

**面向旅行规划的多 Agent 系统：航班/酒店/目的地智能体协作**

TravelMate AI 是基于 LangChain + LangGraph 的多智能体旅行规划系统，后端 FastAPI、前端 React + TypeScript。包含航班、酒店、目的地三个专用 Agent 与一个 Team Coordinator，负责跨 Agent 协调复杂行程；支持会话记忆与客户端线程持久化，通过自然语言对话完成机票搜索、住宿发现与目的地推荐。提供 REST API（/search/team 等四个端点），需配置 Amadeus 等 API key；部署方式为 git clone 源码运行前后端。租车 Agent 等功能列入 Roadmap 未实现，测试套件标注 coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 航班/酒店/目的地三个专用 Agent + Team Coordinator 协调
- LangGraph 编排的多 Agent 工作流与会话线程持久化
- FastAPI 后端提供 /search/team 等 4 个 REST 端点
- React + TypeScript 前端

## 适用场景

- 用自然语言对话完成机票搜索与酒店预订协助
- 获取目的地景点与当地文化推荐
- 作为开发者扩展新的旅行领域 Agent

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L24: - **Flight Agent**: Advanced flight search, price tracking, and booking assistance
> L43: - **AI/ML**: LangChain + LangGraph (advanced agent orchestration)

## 星数曲线

```mermaid
xychart-beta
    title "aymen-000/travel_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c4cc03af83fc` · [字段定义](../../DATASET.md)*
