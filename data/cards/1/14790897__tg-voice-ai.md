# 14790897/tg-voice-ai

⭐ 251 · TypeScript · 推送 2026-06-14 · [GitHub](https://github.com/14790897/tg-voice-ai) · [官网](https://t.me/tg_voice_ai_bot) · 个人维护 · 中文 README

**Telegram 语音对话机器人：语音/文字进，语音+文字回复**

部署在 Cloudflare Workers 上的 Telegram 机器人：接收语音或文字消息，经 Whisper 模型转录，由 Llama 类对话模型生成回复，再经 TTS（MeloTTS/SiliconFlow GPT-SoVITS/Deepgram Aura 可选）合成语音，返回语音+文字双形式回复。作者提供已部署实例，也可自部署：pnpm 安装依赖、wrangler 部署、配置 Telegram token 等环境变量并访问 /init 注册 webhook。所用模型可在代码中修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音输入经 Whisper 转录后由对话模型生成回复
- 三种 TTS 后端可选（workers/siliconflow/deepgram）
- 运行于 Cloudflare Workers，提供已部署实例可直接使用
- 模型路径可在代码中修改

## 适用场景

- 与 Telegram 机器人进行语音或文字对话
- 自部署一个私有语音聊天机器人
- 在代码中替换为自己的对话/语音模型

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: 发送语音或者文字，收到语音+文字的聊天回复
> L40:    const WHISPER_MODEL = '@cf/openai/whisper-large-v3-turbo'; // Whisper model path
> L41:    const CHAT_MODEL = '@cf/meta/llama-4-scout-17b-16e-instruct'; // Chat model path

## 星数曲线

```mermaid
xychart-beta
    title "14790897/tg-voice-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 250 --> 252
    line [251, 251]
```

2026-10-18 251 → 2026-10-24 251（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0ab3a80a41a8` · [字段定义](../../DATASET.md)*
