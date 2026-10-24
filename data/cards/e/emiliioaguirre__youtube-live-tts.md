# emiliioaguirre/youtube-live-tts

⭐ 56 · TypeScript · Apache-2.0 · 推送 2026-04-14 · [GitHub](https://github.com/emiliioaguirre/youtube-live-tts) · 个人维护

**YouTube 直播弹幕实时转语音工具，调用 ElevenLabs 语音**

面向主播的直播工具：实时监听 YouTube 直播聊天消息，经消息队列防重叠后调用 ElevenLabs API 将弹幕转换为语音播放，支持自定义 "{author} says: {message}" 模板、每用户冷却与长度限制的反刷屏、Web 仪表盘配置监控、英文/西语界面与 Windows/macOS/Linux 运行。技术栈为 FastAPI 后端 + Next.js 前端，需自备 ElevenLabs API key，依赖 Python 3.12 与 Bun 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时监听 YouTube 直播聊天并转为语音
- 消息队列防止音频重叠，支持每用户冷却与长度限制
- Web 仪表盘配置与监控，英文/西语双语界面
- 自定义 "{author} says: {message}" 播报模板

## 适用场景

- 直播时让弹幕内容自动读出来
- 通过 Web 界面配置播报模板与防刷屏规则
- 跨 Windows/macOS/Linux 在本地运行直播语音工具

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: Let your chat speak for itself. Real-time text-to-speech for YouTube live streams, powered by ElevenLabs.
> L10: - **AI-powered voices:** High-quality TTS with ElevenLabs API

## 星数曲线

```mermaid
xychart-beta
    title "emiliioaguirre/youtube-live-tts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-24 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b66aba5d2a40` · [字段定义](../../DATASET.md)*
