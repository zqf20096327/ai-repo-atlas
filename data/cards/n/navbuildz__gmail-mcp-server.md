# navbuildz/gmail-mcp-server

⭐ 16 · TypeScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/navbuildz/gmail-mcp-server) · 组织维护

**给 AI agent 用的多账户 Gmail MCP 服务器：读写邮件、归档、打标、退订**

开源的 Model Context Protocol 服务器，向 MCP 客户端（Claude、Cursor、Windsurf、Cline、Continue 等）暴露 9 个 Gmail 工具：搜索/读取邮件、归档、打标签、建草稿、发信、批量分诊与自动退订（支持 List-Unsubscribe 头、mailto 与正文链接扫描）。支持连接多个 Gmail 账户并可按单账户或 all 查询。通过 Google OAuth 2.0 授权，refresh token 以 AES-256-GCM 加密存储，仅申请 gmail.readonly 与 gmail.modify scope。部署方式含 Vercel、Railway、自托管与 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个工具覆盖读写、归档、标签、草稿、发信与批量分诊
- 多 Gmail 账户连接，工具级 account 参数可查单账户或 all
- 自动退订：RFC 8058 one-click POST、mailto 链接与正文链接扫描
- OAuth 2.0 + AES-256-GCM 加密 token 存储，最小 Gmail scopes

## 适用场景

- 让 Claude/Cursor 等 AI 客户端代管我的多个 Gmail 收件箱
- 用自然语言批量归档促销邮件、退订 newsletter
- AI 辅助邮件分诊：批量拉取邮件并执行归档/打标

## 场景标签

 · 领域:AI Agent 工具/邮件自动化

## 证据(README 行号)

> L5: An open-source Model Context Protocol (MCP) server that gives AI agents and assistants full read and write access to
> L37: Model Context Protocol (MCP) is an open standard that lets AI agents and assistants connect to external tools and d

## 星数曲线

```mermaid
xychart-beta
    title "navbuildz/gmail-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `17751e62f8ad` · [字段定义](../../DATASET.md)*
