# gopalmani/QueryMindAI

⭐ 18 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/gopalmani/QueryMindAI) · [官网](https://querymind-web-iell.onrender.com) · 个人维护

**开源自然语言数据分析工作台：把业务问题转为安全可审计 SQL**

自托管 AI 数据工作区：用户连接只读 PostgreSQL 数据库，用自然语言提问，系统基于实时 schema 内省生成结构化 SQL，经 sqlglot 解析与表校验、LIMIT 封顶后存为草稿，需人工审批方可只读执行，结果与审计事件进入历史记录。支持 Ollama/Groq/OpenAI 兼容提供方，可选 pgvector 检索与人工验证示例。仅支持 PostgreSQL；账户登录与企业身份集成在路线图中，自述为早期版本。FastAPI + Next.js 技术栈，提供 Docker Compose 与 Render Blueprint 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- sqlglot 单语句解析与只读执行强制
- 生成 SQL 后需人工审批方可执行的草稿流程
- 支持 Ollama/Groq/OpenAI 兼容提供方与本地部署
- 加密保存连接、SSRF 检查与审计事件记录

## 适用场景

- 用自然语言查询业务数据库，无需写 SQL
- 在只读与人工审批约束下安全开放数据库查询
- 自托管部署供团队做数据分析工作区

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L4: QueryMindAI is an open-source AI data workspace that lets users connect a read-only database and query it safely usi
> L15: 2. **Query** — ask a business question, generate structured SQL, and review the SQL, explanation, assumptions, and 
> L22: - Schema-aware generation using live introspection, with optional pgvector retrieval.

## 星数曲线

```mermaid
xychart-beta
    title "gopalmani/QueryMindAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d6111a809ec2` · [字段定义](../../DATASET.md)*
