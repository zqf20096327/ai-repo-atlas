# pragunbhutani/dbt-llm-agent

⭐ 180 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/pragunbhutani/dbt-llm-agent) · [官网](https://ragstar.vercel.app) · 个人维护

**面向 dbt 项目的 AI 数据分析问答应用（Ragstar）**

Ragstar 连接 dbt 项目（dbt Cloud、GitHub 或 zip 上传），从模型与文档构建基于 PostgreSQL+pgvector 的知识库，让用户通过 Web 仪表盘或 Slack 用自然语言提问，由 Embeddings+LLM（OpenAI、Anthropic、Google 等，需 API key）生成回答。技术栈为 Next.js 前端 + Django 后端，Docker Compose 一键部署。另含 MCP 服务器（仅自托管），供 Claude.ai 等 LLM 客户端经 OAuth 2.0 访问 dbt 知识库。项目处于 public beta，MCP 服务器暂时禁用中，Metabase/Snowflake 集成为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 dbt 模型与文档构建 pgvector 知识库，自然语言问答
- Web 仪表盘与 Slack（/ask 命令）两种提问入口
- 内置 MCP 服务器（OAuth 2.0+PKCE），供 Claude.ai 等客户端访问 dbt 知识库，仅限自托管
- Docker Compose 一键部署，本地仅需 3 个环境变量

## 适用场景

- 团队用自然语言查询 dbt 数据模型获得分析结果
- 在 Slack 中通过 /ask 直接提问数据问题
- 让 Claude.ai 通过 MCP 直接浏览和检索我的 dbt 模型

## 场景标签

 · 领域:数据分析/LLM 应用

## 证据(README 行号)

> L12: Ragstar connects to your **dbt** project, builds a knowledge base from models & documentation, and lets everyone as
> L15: - Embeddings + LLMs (OpenAI, Anthropic, etc.) for reasoning

## 星数曲线

```mermaid
xychart-beta
    title "pragunbhutani/dbt-llm-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-22 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `94fba201dc4f` · [字段定义](../../DATASET.md)*
