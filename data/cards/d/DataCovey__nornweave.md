# DataCovey/nornweave

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/DataCovey/nornweave) · [官网](https://nornweave.datacovey.com/) · 个人维护

**为 AI Agent 提供的自托管收件箱即服务（Inbox-as-a-Service）API**

自托管的邮件 API 服务：将 Mailgun、SES、SendGrid、Resend 等标准邮件服务商或 IMAP/SMTP 邮箱包装为面向 LLM 的有状态收件箱服务，提供虚拟收件箱创建、Webhook/IMAP 收信、会话线程化分组、HTML 转 Markdown、LLM 线程摘要（OpenAI/Anthropic/Gemini）、pgvector 语义搜索、附件文本提取与限流、多租户。通过 REST API 与 MCP 服务器（可接入 Claude、Cursor 等 MCP 客户端）暴露能力，支持 SQLite/PostgreSQL 存储，以 pip 包与 Docker 方式部署，附带 Python 客户端 SDK 与 n8n 节点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将邮件服务商转为面向 LLM 的有状态收件箱 API（REST + MCP）
- 线程化分组、HTML 转 Markdown、LLM 线程摘要（OpenAI/Anthropic/Gemini）
- pgvector 语义搜索与附件文本提取
- 支持 Mailgun/SES/SendGrid/Resend/IMAP-SMTP 五类收发通道

## 适用场景

- 为 AI Agent 分配独立邮箱并程序化收发邮件
- 让 Claude/Cursor 等 MCP 客户端通过 wait_for_reply 等工具处理邮件会话
- 把现有邮箱经 IMAP 接入为 LLM 可读的线程上下文

## 场景标签

 · 领域:AI 基础设施/邮件服务

## 证据(README 行号)

> L8:  Open-source, self-hosted Inbox-as-a-Service API for AI Agents
> L15: Standard email APIs are stateless and built for transactional sending. **NornWeave** adds a **stateful layer** (Inb
> L137: NornWeave exposes an MCP server for direct integration with Claude, Cursor, and other MCP-compatible clients.

## 星数曲线

```mermaid
xychart-beta
    title "DataCovey/nornweave 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `86f53702a32d` · [字段定义](../../DATASET.md)*
