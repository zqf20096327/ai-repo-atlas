# Empreiteiro/data-talks

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Empreiteiro/data-talks) · [官网](https://www.t2d.digital/) · 个人维护

**自然语言数据分析平台：连接数据源，提问即得图表答案**

自托管的 Web 数据分析平台：接入 CSV/XLSX、BigQuery、PostgreSQL/MySQL/Snowflake、Google Sheets、S3、REST API 及 Stripe/Salesforce 等 10+ SaaS 数据源，通过 LLM agent 用自然语言提问，自动生成图表与表格回答。含 LLM 驱动的数据源引导向导（澄清列含义、建议 KPI 与筛选器）、定时监控告警、仪表盘、多租户与角色权限、MCP server 暴露及 Telegram/WhatsApp/Slack 机器人集成。后端 Python/FastAPI，前端 React/Vite，LLM 支持 OpenAI 兼容、Ollama、Claude、Gemini 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多类数据源接入：文件、SQL 数据库、BigQuery、SaaS 集成（Stripe/Salesforce/HubSpot 等）
- LLM 驱动的数据源引导向导：澄清问题、KPI 建议、跨源关系推断
- 自然语言 Q&A 自动生成图表，SQL 模式可返回原始查询
- 多租户组织与角色权限、MCP server、Telegram/WhatsApp/Slack 机器人集成

## 适用场景

- 把公司各处数据接入后用自然语言做即席分析
- 为 SaaS 工具（CRM、支付、客服）生成预置模板报表
- 通过 Telegram/Slack 在聊天中直接查询业务数据
- 设置定时告警持续监控业务指标变化

## 场景标签

`数据分析` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L11: - **Ask questions** in natural language about your data
> L52: - **Visual answers**: Auto-generated charts and tables, server-rendered as images
> L115: - **LLM providers**: OpenAI / OpenAI-compatible (LiteLLM, OpenRouter, …), Ollama, Anthropic Claude (API), Claude C

## 星数曲线

```mermaid
xychart-beta
    title "Empreiteiro/data-talks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6f22381123f2` · [字段定义](../../DATASET.md)*
