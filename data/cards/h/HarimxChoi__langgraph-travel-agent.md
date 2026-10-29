# HarimxChoi/langgraph-travel-agent

⭐ 20 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/HarimxChoi/langgraph-travel-agent) · 个人维护

**LangGraph 多智能体旅行规划系统，接入机票/酒店/CRM/SMS**

基于 LangGraph 的多智能体旅行规划后端服务：接收自然语言旅行请求，经 Google Gemini 生成结构化 TravelPlan，通过 Amadeus、Hotelbeds 并行搜索机票、酒店与活动，产出 Budget/Balanced/Premium 三档方案；支持对话中收集客户信息的人机协同流程，可选接入 Twilio 发送 SMS 与 HubSpot 创建 CRM 商机。以 FastAPI 提供 /chat 异步接口，用 git clone 源码加 pip 安装依赖运行，需 Python 3.10+ 与 Amadeus API key。

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

- 自然语言请求 → 结构化 TravelPlan，三档预算方案生成
- Amadeus/Hotelbeds 机票、酒店、活动异步并行搜索
- Human-in-the-loop：对话中收集客户信息表单
- FastAPI 异步 /chat 接口，任务状态轮询

## 适用场景

- 搭建旅行社或预订代理的自动化行程规划后端
- 并行聚合机票、酒店、活动数据生成打包方案
- 将规划结果同步到 CRM 并通过 SMS 通知客户

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Production-ready LangGraph multi-agent system for travel planning. Async parallel tool orchestration across Amadeus,
> L16: - LLM-driven package generation (Budget / Balanced / Premium)
> L61: |Google Gemini|yes|LLM (analysis, package generation, final response)|

## 星数曲线

```mermaid
xychart-beta
    title "HarimxChoi/langgraph-travel-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7de17165a1dc` · [字段定义](../../DATASET.md)*
