# nshiab/simple-data-analysis

⭐ 356 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/nshiab/simple-data-analysis) · [官网](https://nshiab.github.io/simple-data-analysis/) · 个人维护

**TypeScript 数据分析库：基于 DuckDB 做表格/地理/向量与 AI 辅助分析**

面向 JavaScript/TypeScript 生态的数据分析库，核心包基于 DuckDB 提供数据加载、过滤、连接、汇总与地理空间运算，主包在此基础上扩展 AI 方法（逐行 LLM 处理、嵌入、向量相似、混合搜索、RAG、自然语言查询）、Google Sheets/Cloud Storage 集成与图表地图可视化。由 CBC News 计算新闻记者 Nael Shiab 维护，源自数据新闻项目中跨语言切换的需求。变换以队列形式融合为单条 DuckDB 语句执行，支持直接下载 Statistics Canada 与 OpenStreetMap 数据；AI 能力依赖 Gemini/Vertex AI 或本地 Ollama，需配置 .env。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DuckDB 的链式同步 API，操作融合为单条 SQL 减少数据库往返
- AI 方法含逐行 LLM 处理、嵌入、聚类、向量相似与 RAG（journalism-ai）
- 可直接下载 Statistics Canada 与 OpenStreetMap 数据并默认本地缓存
- LLM 响应与嵌入默认缓存于 .journalism-cache，避免重复调用

## 适用场景

- 在 TypeScript 中完成数据清洗、分析与可视化，无需切换 Python/R
- 用 LLM 批量清洗、抽取、分类表格数据或构建语义搜索
- 加载加拿大统计局与 OpenStreetMap 公共数据做地理分析

## 场景标签

`数据分析` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L3: SDA is a fast and easy-to-use TypeScript library for tabular, geospatial,
> L29: - **`simple-data-analysis`** (this package) extends the core with additional
> L31:  hybrid search, RAG, natural language queries), Google Cloud Storage and Google

## 星数曲线

```mermaid
xychart-beta
    title "nshiab/simple-data-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 355 --> 357
    line [356, 356]
```

2026-10-18 356 → 2026-10-22 356（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1e2852e97dcd` · [字段定义](../../DATASET.md)*
