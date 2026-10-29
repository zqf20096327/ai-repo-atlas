# guangxiangdebizi/email-mcp

⭐ 17 · TypeScript · ISC · 推送 2026-08-24 · [GitHub](https://github.com/guangxiangdebizi/email-mcp) · [官网](https://www.npmjs.com/package/@xingyuchen/email-mcp) · 个人维护 · 中文 README

**通用多邮箱 MCP 服务：让 AI 客户端收发读搜邮件**

基于 MCP Streamable HTTP 的邮箱服务端，固定提供 5 个工具（send/read/search/delete/reply_email）。读、搜、删走 IMAP，发、回走 SMTP，均兼容 Gmail API 模式；支持 QQ、163、Gmail、Outlook 等邮箱及自建邮箱。多账号通过 EMAIL_ACCOUNTS_JSON 命名配置或 X-Email-* 请求头逐次切换，无需重启。默认仅监听本机回环，跨机器部署要求原生 HTTPS 或可信代理终止 TLS，可选 MCP_API_KEY 鉴权。要求 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固定 5 个工具，读/搜/删走 IMAP、发/回走 SMTP，保留 Gmail API 模式
- 多账号切换：命名账号、account 参数与 X-Email-* 请求头覆盖，无需重启
- 原生 Streamable HTTP MCP，不依赖 SuperGateway 或旧 /sse 协议
- 默认仅监听回环地址；跨机器部署强制 HTTPS，支持 mTLS 与可选 API Key 鉴权

## 适用场景

- 让 MCP 客户端（如 AI 助手）代替我收发和管理多个邮箱
- 个人与工作邮箱在对话中按需切换账号
- 通过 IMAP 搜索语法按发件人、主题、日期查找邮件

## 场景标签

 · 领域:邮件/MCP 服务器

## 证据(README 行号)

> L3: 一个基于 MCP **Streamable HTTP** 的通用邮箱服务。固定提供 5 个工具，支持通过标准
> L50: 这是原生 Streamable HTTP MCP，不再需要 SuperGateway，也不是旧的 `/sse` 协议。
> L182: |工具|用途|主要协议|

## 星数曲线

```mermaid
xychart-beta
    title "guangxiangdebizi/email-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6dba34f2a653` · [字段定义](../../DATASET.md)*
