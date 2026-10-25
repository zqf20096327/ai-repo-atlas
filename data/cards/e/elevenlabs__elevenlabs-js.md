# elevenlabs/elevenlabs-js

⭐ 446 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/elevenlabs/elevenlabs-js) · [官网](https://elevenlabs.io) · 组织维护

**ElevenLabs 官方 Node.js SDK：接入其文本转语音与语音 Agent API**

ElevenLabs 官方 TypeScript/Node SDK，封装其 HTTP API：文本转语音（流式生成）、语音列表查询，以及 Speech Engine——通过 WebSocket 连接让开发者在自有服务器接入自选 LLM 构建语音 Agent，ElevenLabs 负责语音侧，自动校验请求签名。内置指数退避自动重试（默认 2 次）、可配置超时（默认 60 秒），支持 Node.js 15+/Vercel/Cloudflare Workers/Deno/Bun 运行时。播放音频需系统安装 MPV 与 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本转语音含实时流式输出，覆盖 Multilingual/Flash/Turbo v2.5 等模型
- Speech Engine：WebSocket 连接接入自选 LLM 构建语音 Agent，支持附加到现有 HTTP 服务器或独立运行
- 自动重试（指数退避）与可配置超时
- 支持 Node.js 15+/Vercel/Cloudflare Workers/Deno v1.25+/Bun 1.0+ 运行时

## 适用场景

- 在 Node 应用中集成 ElevenLabs 的文本转语音能力
- 为已有聊天 Agent 添加语音交互（Speech Engine）
- 通过 API 查询与管理可用语音

## 场景标签

`语音合成` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L12: The official Node SDK for ElevenLabs. ElevenLabs brings the most compelling, rich and lifelike voices to creators a
> L88: Speech Engine lets you build voice-powered AI agents with a custom LLM or add voice to your existing chat agent. Th

## 星数曲线

```mermaid
xychart-beta
    title "elevenlabs/elevenlabs-js 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 445 --> 448
    line [446, 447, 446]
```

2026-10-18 446 → 2026-10-25 446（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9a098c863d38` · [字段定义](../../DATASET.md)*
