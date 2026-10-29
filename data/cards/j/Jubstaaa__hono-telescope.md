# Jubstaaa/hono-telescope

⭐ 27 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/Jubstaaa/hono-telescope) · [官网](https://hono-telescope.ilkerbalcilar.com/telescope) · 个人维护

**Hono 应用的 Telescope 式调试面板，附带供 AI agent 读取遥测的 MCP 服务**

面向 Hono 框架开发者的调试中间件：以仪表盘展示每个请求及其日志、SQL 查询（Prisma/Sequelize/MongoDB/Bun SQLite 需逐客户端显式插桩）、异常与外发 fetch 调用；同一端点兼作 MCP 服务器，提供 recent_exceptions、request_detail、slow_queries 等五个只读工具，供 Claude Code、Cursor 等 agent 直接读取运行中应用的遥测，另附 stdio 桥接。零运行时依赖，支持 Node.js 与 Bun；默认生产环境禁用，需 basic auth 方可开启。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仪表盘端点兼作 MCP 服务器，提供 5 个只读遥测工具
- 显式插桩 Prisma/Sequelize/MongoDB/Bun SQLite 查询并记录执行时间
- 默认递归脱敏敏感 header 与 body 字段
- 为零依赖的 npm 包，仅以 Hono 为 peer 依赖，Node.js/Bun 双运行时

## 适用场景

- 开发 Hono 应用时在面板中查看请求、查询、异常与外发调用
- 让 Claude Code/Cursor 等 agent 直接读取应用实时遥测定位错误
- 通过 minStatus 过滤返回错误状态但未抛异常的失败请求

## 场景标签

 · 领域:Web 开发/可观测性

## 证据(README 行号)

> L13: A debugging tool for Hono applications, inspired by Laravel Telescope: a dashboard that shows
> L47: - 📡 **MCP Server** - The dashboard endpoint doubles as a Model Context Protocol server, so an AI agent can read liv

## 星数曲线

```mermaid
xychart-beta
    title "Jubstaaa/hono-telescope 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-29 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0a2b9774834d` · [字段定义](../../DATASET.md)*
