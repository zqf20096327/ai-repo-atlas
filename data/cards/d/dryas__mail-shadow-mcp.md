# dryas/mail-shadow-mcp

⭐ 14 · Go · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/dryas/mail-shadow-mcp) · 个人维护

**给 AI agent 提供安全邮件只读访问的 MCP 服务器**

Go 编写的 MCP 服务器：通过同步引擎用 IMAP 凭据（只读 SELECT/UID FETCH）将邮件同步进本地 SQLite FTS5 影子数据库，AI agent 仅通过 MCP API（stdio/HTTP/SSE）查询，IMAP 凭据不暴露给 agent。提供 8 个工具：全文本搜索、读取邮件、线程视图、下载附件、软删除（IMAP MOVE 到指定垃圾文件夹，不永久删除）等，支持多账户、IMAP IDLE 实时推送与增量同步。面向不想让 agent 直连邮箱的用户，推荐 Docker 运行隔离凭据，也可用预编译二进制 stdio 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 SQLite FTS5 影子数据库，agent 不直连 IMAP，凭据不暴露
- 软删除机制：IMAP MOVE 到配置文件夹，不执行破坏性命令
- 多账户同步、增量同步与 IMAP IDLE 实时推送
- Docker 多架构镜像（amd64/arm64）与 HTTP Bearer Token 鉴权

## 适用场景

- 让 AI 助手安全地搜索和阅读我的邮件
- 让 agent 汇总未读邮件或查找发票、航班确认等邮件
- 在不暴露 IMAP 凭据的前提下给 agent 提供邮件上下文

## 场景标签

 · 领域:AI Agent 基础设施/邮件访问

## 证据(README 行号)

> L38: [Remote IMAP Server] ──IMAP──▶ [Sync Engine] ──▶ [SQLite FTS5] ◀──▶ [MCP Server] ◀──▶ [AI Agent]
> L186: - **Local shadow database** — emails are synced into a local SQLite database; the AI agent never connects to your 

## 星数曲线

```mermaid
xychart-beta
    title "dryas/mail-shadow-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2dc1a4507bdc` · [字段定义](../../DATASET.md)*
