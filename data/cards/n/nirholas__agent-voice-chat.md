# nirholas/agent-voice-chat

⭐ 19 · JavaScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/nirholas/agent-voice-chat) · [官网](https://github.com/nirholas/agent-voice-chat) · 个人维护

**在网站中加入多 AI 语音对话的 TypeScript SDK 与服务**

面向开发者的多 agent 实时语音对话工具链：用户对麦克风说话，多个带独立人设与音色的 AI agent 轮流收听、思考并回应。提供自托管 Node.js 服务、可用单个 script 标签嵌入任意网站的组件，以及 React/Vue 组件（后者尚未发布到 npm）。LLM 支持 OpenAI Realtime/Chat、Claude、Groq；TTS 支持 OpenAI、ElevenLabs、浏览器原生；通过 WebRTC（约 200ms）或服务端 STT→LLM→TTS 管道两种路径实现，服务端轮转队列管理多 agent 发言。许可证为保留所有权利。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebRTC 实时路径（OpenAI Realtime）与服务端 STT→LLM→TTS 管道两种实现
- 多 agent 轮转队列与房间级多租户隔离
- 单 script 标签嵌入任意网站的可挂载组件
- 通过 agents.config.json 定义 agent 人设、音色与头像

## 适用场景

- 在我的网站上添加一个浮动的多 agent 语音对话入口
- 搭建多角色 AI 主播或语音助手房间
- 用 React/Vue 组件集成实时语音 agent

## 场景标签

`语音 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Add multi-agent AI voice conversations to any website in minutes
> L15: - **Flexible audio pipeline** — STT + LLM + TTS for non-realtime providers
> L151: ├── server.js                 # Express + Socket.IO server

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/agent-voice-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4673101c9b97` · [字段定义](../../DATASET.md)*
