# project-ryoma/ryoma

⭐ 405 · Python · Apache-2.0 · 推送 2026-02-01 · [GitHub](https://github.com/project-ryoma/ryoma) · [官网](https://project-ryoma.github.io/ryoma/) · 组织维护

**面向数据分析/工程/可视化的 AI 数据 Agent 框架**

Ryoma 是一个 Python AI 数据 Agent 框架，提供 SQL Agent 等能力：连接 Postgres、MySQL、BigQuery、Snowflake、SQLite 及文件等数据源，通过自然语言提问让 Agent 调用工具执行查询并流式返回结果。底层使用 LangChain、Apache Arrow、Ibis 等技术栈，模型接入依托 Jupyter AI Magics 支持的 provider 列表；另提供基于 Reflex 构建的 Ryoma Lab Web 界面，支持 Apache Spark 与 Flink 引擎。以 pip 包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQL Agent 通过自然语言对数据库提问并自动执行工具
- 支持 Snowflake/Postgres/MySQL/BigQuery/SQLite/文件等数据源
- 基于 Jupyter AI Magics 接入 10+ 模型 provider（OpenAI/Anthropic/Gemini 等）
- Ryoma Lab 提供 Reflex 构建的 Web 交互界面

## 适用场景

- 用自然语言查询业务数据库并获取分析结果
- 在 Web 界面中与数据和 AI 模型交互
- 构建数据分析/工程/可视化的 Agent 工作流

## 场景标签

`Agent 框架` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L2: AI Powered Data Agent framework, a comprehensive solution for data analysis, engineering, and visualization.
> L39: Below is an example of using Ryoma to connect to a postgres database and ask a question.
> L88: ## Supported Models

## 星数曲线

```mermaid
xychart-beta
    title "project-ryoma/ryoma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 404 --> 406
    line [405, 405]
```

2026-10-18 405 → 2026-10-28 405（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0b101608e2aa` · [字段定义](../../DATASET.md)*
