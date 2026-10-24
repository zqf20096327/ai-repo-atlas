# bhaskarblur/NeoBaseAI-Copilot-for-database

⭐ 69 · Go · NOASSERTION · 推送 2026-10-06 · [GitHub](https://github.com/bhaskarblur/NeoBaseAI-Copilot-for-database) · [官网](https://neobase.cloud) · 个人维护

**自托管 AI 数据库 Copilot：自然语言查库、分析与可视化**

NeoBase 是开源自托管的数据库对话式分析工具：通过自然语言在聊天界面生成并执行 SQL/NoSQL 查询，采用 Agentic 工具调用自主迭代执行；基于 Qdrant 的混合 RAG 检索数据库 Schema 与历史会话上下文；支持 AI 生成 11 种组件的仪表盘、根据查询结果自动生成图表。可连接 PostgreSQL、MySQL、MongoDB、ClickHouse 等 9 种数据源及 CSV/Excel、Google Sheets，支持事务管理与查询优化建议。LLM 侧支持 OpenAI、Gemini、Claude、Ollama 四类客户端共 65+ 预配置模型，通过环境变量切换。前后端为 React 与 Go(Gin)，安装细节指向 SETUP.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成/执行 SQL 与 NoSQL 查询的 Agentic 工具调用
- Qdrant 混合 RAG：Schema 检索相关表 + 历史会话语义检索
- AI 生成含 11 种组件的仪表盘，支持导入导出与变体重生成
- 支持 9 种数据库/数据源与事务管理（启动/提交/回滚）

## 适用场景

- 用对话方式查询和分析自己的数据库
- 让 AI 自动把查询结果做成图表和仪表盘
- 在自有基础设施上自托管，控制数据隐私

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: **NeoBase** is an AI database copilot that allows you to chat with your data and visualize, analyze it quickly and 
> L20: - **AI-Powered Queries with Agentic Tool Calling**: Generate and optimize SQL & NoSQL queries using natural languag
> L130: 3. **Chat with Your Database**:

## 星数曲线

```mermaid
xychart-beta
    title "bhaskarblur/NeoBaseAI-Copilot-for-database 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-24 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `032967b64efd` · [字段定义](../../DATASET.md)*
