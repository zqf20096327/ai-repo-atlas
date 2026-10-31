# HectorPulido/Deeplearning-based-Twitch-bot

⭐ 30 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/HectorPulido/Deeplearning-based-Twitch-bot) · [官网](https://pequesoft.net) · 个人维护

**基于 Transformers 的 Twitch 聊天机器人，带情感分析与 TTS**

用 TwitchIO 连接 Twitch、用 Hugging Face Transformers 生成回复的聊天机器人，README 提及 Llama2 技术与 gpt2-medium、dialogpt-large 模型的示例对话。功能包括命令与链接、聊天机器人个性、西语翻译、随机定时消息、词黑名单、订阅与 bits 消息、自定义函数、基于 Vader 的表情情感分析、pyttsx3 文字转语音及频道积分自定义奖励。通过 .env 配置凭据，提供 Docker 构建运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 使用 Hugging Face Transformers 生成聊天回复（示例含 gpt2-medium、dialogpt-large）
- Vader 情感分析驱动表情回应
- pyttsx3 文字转语音（读消息、读自身回复、订阅感谢）
- 支持频道积分自定义奖励触发 TTS 等功能

## 适用场景

- 主播在 Twitch 频道部署自动聊天机器人
- 通过频道积分奖励触发 TTS 或额外命令
- 对聊天表情做情感分析并回应

## 场景标签

`聊天机器人` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: This is a twitch chatbot made with Twitchio for the twitch connection and Transformers from Huggingface.
> L66: Using Vader sentiment analysis tool the chatbot is capable to response with emotes in the chat

## 星数曲线

```mermaid
xychart-beta
    title "HectorPulido/Deeplearning-based-Twitch-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `34b74064941b` · [字段定义](../../DATASET.md)*
