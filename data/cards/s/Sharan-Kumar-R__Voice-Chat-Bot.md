# Sharan-Kumar-R/Voice-Chat-Bot

⭐ 80 · Python · 推送 2026-06-05 · [GitHub](https://github.com/Sharan-Kumar-R/Voice-Chat-Bot) · 个人维护

**实时语音对话机器人：Deepgram 语音 + Groq LLaMA3 对话**

基于 Python 的实时语音会话助手：麦克风输入经 Deepgram STT 实时转录为文本，由 Groq 上的 LLaMA3（经 LangChain 接入）生成回答，再经 Deepgram TTS 用 ffplay 播放语音回复；另有文本聊天机器人脚本。需要自行配置 Groq 与 Deepgram API key，并预先安装 FFmpeg；从源码克隆运行，通过编辑 Bot_prompt.txt 自定义模型名称与功能定位。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Deepgram STT 实时转录麦克风输入
- Groq LLaMA3（经 LangChain）生成对话回答
- Deepgram TTS 输出自然语音（ffplay 播放）
- 通过 Bot_prompt.txt 自定义机器人行为

## 适用场景

- 我想和语音助手实时对话获得语音回答
- 我想定制一个有自己名字和角色设定的语音机器人
- 我想参考 STT↔LLM↔TTS 链路搭建自己的语音助手

## 场景标签

`语音 Agent` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13:  🧠 Groq’s LLaMA3 (via LangChain) for ultra-fast, high-quality conversational intelligence
> L15:  🎙️ Deepgram STT (Speech-to-Text) for real-time transcription from microphone input
> L17:  🗣️ Deepgram TTS (Text-to-Speech) for fast and natural voice responses using ffplay

## 星数曲线

```mermaid
xychart-beta
    title "Sharan-Kumar-R/Voice-Chat-Bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-26 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9a248b1a748b` · [字段定义](../../DATASET.md)*
