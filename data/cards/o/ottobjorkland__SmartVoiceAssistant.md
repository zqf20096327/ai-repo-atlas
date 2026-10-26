# ottobjorkland/SmartVoiceAssistant

⭐ 29 · Python · 推送 2026-04-22 · [GitHub](https://github.com/ottobjorkland/SmartVoiceAssistant) · 个人维护

**多语言 AI 语音助手，支持长期记忆，面向终端用户**

基于 OpenAI GPT 模型的个人语音助手：通过 Porcupine 唤醒词、Google STT 语音识别、Google/ElevenLabs TTS 语音合成实现对话，具备多语言支持（瑞典语和英语为主）与长期记忆，可调用 Google 搜索、Wolfram Alpha 等外部工具回答问题。仅 OpenAI API Key 为必需，其余为可选增强。以 Python 源码形式提供，兼容 Windows 与 Raspberry Pi，需手动配置密钥并安装依赖包。

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

- 语音交互链路：Porcupine 唤醒词 + Google STT + Google/ElevenLabs TTS
- 长期记忆与多语言支持（瑞典语/英语为主）
- 通过 function calling 调用 Google 搜索、Wolfram Alpha 等外部工具
- 兼容 Windows 与 Raspberry Pi 运行

## 适用场景

- 在桌面或树莓派上搭建个人语音助手进行问答
- 通过语音调用搜索与计算工具获取信息
- 使用瑞典语或英语进行语音对话交互

## 场景标签

 · 领域:消费级 AI 语音助手

## 证据(README 行号)

> L2: A smart AI voice assistant with multi-language support and long-term memory. Currently best for Swedish and English.
> L8: If you do not want to gather all of this information or do not have time, simply do not save them to the "apiKeys.py

## 星数曲线

```mermaid
xychart-beta
    title "ottobjorkland/SmartVoiceAssistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b15bce8c8ce0` · [字段定义](../../DATASET.md)*
