# local-falcon/mcp

⭐ 24 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/local-falcon/mcp) · [官网](https://www.localfalcon.com/features/mcp) · 组织维护

**将 Local Falcon 本地 SEO 平台接入 MCP 客户端的服务器**

用 TypeScript 基于官方 MCP SDK 实现的 Model Context Protocol 服务器，把 Local Falcon 商业平台的地理网格排名扫描、活动管理、竞争对手分析、评论分析、Falcon Guard 监控与 Google Business Profile 管理暴露为 MCP 工具（普通客户端 60 个、ChatGPT 会话 57 个）。支持 OAuth 2.1/PKCE、Bearer Token 与 API key 查询串三种认证，提供远程 HTTP/SSE 与本地 STDIO 运行方式，并内置带 HTML 消毒的 geo-grid 热力图交互组件。使用需 Local Falcon 账户与计费积分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 MCP 工具形式暴露扫描、活动管理、竞品分析、GBP 管理等约 60 项能力
- OAuth 2.1+PKCE、Bearer Token、API key 查询串三种认证方式
- 交互式 geo-grid 热力图 MCP Apps 组件（带 HTML 消毒）
- 每个工具显式声明 readOnly/destructive/openWorld 注解

## 适用场景

- 在 Claude/ChatGPT 等 MCP 客户端中直接查询本地搜索排名扫描报告
- 通过对话创建和管理定时的排名追踪活动
- 在 AI 客户端内查看业务位置的 geo-grid 排名热力图

## 场景标签

 · 领域:本地 SEO/营销分析工具

## 证据(README 行号)

> L5:  An MCP (Model Context Protocol) server for the Local Falcon AI visibility and local search intelligence platform
> L16: Local Falcon is an AI visibility and local search intelligence platform that tracks business visibility across AI s

## 星数曲线

```mermaid
xychart-beta
    title "local-falcon/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a60d2d97c60a` · [字段定义](../../DATASET.md)*
