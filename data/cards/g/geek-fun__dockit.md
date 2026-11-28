# geek-fun/dockit

⭐ 1,147 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/geek-fun/dockit) · [官网](https://www.geekfun.club/products/dockit/) · 组织维护 · 中文 README

**多 NoSQL 数据库桌面 GUI 客户端，支持自然语言查询与管理**

基于 Tauri（Rust）+ Vue 3 构建的原生桌面应用，为 Elasticsearch、OpenSearch、DynamoDB、MongoDB 与 EasySearch 提供统一 GUI：Monaco 编辑器、查询构建器、集群/索引/表管理、查询历史、JSON/CSV 导入导出与监控。AI 部分：Agent 以自然语言生成查询（ES DSL、PartiQL、MongoDB）、检查 schema、执行 CRUD，支持 destructive 操作确认门与凭证不外泄；通过 MCP server 可接入外部 agent 客户端。提供 macOS/Windows/Linux 安装包，隐私上不采集遥测、本地存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个桌面应用管理 ES/OpenSearch/DynamoDB/MongoDB/EasySearch 五类数据库
- 自然语言生成 ES DSL、PartiQL、MongoDB 查询并执行数据操作
- MCP server 可被 Claude Code、Cursor 等 MCP 客户端接入，支持分级权限控制
- 隐私机制：无遥测、凭证经系统钥匙串加密、支持完全离线

## 适用场景

- 用一个客户端替代 Kibana/AWS Console 管理多个 NoSQL 数据库
- 用自然语言描述需求让 agent 生成并执行查询
- DynamoDB Local 离线开发无需 AWS 凭证
- 集群迁移、备份与开发环境数据填充的批量导入导出

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Open-source GUI client for Elasticsearch, OpenSearch, DynamoDB and MongoDB — one native desktop app for all your N
> L20: DocKit replaces browser consoles like Kibana and AWS Console with a single native desktop app. Describe what you ne
> L67: Describe what you need in natural language — the agent writes queries, inspects schemas, updates documents, deletes

## 星数曲线

```mermaid
xychart-beta
    title "geek-fun/dockit 星数(近 10 点)"
    x-axis ["2026-10-26", "2026-11-01", "2026-11-06", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-28"]
    y-axis "stars" 1140 --> 1148
    line [1142, 1141, 1143, 1144, 1145, 1146, 1145, 1146, 1147, 1147]
```

2026-10-26 1,142 → 2026-11-28 1,147（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `bf8fbb58c4fa` · [字段定义](../../DATASET.md)*
