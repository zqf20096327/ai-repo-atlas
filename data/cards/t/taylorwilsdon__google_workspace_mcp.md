# taylorwilsdon/google_workspace_mcp

⭐ 3,594 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/taylorwilsdon/google_workspace_mcp) · [官网](https://workspacemcp.com) · 个人维护

**让 AI 助手通过 MCP 操作 Google Workspace 全套服务的服务器**

MCP 服务器与 CLI 工具，通过 120+ 工具连接 AI 助手到 12 个 Google Workspace 服务（Gmail、Drive、Calendar、Docs、Sheets、Slides、Forms、Tasks、Contacts、Chat、Custom Search、Apps Script）。机制包括 OAuth 2.1 多用户认证、三级渐进工具分层（core/extended/complete）、只读模式、无状态容器部署、stdio 与 streamable HTTP 双传输。需要用户自建 Google Cloud OAuth 凭据；MIT 许可，支持商业使用。

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

- 120+ 工具覆盖 12 个 Google Workspace 服务
- OAuth 2.1 多用户认证与 PKCE 模式，支持组织级集中部署
- 三级工具分层与 --tools/--read-only/--disabled-tools 上下文控制
- 附带 workspace-cli 命令行工具与加密磁盘缓存的 OAuth 令牌

## 适用场景

- 让 Claude Desktop / ChatGPT 等客户端读写 Gmail、Calendar、Drive
- 为团队提供集中部署的多用户 Google Workspace AI 接入
- 通过 CLI 脚本化调用 Workspace 工具
- 只读模式下安全地让 AI 检索企业文档

## 场景标签

 · 领域:AI 生态/MCP 工具服务

## 证据(README 行号)

> L10: *Full natural language control over Google Calendar, Drive, Gmail, Docs, Sheets, Slides, Forms, Tasks, Contacts, an
> L35: Workspace MCP connects AI assistants to all twelve major Google Workspace services - 120+ tools behind a single MCP

## 星数曲线

```mermaid
xychart-beta
    title "taylorwilsdon/google_workspace_mcp 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 3389 --> 3612
    line [3407, 3411, 3417, 3423, 3430, 3437, 3444, 3451, 3456, 3407, 3485, 3502, 3506, 3508, 3513, 3518, 3523, 3530, 3538, 3544, 3549, 3556, 3560, 3564, 3573, 3585, 3594]
```

2026-10-25 3,407 → 2026-11-27 3,594（+187）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a9a303bd7d35` · [字段定义](../../DATASET.md)*
