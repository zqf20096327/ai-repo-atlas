# Laksh-star/competitive-intelligence

⭐ 23 · Python · MIT · 推送 2026-06-22 · [GitHub](https://github.com/Laksh-star/competitive-intelligence) · 个人维护

**AI 驱动的竞争情报监控管线：搜网+LLM 抽取事件+生成简报**

基于 Python 的竞争情报监控管线：用 Tavily AI 搜索竞对公司新闻，通过 OpenRouter 调用 GPT-4o-mini/DeepSeek 抽取产品发布、合作、融资、高管变动、并购五类结构化事件并评级，用 CocoIndex 增量索引到 PostgreSQL，输出 Markdown/JSON/CSV/HTML 简报与仪表盘。另暴露 7 个 MCP 工具供 agent 调用。提供无凭据的示例模式（读取本地文章 JSON 即可运行）；实时模式需 PostgreSQL、Tavily 与 OpenRouter API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tavily 搜索 + LLM 抽取五类竞争事件并评定重要性
- CocoIndex 增量双索引（文章与事件）到 PostgreSQL
- 暴露 7 个 MCP 工具供其他 agent 调用
- 无凭据示例模式可直接本地运行，输出简报与静态仪表盘

## 适用场景

- 定期监控竞对公司的产品、融资、并购动态并生成简报
- 让 MCP 客户端 agent 调用工具查询事件与趋势
- 分析已有文章集合生成竞争情报仪表盘

## 场景标签

`网页抓取` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L17: - **Searches** the web using Tavily AI (AI-native search engine optimized for agents)
> L18: - **Extracts** competitive intelligence events using DeepSeek LLM analysis:
> L406: 2. **LLM Extraction** (GPT-4o-mini via OpenRouter)

## 星数曲线

```mermaid
xychart-beta
    title "Laksh-star/competitive-intelligence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dff284198938` · [字段定义](../../DATASET.md)*
