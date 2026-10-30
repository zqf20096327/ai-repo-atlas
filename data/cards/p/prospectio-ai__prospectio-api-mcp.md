# prospectio-ai/prospectio-api-mcp

⭐ 21 · Python · 推送 2026-03-25 · [GitHub](https://github.com/prospectio-ai/prospectio-api-mcp) · 组织维护

**面向线索挖掘的 FastAPI/MCP 服务器，连接多种销售线索数据源**

基于 FastAPI 实现 Model Context Protocol（MCP）与 REST 双协议的服务端，用于线索挖掘：通过 Active Jobs DB、Jsearch、Mantiks 等数据源按地点与职位检索公司招聘信息，持久化到 PostgreSQL（含 pgvector），并对联系人做三阶段信息补全——Perplexity（经 OpenRouter）搜索联系方式与简历、DuckDuckGo HTML 搜索发现 LinkedIn 主页 URL。采用 Clean Architecture 分层，供 AI agent 或客户端接入使用。运行需配置 Mantiks/RapidAPI 等 API key 与 PostgreSQL 连接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时暴露 REST（/rest/v1/）与 MCP（/prospectio/）两种协议
- 三种数据源策略（Active Jobs DB / Jsearch / Mantiks）可切换扩展
- 三阶段联系人补全：联系方式→LinkedIn URL→个人简历
- PostgreSQL + pgvector 持久化线索与档案数据

## 适用场景

- 为 AI agent 提供 MCP 工具来检索和管理销售线索
- 按地点和职位从多个招聘数据源批量抓取公司线索
- 对联系人执行联系方式与 LinkedIn 主页的自动化补全

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: A FastAPI-based application that implements the Model Context Protocol (MCP) for lead prospecting. The project follo
> L164:  - MCP protocol available at `/prospectio/` (implemented in `mcp_routes.py`)

## 星数曲线

```mermaid
xychart-beta
    title "prospectio-ai/prospectio-api-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f65750731531` · [字段定义](../../DATASET.md)*
