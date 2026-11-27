# paolobietolini/gtm-mcp-server

⭐ 192 · Go · BSD-3-Clause · 推送 2026-11-26 · [GitHub](https://github.com/paolobietolini/gtm-mcp-server) · [官网](https://mcp.gtmeditor.com) · 个人维护

**让 LLM 客户端经 MCP 以自然语言管理 Google Tag Manager**

一个连接 MCP 客户端与 Google Tag Manager API 的服务器：可检查容器、创建和更新工作区实体、创建版本并在显式确认后发布，覆盖 Google 106 个 GTM v2 方法中的 101 个（故意排除 user_permissions 相关 5 个敏感方法）。支持 stdio 与 HTTP 两种传输，认证采用浏览器 OAuth 或服务账号；附带 gtm-cli 命令行工具，供 shell、脚本与 agent 无服务器直接访问 GTM。原托管端点已关闭，需自行部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 GTM v2 API 101/106 个方法，默认 64 个工具、全部 94 个
- stdio / HTTP + OAuth / HTTP + 服务账号等多种部署模式
- 附带 gtm-cli 命令行工具，无需服务器即可访问 GTM
- 写入命令支持 --dry-run，delete/publish 需 --confirm

## 适用场景

- 通过 Claude Code、Cursor 等 MCP 客户端用自然语言管理 GTM 标签、触发器与变量
- 在 CI 或自动化流程中以服务账号批量操作 GTM 工作区与版本发布
- 用 gtm-cli 在脚本与 shell 中做 GTM 只读审计

## 场景标签

 · 领域:开发者工具/营销基础设施

## 证据(README 行号)

> L18: GTM MCP Server connects MCP clients to the Google Tag Manager API. It can
> L36: |Transport|MCP Streamable HTTP, or stdio for local service-account use|
> L51: agents such as Claude Code, Codex and Cursor. There is no server, MCP client

## 星数曲线

```mermaid
xychart-beta
    title "paolobietolini/gtm-mcp-server 星数(近 12 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-20", "2026-11-21", "2026-11-27"]
    y-axis "stars" 178 --> 193
    line [179, 180, 182, 179, 186, 187, 188, 189, 190, 191, 192, 192]
```

2026-10-25 179 → 2026-11-27 192（+13）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `c688bc0f2ad2` · [字段定义](../../DATASET.md)*
