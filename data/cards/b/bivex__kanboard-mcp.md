# bivex/kanboard-mcp

⭐ 28 · Go · MIT · 推送 2026-06-12 · [GitHub](https://github.com/bivex/kanboard-mcp) · 个人维护

**Go 编写的 Kanboard MCP 服务器：让 AI 客户端管理看板项目与任务**

以 Go 实现的 Model Context Protocol 服务器，将自然语言指令转换为 Kanboard JSON-RPC API 调用，供 Claude Desktop、Cursor 等 MCP 客户端使用。提供项目管理、任务、评论、列、分类、泳道、看板、当前用户与外部任务链接等 80 余个工具，支持 API key（global_token/user_token）与 Bearer 三种认证方式，并通过环境变量配置应用级与项目级 RBAC 角色。需从源码克隆并自行构建（Go 1.21+），无预编译安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 Kanboard API 调用，兼容 MCP 标准客户端
- 覆盖项目、任务、评论、列、分类、泳道等多类管理工具
- 三种认证方式与基于环境变量的 RBAC 角色控制

## 适用场景

- 在 Cursor 或 Claude Desktop 中用自然语言管理 Kanboard 项目与任务
- 让 AI 助手查询逾期任务、看板与个人仪表盘
- 通过角色配置控制 AI 客户端的 Kanboard 操作权限

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: > **Model Context Protocol (MCP) Server for Kanboard Integration**
> L5: A powerful Go-based MCP server that enables seamless integration between AI assistants (like Claude Desktop, Cursor)
> L31: - 🎯 **MCP Standard** - Compatible with all MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "bivex/kanboard-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8a49f486d44f` · [字段定义](../../DATASET.md)*
