# jlucaso1/whatsapp-mcp-ts

⭐ 75 · TypeScript · 推送 2026-01-23 · [GitHub](https://github.com/jlucaso1/whatsapp-mcp-ts) · 个人维护

**把个人 WhatsApp 账号接入 AI 客户端的 MCP 服务器**

基于 TypeScript 与 @whiskeysockets/baileys 库构建的 Model Context Protocol（MCP）服务器：通过 WhatsApp Web 多设备 API 连接个人 WhatsApp 账号，向 Claude Desktop、Cursor、Cline、Roo Code 等 MCP 客户端暴露 6 个工具（搜索联系人、列出聊天、获取消息历史、获取消息上下文、发送消息、获取聊天详情）。消息与认证凭据本地存储于 SQLite 数据库与 auth_info 目录，数据仅在 AI agent 调用工具时发送。需 Node.js ≥23.10.0，首次运行扫码认证。

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

- 6 个 MCP 工具：联系人/聊天/消息查询与消息发送
- 基于 Baileys 连接 WhatsApp Web 多设备 API，扫码认证
- 消息与凭据本地 SQLite 存储，仅在工具调用时传出数据
- 支持 Smithery 一键安装及手动源码安装

## 适用场景

- 让 Claude 或 Cursor 中的 AI 助手搜索和读取我的 WhatsApp 消息
- 通过对话让 AI 代为发送 WhatsApp 消息
- 本地保留聊天数据的前提下接入 AI 客户端

## 场景标签

 · 领域:AI 客户端集成/即时通讯

## 证据(README 行号)

> L4: This is a Model Context Protocol (MCP) server for WhatsApp, built with TypeScript and using the `@whiskeysockets/bai
> L145: 3. Runs an MCP server using `@modelcontextprotocol/sdk` that listens for requests from an AI client over standard 

## 星数曲线

```mermaid
xychart-beta
    title "jlucaso1/whatsapp-mcp-ts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 73 --> 76
    line [74, 75, 75]
```

2026-10-18 74 → 2026-10-24 75（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `138ef4f39b99` · [字段定义](../../DATASET.md)*
