# Mohith-akash/Global-News-Intel-Platform

⭐ 28 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Mohith-akash/Global-News-Intel-Platform) · [官网](https://global-news-intel-platform.streamlit.app/) · 个人维护

**GDELT 地缘新闻数据平台：每小时 ETL + 仪表盘与 AI 问答**

基于 GDELT 事件的新闻情报平台：GitHub Actions 定时触发 Dagster 作业，用 Polars 解析、Great Expectations 校验后写入 MotherDuck（DuckDB），dbt 每周构建模型并跑 30+ 测试；累计处理 3000 万+事件，每日新增约 10 万。Streamlit 仪表盘提供趋势、情绪与地理分析，AI 聊天有 RAG 与 SQL 双模式（Cerebras GPT-OSS 120B 生成回答，Voyage AI 嵌入），SQL 模式路由到测试过的查询模板而非由 LLM 直接写 SQL。面向数据工程与分析类开发者，全栈在免费额度上以 $0/月运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每小时摄取 10 万+ GDELT 事件，Polars + Great Expectations + MotherDuck 的无服务器 ELT
- 双模式 AI 聊天：RAG（关键词预过滤+向量搜索）与基于测试模板的 SQL 问答
- dbt 每周构建 staging 与 5 个 mart 表并运行 30+ 测试与新鲜度检查
- Cerebras 批量修复标题任务带幻觉防护

## 适用场景

- 追踪全球新闻事件、情绪与趋势的地缘政治分析
- 参考 $0/月的服务器端数据工程架构（编排/校验/仓库/向量搜索）
- 用自然语言查询 GDELT 数据（RAG 与 SQL 模板两种方式）

## 场景标签

`RAG` `数据分析` `MLOps` · 领域:效率与自动化

## 证据(README 行号)

> L5: Serverless ELT pipeline that ingests, processes, and visualizes 100,000+ global news events per day from the GDELT P
> L52: |AI chat|Two modes: RAG (keyword pre-filter plus vector search) and a SQL mode that routes questions to tested quer

## 星数曲线

```mermaid
xychart-beta
    title "Mohith-akash/Global-News-Intel-Platform 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-27 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9c2abbaf6a4b` · [字段定义](../../DATASET.md)*
