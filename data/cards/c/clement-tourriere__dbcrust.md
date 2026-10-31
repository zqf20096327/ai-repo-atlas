# clement-tourriere/dbcrust

⭐ 92 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/clement-tourriere/dbcrust) · [官网](https://clement-tourriere.github.io/dbcrust/) · 个人维护

**终端多数据库 CLI/工作台，AI 助手为可选功能**

psql 风格的数据库命令行工具：通过统一 URL 语法连接 PostgreSQL、MySQL、SQLite、ClickHouse、MongoDB、Elasticsearch、Redis、SQL Server、Redshift 等 15+ 种数据库与数据服务，并以 DataFusion 对 Parquet/CSV/JSON 本地文件执行 SQL。提供交互式 REPL（60+ 反斜杠命令、自动补全）、一次性脚本模式（稳定退出码、JSON 输出）、SSH 隧道、Vault 凭证、Docker 容器发现、Python API 与 Django ORM 分析中间件。AI 助手为可选且默认关闭，支持 25+ 提供方，生成 SQL 前先展示。macOS/Linux 提供预编译二进制，桌面 GUI 需从源码构建。

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

- 统一 URL 语法连接 15+ 种数据库与 S3/DynamoDB/CloudWatch 等数据服务
- Parquet/CSV/JSON 文件经 DataFusion 直接以 SQL 查询，无需导入
- 面向 AI agent 的一次性模式：稳定退出码、JSON 输出、--read-only 守卫、无密码凭证代理
- Django ORM 性能分析中间件（N+1 查询、缺失 select_related 等检测）

## 适用场景

- 用同一套命令行工作流访问公司内多种数据库
- 不导入数据库直接对导出文件和日志跑 SQL 分析
- 给编码 agent 一个可安全调用数据库的 CLI 工具

## 场景标签

 · 领域:数据库工具/开发者效率

## 证据(README 行号)

> L3: **A fast psql-style database workbench for your terminal.** One CLI for PostgreSQL, MySQL, SQLite, ClickHouse, Mongo
> L15: > **AI is optional and disabled by default.** DBCrust works with zero AI setup. `??` sends schema metadata and your
> L23: - **Optional AI you control** — type `?? top 10 customers by revenue` to generate SQL from schema context, or use `

## 星数曲线

```mermaid
xychart-beta
    title "clement-tourriere/dbcrust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-31 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d83ef35fd7e6` · [字段定义](../../DATASET.md)*
