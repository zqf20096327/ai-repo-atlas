# arlanrakh/talk-to-girlfriend-ai

⭐ 548 · Python · Apache-2.0 · 推送 2026-02-03 · [GitHub](https://github.com/arlanrakh/talk-to-girlfriend-ai) · 个人维护

**用 AI 代写并代发 Telegram 恋爱消息的 CLI agent**

基于 Claude Sonnet 的 Telegram 约会助手：TypeScript CLI agent 通过 Python FastAPI 桥接（端口 8765）接入 Telegram API，用自然语言读取消息、代发回复、管理会话；内置 20+ agent 工具与 60+ MCP 工具，可用作 Claude Desktop/Cursor 的独立 MCP 服务器。知识检索用 Nia 语义搜索索引 500+ 搭讪语句与约会指南。需要自备 Telegram API 凭据，支持 Docker 部署，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言读写 Telegram 消息、代发回复与管理会话（20+ agent 工具）
- Nia 语义搜索索引 500+ 搭讪语句与约会指南
- 可作独立 MCP 服务器供 Claude Desktop/Cursor 调用（60+ 工具）
- 提供 Docker 构建与 compose 部署方式

## 适用场景

- 让 AI 基于聊天上下文生成回复建议并代发消息
- 把 Telegram 全功能作为 MCP 工具接入 Claude Desktop/Cursor
- 语义搜索搭讪语句与约会沟通技巧

## 场景标签

`聊天机器人` `AI 助手` `语义搜索` · 领域:对话与助手

## 证据(README 行号)

> L5: An AI-powered Telegram agent that helps you craft witty, engaging messages for your conversations. Built with Claude
> L9: - **Smart Reply Suggestions**: Get AI-powered response suggestions based on conversation context

## 星数曲线

```mermaid
xychart-beta
    title "arlanrakh/talk-to-girlfriend-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 546 --> 549
    line [547, 548, 548]
```

2026-10-18 547 → 2026-10-25 548（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `96b83cdcd324` · [字段定义](../../DATASET.md)*
