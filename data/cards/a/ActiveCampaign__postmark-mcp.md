# ActiveCampaign/postmark-mcp

⭐ 60 · JavaScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ActiveCampaign/postmark-mcp) · [官网](https://postmarkapp.com/lp/mcp) · 组织维护

**官方 Postmark MCP 服务器：让 AI 助手发送与诊断邮件**

ActiveCampaign 官方维护的 Model Context Protocol 服务器，把 Postmark 事务邮件账户接入 Claude Desktop、Cursor 等 MCP 客户端。提供 24 个工具，覆盖邮件发送（单个、批量最多 500 封、模板发送）、模板 CRUD 与校验、出站邮件搜索、退信/抑制名单/统计/服务器信息/Webhook 管理，以及组合多个 API 调用给出投递诊断建议的 diagnoseDelivery。通过 MCP 工具注解区分只读与破坏性操作，供客户端自动批准或要求确认。需 Node.js v20 与 Postmark 账户，支持 npx 直接运行或源码部署，凭环境变量配置。

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

- 24 个工具覆盖发送、模板、搜索、退信、抑制名单、统计与 Webhook
- diagnoseDelivery 组合诊断工具：判断邮件是否送达并给出建议
- MCP 工具注解区分只读/破坏性操作，支持客户端审批策略
- 支持 npx 免克隆运行，日志默认部分掩码邮箱地址

## 适用场景

- 在 Claude/Cursor 等客户端中直接发送和模板化事务邮件
- 排查邮件是否送达、为何被退信或抑制
- 通过对话管理邮件模板与 Webhook

## 场景标签

 · 领域:开发工具/邮件服务集成

## 证据(README 行号)

> L3: Send emails with Postmark using Claude and other MCP-compatible AI assistants.
> L10: - Exposes a Model Context Protocol (MCP) server backed by your Postmark account
> L139: Both snippets work with **Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`), **

## 星数曲线

```mermaid
xychart-beta
    title "ActiveCampaign/postmark-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-27"]
    y-axis "stars" 57 --> 61
    line [58, 59, 60, 60]
```

2026-10-18 58 → 2026-10-27 60（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ff851b27e765` · [字段定义](../../DATASET.md)*
