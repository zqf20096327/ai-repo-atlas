# hayyanjpg/SQL_Analysis

⭐ 3 · JavaScript · 推送 2026-11-20 · [GitHub](https://github.com/hayyanjpg/SQL_Analysis) · [官网](https://sql-analysis.vercel.app) · 个人维护

**自然语言查询 PostgreSQL 的 text-to-SQL 数据分析台**

SIFT 是一个基于自然语言的数据分析平台：用户以 Google 或邮箱登录后上传 CSV/Excel/SQL 数据集，用印尼语或英语提问，由 LLM 生成 SQL 并在 PostgreSQL 上执行，返回表格与自动图表。后端 FastAPI，前端 React+Vite，数据库与认证用 Supabase，部署于 Vercel。关键机制包括：每账号独立 PostgreSQL schema 隔离、SQL 白名单校验（仅允许 SELECT/单条语句/拒绝 DDL）、DML 需用户显式确认执行、SELECT 在只读事务中限时运行。用户无需自备 LLM API key，由应用方统一提供并按账号设每日配额。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成 SQL，结果以表格与自动折线/柱状图呈现
- 每账号独立 ws_ schema 数据隔离，跨 schema 查询返回 403
- SQL 安全校验：拒绝 DDL、要求 UPDATE/DELETE 带 WHERE、只读事务 60s 超时
- INSERT/UPDATE/DELETE 走人工确认流程，执行前二次校验

## 适用场景

- 不懂 SQL 的业务人员上传数据表后用日常语言查询
- 给团队内部搭一个带账号隔离的自助数据分析入口
- 需要 DML 变更必须人工审批的数据操作流程

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Platform analitik data berbasis bahasa natural: masuk dengan akun Google atau email, unggah dataset sendiri, ajukan 
> L30: 3. **Tanya dengan bahasa natural** — backend membaca skema workspace secara *real-time* dan menyuntikkannya ke prom


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8371a0220125` · [字段定义](../../DATASET.md)*
