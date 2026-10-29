# thehwang/Scripta

⭐ 19 · Swift · MIT · 推送 2026-09-29 · [GitHub](https://github.com/thehwang/Scripta) · [官网](https://dev.to/thehwang/building-a-100-local-meeting-transcription-app-for-macos-with-whispercpp-and-screencapturekit-33m7) · 个人维护

**macOS 本地双通道会议转写与 AI 摘要应用**

macOS 原生应用，会议中同时采集麦克风（whisper.cpp、Metal 加速）与系统音频（Apple SFSpeechRecognizer），实时双通道转写，并通过本地 Ollama 生成要点/行动项摘要与多轮对话问答；macOS 15+ 可实时双语翻译。全部处理在本机完成，无需账号与联网（首次模型下载除外）。支持定时录制、历史搜索、悬浮字幕条。需 macOS 14+、Ollama，约 2 GB 磁盘存模型；需授予麦克风、屏幕录制、语音识别权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双通道实时转写：whisper.cpp（麦克风）+ Apple SFSpeechRecognizer（系统音频），支持 10+ 语言
- Ollama 本地生成要点/行动项摘要与多轮流式对话
- 定时录制、命名会话历史搜索、悬浮字幕模式
- 实时双语翻译（macOS 15+，Apple Translation 框架）

## 适用场景

- 会议中同时记录我的发言和对方音频并生成摘要
- 会后针对转写文本用自然语言提问
- 不想让会议录音上云的隐私敏感场景

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L47: Scripta is a native macOS app that captures **both your microphone and system audio** during meetings, transcribes 
> L49: - **Mic** transcription powered by whisper.cpp (Metal-accelerated, on-device)
> L51: - **AI summaries & chat** via Ollama (local LLM)

## 星数曲线

```mermaid
xychart-beta
    title "thehwang/Scripta 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `91b77011494e` · [字段定义](../../DATASET.md)*
