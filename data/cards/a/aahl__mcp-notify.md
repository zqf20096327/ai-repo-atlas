# aahl/mcp-notify

⭐ 29 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/aahl/mcp-notify) · 个人维护 · 中文 README

**消息推送 MCP 服务器：让 AI 客户端向微信/钉钉/Telegram 等发通知**

基于 Model Context Protocol 的消息推送服务器，供 Cursor、VS Code、Claude Code、OpenAI CodeX、Cherry Studio 等 MCP 客户端调用。支持企业微信（群机器人与应用号）、钉钉、飞书/Lark、Telegram、Bark、Ntfy、PushPlus、Home Assistant 共十余种推送渠道，通过环境变量配置各渠道凭证，暴露文本/图片/音视频/文件等发送工具。提供 uvx、Smithery 与 Docker 三种安装方式，另有 fastmcp.cloud、smithery.ai 在线体验。

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

- 覆盖企业微信/钉钉/飞书/Telegram/Bark/Ntfy/PushPlus/Home Assistant 等多渠道推送
- 按渠道拆分的发送工具（文本/图片/音视频/文件/图文）
- uvx、Smithery、Docker 三种安装途径
- 各渠道通过环境变量配置凭证，部分参数可在提示词中指定

## 适用场景

- 让 Claude Code/Cursor 等 AI 客户端在任务完成或异常时推送通知到我手机
- AI 助手直接向企业微信群、钉钉群或 Telegram 发送消息
- 配合 Home Assistant 触发移动设备通知

## 场景标签

 · 领域:消息推送/AI 工具集成

## 证据(README 行号)

> L5: 提供消息推送的 MCP (Model Context Protocol) 服务器，支持企业微信、钉钉、Telegram、Bark、Lark、飞书、Home Assistant
> L47: - 添加到 Claude Code, 执行命令: `claude mcp add notify -- uvx mcp-notify`

## 星数曲线

```mermaid
xychart-beta
    title "aahl/mcp-notify 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-28 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `22aa91476ade` · [字段定义](../../DATASET.md)*
