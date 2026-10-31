# 0xHayd3n/cPanel-MCP-Server

⭐ 26 · TypeScript · 推送 2026-09-10 · [GitHub](https://github.com/0xHayd3n/cPanel-MCP-Server) · 个人维护

**让 AI 助手通过 MCP 管理 cPanel 主机账户的服务器**

基于 TypeScript 实现的 Model Context Protocol 服务器，通过 cPanel UAPI 与 API2 接口连接 cPanel 账户，向 AI 助手暴露 164 个工具，覆盖文件、MySQL/PostgreSQL、邮件（含 DKIM/SPF）、DNS/DNSSEC、域名、SSL/AutoSSL、PHP、cron、安全（WAF/IP 封禁/2FA）、备份、FTP、Git 部署与 Node.js/Python 应用等管理操作。需要 Node.js 18+ 与 cPanel API token，通过 MCP 配置接入 Claude Desktop、Cline 等 AI 客户端，凭据经环境变量传入且默认强制 HTTPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 164 个工具覆盖 25 类 cPanel 管理功能
- 同时对接 UAPI 与旧版 API2（cron/DNS/子域名等）
- 凭据仅经环境变量传入，默认强制 HTTPS
- Git 版本控制与 Passenger 应用（Node.js/Python/Ruby）部署管理

## 适用场景

- 通过自然语言让 AI 助手管理我的 cPanel 主机
- 用 AI 操作 DNS、SSL、邮件与数据库等日常运维
- 在 Claude Desktop 或 Cline 中远程管理网站账户

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # cPanel MCP Server
> L3: A comprehensive Model Context Protocol (MCP) server for managing cPanel hosting accounts through AI assistants. Conn

## 星数曲线

```mermaid
xychart-beta
    title "0xHayd3n/cPanel-MCP-Server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c36cb747eaba` · [字段定义](../../DATASET.md)*
