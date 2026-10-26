# alexogeny/cortana

⭐ 53 · Python · 推送 2026-06-22 · [GitHub](https://github.com/alexogeny/cortana) · 个人维护

**给个人用户的 Python 语音 AI 助手库：Whisper 转写+GPT 对话+TTS 回答**

Python 库形式的个人 AI 助手：通过 openai-whisper 做语音转文字，将文本发给 GPT（默认 gpt-4，可改 gpt-3.5-turbo）生成回复，再经 ElevenLabs 或 60db（TTS_PROVIDER 可配）合成语音播放。助手模式带热词检测，仅响应含热词的指令；聊天记录保存到 /chats 目录。安装依赖 pipenv，API key 与声音配置写入 .env。当前不支持流式播放（整段生成后播放），也暂无法识别不含热词的连续对话。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 语音转写 + GPT 生成回复 + ElevenLabs/60db 双 TTS 提供商的可切换管线
- 助手模式支持热词检测激活
- 聊天记录保存到 /chats 文件夹，声音列表本地缓存以减少 API 调用
- Whisper 模型大小可在 tiny/small/medium 间调整

## 适用场景

- 用麦克风与 AI 助手进行语音对话并获得语音回答
- 命令行直接与 GPT 聊天
- 用不同克隆声音进行文字转语音

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L8: - creating a personal assistant with whisper, GPT, and your chosen TTS provider
> L22: Cortana uses whisper to do speech to text, and then uses GPT to generate a response. It then uses a text-to-speech 

## 星数曲线

```mermaid
xychart-beta
    title "alexogeny/cortana 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2e124cc0acc2` · [字段定义](../../DATASET.md)*
