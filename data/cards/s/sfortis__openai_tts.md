# sfortis/openai_tts

⭐ 221 · Python · GPL-3.0 · 推送 2026-10-11 · [GitHub](https://github.com/sfortis/openai_tts) · 个人维护

**Home Assistant 文字转语音集成，接入多家 OpenAI 兼容语音服务**

面向 Home Assistant 用户的 TTS 集成：通过 OpenAI speech API 调用 OpenAI、Mistral、Groq、Lemonfox、OpenRouter 或自托管后端（Kokoro-FastAPI、Chatterbox、LocalAI 等），以预设自动填充端点、模型与语音列表。功能包括多语音配置、六种音频格式、流式播放、响度归一化、每档案增益、播报前提示音，以及按实体/设备/区域/楼层定位的播报，播报后恢复音量与音乐。README 声明 OpenAI 三个 TTS 模型将于 2027 年 1 月停用，届时 OpenAI 档案需迁移到其他提供商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 类提供商预设自动填充端点、模型与语音
- 流式播放、逐句流式、响度归一化与 -12~+12 dB 增益
- 播报按实体/设备/区域/楼层/标签定位并恢复音量与音乐
- 5 种内置提示音并支持自定义 mp3 提示音

## 适用场景

- 让 Home Assistant 用云端或自托管服务朗读文本
- 语音助手（Assist pipeline）的语音输出
- 在家中多个音箱播报通知并自动恢复音乐

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: **Text-to-speech for Home Assistant from OpenAI, Mistral, Groq, Lemonfox, Kokoro, Chatterbox or any server that impl
> L14: OpenAI TTS is a text-to-speech integration for Home Assistant that works with any service implementing the OpenAI s
> L119: - Announcements on any media player, targeted by entity, device, area, floor or label.

## 星数曲线

```mermaid
xychart-beta
    title "sfortis/openai_tts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 219 --> 222
    line [220, 221, 221]
```

2026-10-18 220 → 2026-10-23 221（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1cbe69300a33` · [字段定义](../../DATASET.md)*
