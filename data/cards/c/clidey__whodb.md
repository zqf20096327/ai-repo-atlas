# clidey/whodb

⭐ 5,066 · Go · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/clidey/whodb) · [官网](https://whodb.com) · 组织维护

**自托管数据库工作台：浏览、查询、管理多种数据库，可选 AI 问答**

以浏览器为界面的自托管数据库工作区，支持数据网格浏览与内联编辑、交互式 schema 关系图、多单元查询暂存板（含自动补全与历史）、数据导入导出与 mock 数据生成。支持 PostgreSQL、MySQL、SQLite、MongoDB、Redis、Elasticsearch、ClickHouse 等 20 余种数据源，不同数据源能力有差异。AI 问答为可选功能，可接入本地或托管 provider。提供 Docker、桌面应用（macOS/Windows/Snap）与含 MCP server 的 CLI 三类使用形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 电子表格式数据浏览、过滤与内联编辑
- 交互式 schema 关系图与查询暂存板（自动补全、历史）
- 支持 20 余种关系型、文档型、缓存与搜索引擎数据源
- CLI 内置终端 UI 与 MCP server

## 适用场景

- 自托管一个轻量界面来管理本地和远程数据库
- 帮同事探索不熟悉的数据库 schema
- 为开发测试生成 mock 数据、导入导出数据
- 用自然语言向数据库提问（需自行接入 AI provider）

## 场景标签

`数据分析` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L36: WhoDB gives you one place to explore your databases, edit data, run queries, and understand how a schema fits toget
> L38: Use it when you want to inspect a local database, help a teammate explore unfamiliar data, or work without installi

## 星数曲线

```mermaid
xychart-beta
    title "clidey/whodb 星数(近 23 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-24"]
    y-axis "stars" 5036 --> 5068
    line [5038, 5039, 5041, 5042, 5043, 5042, 5046, 5047, 5048, 5041, 5051, 5053, 5054, 5055, 5056, 5058, 5059, 5060, 5063, 5064, 5065, 5066, 5066]
```

2026-10-22 5,038 → 2026-11-24 5,066（+28）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2e52f172277d` · [字段定义](../../DATASET.md)*
