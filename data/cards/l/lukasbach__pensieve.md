# lukasbach/pensieve

⭐ 117 · TypeScript · 推送 2026-05-30 · [GitHub](https://github.com/lukasbach/pensieve) · [官网](https://pensieve.lukasbach.com/) · 个人维护

**本地录音并转录、总结会议的桌面应用**

Pensieve 是一个本地优先的桌面应用，从本机运行的应用中录制会议、讨论或语音备忘，随后用内置 Whisper 实例在本地转录音频，并可选用 LLM 生成摘要。摘要可通过连接本地 Ollama 实例完成，也可提供 OpenAI key 使用 ChatGPT；选择 Ollama 或关闭摘要时数据不离开本机。附带聊天视图用于对录音提问，内置 MCP 服务器供外部工具集成，托盘常驻后台随时启停录制。以安装包形式发布，macOS 需额外安装 FFmpeg 与 Whisper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Whisper 实例本地转录录音
- 可选 Ollama 本地摘要，数据不出本机
- 聊天视图可针对录音提问
- 内置 MCP 服务器对接外部工具

## 适用场景

- 录制并回溯会议或语音备忘
- 对历史录音提问检索讨论内容
- 在不上传数据的前提下获得会议转录与摘要

## 场景标签

`语音识别` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L17: Pensieve is a local-only desktop app for recording meetings, discussions, memos or other audio
> L23: It uses a bundled Whisper instance to transcribe the audio locally, and optionally

## 星数曲线

```mermaid
xychart-beta
    title "lukasbach/pensieve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-31 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7fb27dc3b37e` · [字段定义](../../DATASET.md)*
