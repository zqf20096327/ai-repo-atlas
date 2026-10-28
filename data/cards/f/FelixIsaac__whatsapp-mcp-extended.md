# FelixIsaac/whatsapp-mcp-extended

⭐ 43 · Go · MIT · 推送 2026-10-23 · [GitHub](https://github.com/FelixIsaac/whatsapp-mcp-extended) · 个人维护

**WhatsApp 的 MCP 服务器扩展版：为 AI agent 提供消息、群组与媒体工具**

基于 lharries/whatsapp-mcp 分支链扩展的 Model Context Protocol 服务器，由 Go 桥接层（whatsmeow）+ Python MCP 服务器 + Web UI 三部分组成，供 Claude Desktop、Cursor 等 AI agent 调用。默认暴露 26 个工具，可按 toolset 精简至 15 个，覆盖消息收发、反应、编辑、投票、群组管理、在线状态、频道、媒体下载与历史同步；带 webhook（HMAC-SHA256 签名）、发送白名单安全门。README 声明使用非官方 API 存在封号风险，建议专用号码。

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

- 26 个默认工具 / 15 个精简工具的 toolset 门控机制
- 支持 8 位手机配对码，无需扫码；会话自动重连
- webhook 系统支持按 JID/关键词/媒体类型触发，HMAC-SHA256 签名
- WHATSAPP_ALLOWLIST_JIDS 发送白名单安全门

## 适用场景

- 让 Claude Desktop/Cursor 等 agent 直接读写 WhatsApp 消息与联系人
- 通过 webhook 将收到的 WhatsApp 消息实时推送到外部系统
- 用 AI agent 管理 WhatsApp 群组、投票与频道

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: An extended Model Context Protocol (MCP) server for WhatsApp with a toolset-gated, agent-facing surface for messagin
> L163: * **Composable Primitives:** High-level AI features (voice-to-text transcription, vector database semantic recall,

## 星数曲线

```mermaid
xychart-beta
    title "FelixIsaac/whatsapp-mcp-extended 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-26", "2026-10-28"]
    y-axis "stars" 38 --> 44
    line [39, 40, 41, 43, 43]
```

2026-10-18 39 → 2026-10-28 43（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `009ed5764a4b` · [字段定义](../../DATASET.md)*
