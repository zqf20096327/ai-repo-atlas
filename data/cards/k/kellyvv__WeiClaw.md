# kellyvv/WeiClaw

⭐ 79 · JavaScript · MIT · 推送 2026-03-24 · [GitHub](https://github.com/kellyvv/WeiClaw) · 个人维护 · 中文 README

**一条命令把微信变成任意 AI Agent 入口的全模态网关**

通过 npx 启动的微信↔AI Agent 双向桥接层：直接调用腾讯 ilinkai 接口收发微信消息，无需 clone 与逆向。支持文本、图片、语音、视频、文件全模态双向传输，可接入任何 OpenAI 兼容 HTTP 接口或 ACP 协议 Agent，内置 Codex/Gemini/Claude Code/OpenCode/OpenClaw 的专属启动参数。支持多 Agent 同时接入并按 @ 前缀路由，Agent 可通过本地 HTTP API 主动推送消息、模拟真人打字节奏。要求 Node.js ≥ 22，语音/视频发送需 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npx 一条命令启动，微信扫码即用，无需 clone
- 文本/图片/语音/视频/文件全模态双向通信
- 多 Agent 同时接入，@ 前缀路由切换
- Agent 通过 localhost:9099 HTTP API 主动推送多条消息

## 适用场景

- 在微信里直接使用 Codex/Gemini/Claude Code 等 CLI Agent
- 把自建的 OpenAI 兼容 Agent 接入微信对话
- Agent 主动向微信用户分多段推送消息

## 场景标签

`聊天机器人` `模型网关` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L85: 微信用户 ←→ 腾讯 ilinkai API ←→ weiclaw ←→ 你的 Agent (HTTP)
> L92: 任何语言，暴露 `POST /v1/chat/completions` 即可：

## 星数曲线

```mermaid
xychart-beta
    title "kellyvv/WeiClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 77 --> 80
    line [78, 79, 79]
```

2026-10-18 78 → 2026-10-28 79（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `23049be4f36a` · [字段定义](../../DATASET.md)*
