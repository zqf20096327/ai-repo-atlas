# profclaw/profclaw

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-10-05 · [GitHub](https://github.com/profclaw/profclaw) · [官网](https://profclaw.ai) · 组织维护

**开发者自托管的 AI agent 引擎：35 家 LLM、22 个聊天渠道**

本地优先的自托管 AI agent 引擎，面向开发者。接入 35 个 AI 提供商（含 Ollama 全离线、LM Studio），内置 72 个工具（文件操作、git、浏览器自动化、cron、语音等）、50 个 Markdown 技能文件，并提供带流式 Markdown 与模型切换的终端 TUI。支持 22 个聊天渠道（Slack、Discord、飞书、企业微信等），任务队列基于 BullMQ + Redis（pico/mini 模式用内存回退）。三种部署模式 pico/mini/pro，pico 可在树莓派 Zero 2W 上以约 140MB 内存运行。要求 Node.js 22+，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35 个 AI 提供商接入，含 Ollama 全离线模式
- 72 个内置工具与 50 个 Markdown 技能（斜杠命令）
- 22 个聊天渠道（Slack/Discord/飞书/企业微信等）
- pico/mini/pro 三档部署模式，pico 约 140MB 内存

## 适用场景

- 在自有服务器或树莓派上运行本地 AI 助手
- 通过 Slack/Discord/Telegram 等渠道接入 AI agent
- 在 CI 或脚本中无头调用 agent 完成代码任务
- 作为 MCP server 供 Claude Desktop、Cursor 等 MCP 客户端使用

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Self-hosted AI agent engine for developers.
> L32: - 35 AI providers, including Ollama for fully offline usage.
> L58: npm install -g profclaw

## 星数曲线

```mermaid
xychart-beta
    title "profclaw/profclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `09aafd9b7f1c` · [字段定义](../../DATASET.md)*
