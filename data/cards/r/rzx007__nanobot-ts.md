# rzx007/nanobot-ts

⭐ 14 · TypeScript · MIT · 推送 2026-03-24 · [GitHub](https://github.com/rzx007/nanobot-ts) · 个人维护 · 中文 README

**超轻量个人 AI 助手框架的 TypeScript 实现（多渠道接入）**

nanobot 的 TypeScript 版本，约 5000 行代码，运行于 Bun 1.3+，以 monorepo 组织 10+ 包。核心是事件驱动架构：消息总线、Agent 循环、工具注册、基于风险的工具审批、会话记忆整合与定时任务。支持 WhatsApp（baileys）、飞书（WebSocket 长连接、无需公网 IP）、Email（IMAP/SMTP）、CLI 四个渠道，LLM 接入基于 Vercel AI SDK（OpenAI/Anthropic/OpenRouter/Google/DeepSeek/Groq 等），支持 MCP 工具（stdio/HTTP）、subagent 后台任务与 React Web 管理面板。提供 TUI 终端界面与 CLI 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WhatsApp/飞书/Email/CLI 四渠道消息接入，飞书用 WebSocket 无需公网 IP
- 基于风险分级的工具审批系统（高/中/低风险，可按工具覆盖）
- MCP 支持（stdio/HTTP 服务器、OAuth）与 subagent 双模式后台任务（embedded/isolated）
- 内置文件读写、shell 执行、web 搜索/抓取、定时任务等 12 个工具

## 适用场景

- 通过 WhatsApp/飞书/Email 等聊天渠道运行个人 AI 助手
- 用终端 TUI 或 CLI 与本地 AI 助手对话并执行工具
- 经 MCP 接入外部工具扩展助手能力
- 定时任务与后台 subagent 处理长时任务

## 场景标签

`AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: nanobot-ts is the TypeScript version of nanobot, an ultra-lightweight personal AI assistant framework.
> L17: - 🧠 **Smart**: LLM-driven with tool calling
> L283: Supported providers (powered by Vercel AI SDK):

## 星数曲线

```mermaid
xychart-beta
    title "rzx007/nanobot-ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `24aca53ff4fc` · [字段定义](../../DATASET.md)*
