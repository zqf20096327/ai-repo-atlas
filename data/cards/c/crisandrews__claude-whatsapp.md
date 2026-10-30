# crisandrews/claude-whatsapp

⭐ 16 · TypeScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/crisandrews/claude-whatsapp) · [官网](https://github.com/crisandrews/claude-whatsapp#quick-setup) · 个人维护

**把 WhatsApp 号码接入 Claude Code 的通道插件**

基于 Baileys 的 WhatsApp 通道插件，运行于 Claude Code 插件生命周期内，将个人 WhatsApp 号码变成可通过消息对话的 Claude Code agent。提供 QR/配对码链路、配对码+白名单+群组门控的访问控制、工具权限请求转发到手机（👍/👎 审批）、本地 SQLite+FTS5 全文检索与导出、默认本地 Whisper 语音转写（99+ 语言，可选 Groq/OpenAI 云端）、媒体自动下载管道，共暴露 52 个 MCP 工具。限制：无 Claude Code 之外的独立安装路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QR 扫码或无头服务器配对码两种号码绑定方式
- 配对码/白名单/群组门控与按聊天的历史隔离作用域
- 工具权限请求转发至 WhatsApp，用表情回应或回复审批
- 默认本地 Whisper 语音转写，无需 API key，支持 99+ 语言
- 消息本地索引（SQLite+FTS5），支持全文检索与 markdown/jsonl/csv 导出

## 适用场景

- 通过自己的 WhatsApp 号码随时与 Claude Code agent 对话
- 远程审批 Claude 的工具运行请求
- 把 WhatsApp 群组接入带访问控制的 AI 助手
- 对 WhatsApp 聊天记录做本地检索与导出

## 场景标签

`编码 Agent` `AI 助手` `语音识别` · 领域:编码与开发

## 证据(README 行号)

> L21: This plugin fills that gap. It connects your WhatsApp number directly to Claude Code, turning it into a fully funct
> L199: - Standalone install path (Smithery / non-Claude-Code MCP clients) — the plugin currently runs only inside Claude 

## 星数曲线

```mermaid
xychart-beta
    title "crisandrews/claude-whatsapp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cd915981c12e` · [字段定义](../../DATASET.md)*
