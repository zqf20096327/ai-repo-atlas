# dzaczek/ava

⭐ 19 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/dzaczek/ava) · 个人维护

**接听来电的 AI 语音助理：用类人角色通话并经 Signal 实时干预**

基于 FastAPI（Python 3.11）的电话应答服务：通过 Twilio 接入 PSTN 通话与 STT，用 LLM（OpenAI 或 Groq 后端）生成对话，ElevenLabs 多语种 TTS 输出语音（OpenAI TTS 作后备）；机主经 Signal 收到通话摘要与紧急度标记，可中途发送指令（如转告、询问、结束通话）。限制：Twilio STT 每次 Gather 仅支持一种语言，靠 GPT 分析后在下一轮切换；每通电话上限 10 轮对话。以 Docker Compose 部署，含 Caddy/Cloudflare Tunnel 两种暴露配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Twilio PSTN + STT、LLM 对话、ElevenLabs 多语种 TTS 的完整通话链路
- Signal 实时通道：机主可中途注入指令，另带 11 个斜杠命令（/status、/billings 等）
- 按 52 个电话号码前缀检测语言并在轮次间切换
- GPT 响应末尾的 meta 块控制挂断、紧急度、话题与语言切换

## 适用场景

- 无法接听时由 AI 助理代接并按设定角色应对
- 机主通过 Signal 远程监听通话进度并下达实时指令
- 筛选来电类型（招聘/医疗/IT 故障/推销）并按规则处理

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: > **AVA** answers your calls when you can't, holds a natural conversation with a human-like persona, and keeps you i
> L12:         Twilio["Twilio<br/>Voice / PSTN<br/>STT (Gather)<br/>Record<br/>Webhooks"]

## 星数曲线

```mermaid
xychart-beta
    title "dzaczek/ava 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a50ac93fa799` · [字段定义](../../DATASET.md)*
