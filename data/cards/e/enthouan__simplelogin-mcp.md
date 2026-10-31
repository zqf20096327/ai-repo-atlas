# enthouan/simplelogin-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/enthouan/simplelogin-mcp) · [官网](https://simplelogin-mcp.com) · 个人维护

**面向 SimpleLogin 用户的自托管 MCP 服务器：用 AI 客户端管理邮件别名**

独立开源的 Model Context Protocol 服务器，供已有 SimpleLogin 账号的用户在 MCP 客户端（Codex、Claude Code、Claude Desktop、VS Code、OpenCode）中创建和管理邮件别名、查看别名活动元数据、操作反向别名、管理收件箱与账户设置。支持本地 stdio、Direct Node.js Streamable HTTP 与 Docker Compose 三种运行方式；通过 SL_API_KEY 认证，默认 loopback 监听，非回环启动要求 MCP_AUTH_TOKEN。项目声明与 SimpleLogin/Proton AG 无官方关联；服务器不读取邮件正文，也不代发邮件。

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

- 覆盖别名、联系人/反向别名、收件箱、自定义域名、通知与账户设置的工具目录
- 三种运行方式：本地 stdio、Node.js Streamable HTTP、Docker Compose（GHCR 镜像）
- 支持托管与自托管 SimpleLogin 实例（SL_API_URL 可配置）
- 永久删除需显式确认，大结果读取操作有分页边界

## 适用场景

- 在 MCP 客户端里用对话创建、查找和组织邮件别名
- 审计别名近期活动（转发、回复、拦截、退信元数据）
- 为收件场景创建反向别名路由地址

## 场景标签

 · 领域:邮件隐私/开发者工具

## 证据(README 行号)

> L3: An independent, self-hostable Model Context Protocol server for
> L14: - **Local stdio** is the simplest starting point for one local MCP client. The
> L197: Codex, Claude Code, Claude Desktop, VS Code, and OpenCode. The

## 星数曲线

```mermaid
xychart-beta
    title "enthouan/simplelogin-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b04819086d39` · [字段定义](../../DATASET.md)*
