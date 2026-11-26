# polterguy/magic

⭐ 1,254 · C# · MIT · 推送 2026-11-25 · [GitHub](https://github.com/polterguy/magic) · [官网](https://hyperlambda.dev) · 个人维护

**用自然语言生成全栈应用与 AI Agent 的开源低代码平台**

基于 .NET 的开源低代码平台：用户用英文描述即可生成数据库、受保护 REST API、业务逻辑与前端，运行在自有硬件上。核心机制包括 API Wizard 读取数据库生成 CRUD 接口、Hyperlambda 沙箱执行与 RBAC 函数白名单、内置 MCP 服务器把端点暴露为工具、Chatbot Wizard 爬取网站生成嵌入式聊天机器人。通过 docker compose 一键启动，Dashboard 集成 IDE、SQL Studio、定时任务与插件商店。自带的 LLM 为专有组件，其余代码 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- API Wizard 从数据库 schema 生成受 RBAC 保护的 CRUD REST API
- 内置 MCP 服务器，将每个端点暴露为 Claude/Cursor/Codex 可调用工具
- Hyperlambda AST 生成机制声称拒绝调用不存在的函数
- Chatbot Wizard 爬取网站内容生成可嵌入聊天机器人

## 适用场景

- 为现有 MySQL/PostgreSQL 数据库快速生成 CRUD API
- 构建查询自有数据库并遵守 RBAC 的 AI Agent
- 从 OpenAPI/Swagger 规范生成第三方 API 包装端点
- 自托管搭建 CRM、后台管理等内部业务应用

## 场景标签

`代码生成` `聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Turn plain English into a working full-stack app — database, secure API, business logic, and frontend — running on *
> L40: * **MCP tool servers** — expose your endpoints to Claude, Cursor, Codex, Qoder or any MCP client

## 星数曲线

```mermaid
xychart-beta
    title "polterguy/magic 星数(近 14 点)"
    x-axis ["2026-10-24", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-26"]
    y-axis "stars" 1199 --> 1260
    line [1204, 1205, 1206, 1207, 1204, 1247, 1248, 1250, 1251, 1255, 1254, 1255, 1254, 1254]
```

2026-10-24 1,204 → 2026-11-26 1,254（+50）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `c06f3460773b` · [字段定义](../../DATASET.md)*
