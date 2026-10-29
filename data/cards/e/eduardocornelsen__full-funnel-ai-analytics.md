# eduardocornelsen/full-funnel-ai-analytics

⭐ 25 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/eduardocornelsen/full-funnel-ai-analytics) · 个人维护

**全漏斗营销分析平台：自然语言查询 + 语义层治理 + ML 评分**

基于 dbt MetricFlow 语义层与 MCP 的营销分析栈：AI 层通过 6 个 mock MCP 服务器与 dbt Semantic Layer MCP，让 Claude Desktop、OpenCode、Gemini CLI、Antigravity IDE 以自然语言查询营销数据并生成仪表盘；ML 层用 XGBoost + MLflow + FastAPI /score 做线索评分；BI 层提供 Looker Studio、Streamlit 仪表盘。支持 5 种数仓（BigQuery/Snowflake/Databricks/DuckDB/Supabase），数据基于 Olist 与合成追加，四个 GitHub Actions 工作流保障零指标漂移，基于免费/试用层运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dbt 语义层统一定义指标，供 AI 客户端、仪表盘与 ML 管线共同消费
- XGBoost 线索评分：MLflow 实验跟踪 + FastAPI /score + n8n 自动路由
- 6 个 MCP 服务器暴露数仓、Google/Meta Ads、GA4、HubSpot、Salesforce 工具
- validate_metrics.py 零漂移校验，PR 与部署均强制运行

## 适用场景

- 营销/增长团队用自然语言查询跨渠道花费、归因与 ROAS
- 数据科学家复用带实验跟踪的线索评分 API
- 分析工程师学习带语义层治理的 dbt + MCP 多数仓架构

## 场景标签

`数据分析` `教程课程` · 领域:效率与自动化

## 证据(README 行号)

> L25: **Natural language marketing analytics powered by MCP, dbt Semantic Layer, and ML lead scoring. Works with Claude D
> L106: |**AI Layer**|Query marketing data in plain English, generate dashboards|6 mock MCP servers + dbt Semantic Layer M
> L234: |**dbt Semantic Layer**|Governed metrics + SQL generation|`text_to_sql`, `get_metrics`, `get_dimensions` (60+ tool

## 星数曲线

```mermaid
xychart-beta
    title "eduardocornelsen/full-funnel-ai-analytics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `124b5f2caa5e` · [字段定义](../../DATASET.md)*
