# kcitlyn/PolyScribe

⭐ 16 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/kcitlyn/PolyScribe) · 个人维护

**完全离线的实时语音转写与翻译桌面工具**

基于 Vosk 与 Argos Translate 的桌面应用：实时离线语音识别、口语翻译到 20+ 语言、文本转语音输出。内置模型管理器，可下载 76 个 Vosk 模型与 Argos 翻译包（34 种语言），支持音频文件转写（WAV/MP3 等，经 ffmpeg）、自动语言检测、导出 txt/srt/json、会话历史与悬浮字幕窗。提供 Tkinter GUI（8 主题）与终端模式，另有进行中的 Raspberry Pi 移植。限制：需 Python 3.11，TTS 语音依赖各操作系统自带或另行安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Vosk 驱动的完全离线实时语音识别
- 内置模型管理器，76 个模型/34 种语言按语言与质量筛选下载
- 转写/翻译/TTS 一体，支持 txt/srt/json 导出与悬浮字幕
- GUI 与无头终端双模式，含进行中的树莓派移植

## 适用场景

- 无网络环境下做实时语音转写和跨语言翻译
- 把录音文件转成文本或字幕文件
- 演示或会议时用悬浮字幕窗口显示实时转写内容

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: PolyScribe is a lightweight desktop tool for fully offline live **speech transcription** and **translation**, powere
> L7: - 🎙️ Real-time speech recognition (fully offline, powered by Vosk)
> L11: - 📦 Built-in Model Manager — 76 Vosk models + Argos packages, filtered by language/quality, download with progress 

## 星数曲线

```mermaid
xychart-beta
    title "kcitlyn/PolyScribe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `62500c30dfa1` · [字段定义](../../DATASET.md)*
