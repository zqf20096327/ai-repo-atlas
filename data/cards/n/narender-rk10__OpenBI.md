# narender-rk10/OpenBI

⭐ 20 · TypeScript · NOASSERTION · 推送 2026-07-04 · [GitHub](https://github.com/narender-rk10/OpenBI) · 个人维护

**自托管 AI 商业智能平台：对话查询 90+ 数据源并生成仪表盘**

开源 BI 平台，用户用自然语言向 AI agent 提问，由 MindsDB 的 text2sql 技能翻译为 SQL 在用户数据库上执行，返回表格、自动图表与 LLM 摘要。支持拖拽仪表盘（AntV 图表/透视表/KPI/AI 叙事卡）、文件与网页爬取的 RAG 知识库（9 种向量库后端）、PDF/PPTX 导出、cron 定时报告经邮件/Telegram/Webhook 交付，以及 Langfuse 观测。后端 FastAPI + MongoDB，前端 React/TypeScript，通过 Docker 自托管，面向不会 SQL 的业务分析人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言查询经 MindsDB text2sql 在 90+ 数据源上执行
- 结构化 SQL 与非结构化 RAG 混合查询（9 种向量库后端）
- 拖拽仪表盘 + 对话修改图表 + PDF/PPTX 版本化导出
- Telegram 机器人移动端与 cron 定时报告交付

## 适用场景

- 不懂 SQL 的业务人员直接用英语查数据库拿图表
- 把数据库和文档知识库放进同一个 agent 问答
- 定时生成并推送经营报告到 Telegram 或邮箱

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: # OpenBI - AI-Native Business Intelligence Platform
> L126: - **Plain-English querying** — type any question; MindsDB translates it to SQL and executes it against your live d
> L17: Connect 90+ data sources, chat with AI agents, build interactive dashboards, and automate report delivery — powered

## 星数曲线

```mermaid
xychart-beta
    title "narender-rk10/OpenBI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d487053585ae` · [字段定义](../../DATASET.md)*
