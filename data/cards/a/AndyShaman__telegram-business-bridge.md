# AndyShaman/telegram-business-bridge

⭐ 18 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AndyShaman/telegram-business-bridge) · [官网](https://ai-handler.com/#telegram-business-bridge) · 个人维护

**通过官方 Business API 把 AI agent 接入个人 Telegram 的 MCP 网关**

由常驻守护进程与 MCP 服务器组成：aiogram 3 轮询 Telegram Business API，将私聊消息持续归档到本地 SQLite（FTS5 全文检索），任何 MCP 客户端可获得 9 个工具（搜索历史、读取上下文与媒体、起草/发送回复等）。默认每条回复需在 Telegram 卡片上人工 ✅ 确认后发出，可选按聊天或全局开启自动发送。面向想给个人 Telegram 加 AI 助手又不想冒 userbot 封号风险的用户；不触碰账号 session，普通免费账户可用，Premium 非必需。群组与频道不在 Business API 覆盖范围内（Telegram 限制）。

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

- 官方 Business API 通道，不使用 MTProto session，权限可在设置中随时撤销
- 9 个 MCP 工具：历史搜索、上下文读取、媒体读取、起草与发送回复等
- 回复默认需人工 ✅ 确认，卡片支持编辑（Mini App 编辑器）与暂停
- 消息内容以 UNTRUSTED 标记包裹的提示注入隔离，MCP 服务器与 bot 令牌隔离

## 适用场景

- 让 Claude Code 等 MCP 客户端读取并搜索我的 Telegram 私聊历史
- 让 AI 助手起草回复，我在 Telegram 里确认或编辑后发送
- 为个人 Telegram 构建带长期记忆的 AI 助手（本地归档作为原始素材）

## 场景标签

`Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L43: The bridge is a standard MCP server. Claude Code
> L73: - 9 MCP tools: `list_chats`, `get_history`, `search_messages`, `get_context`,
> L133: For Claude Code: `claude mcp add telegram -- uv run tg-business-bridge-mcp`

## 星数曲线

```mermaid
xychart-beta
    title "AndyShaman/telegram-business-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f4f49b4ae1f4` · [字段定义](../../DATASET.md)*
