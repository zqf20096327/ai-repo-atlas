# lliWcWill/liveTranslation_openai-whisper

⭐ 20 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/lliWcWill/liveTranslation_openai-whisper) · [官网](https://live-translation-openai-whisper.vercel.app) · 个人维护

**调用 Whisper/Groq/OpenAI API 的实时语音转录与翻译工具**

基于 Python 的实时翻译工具（v2.1）：通过 Groq API 进行音频转录，OpenAI API 负责翻译与文本转语音，用户自带 API key 并在 config.yaml 中配置。提供命令行程序 main.py（可选录音时长、语言、连续模式、语音朗读等参数）与基于 Streamlit 的网页应用 gTranscribeq（拖拽上传 WAV/MP3/M4A 文件并下载转录结果）。支持 Smart Select 自动语言检测与多种西班牙语方言等语言选项，需系统安装 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Groq API 用于音频转录，OpenAI API 用于翻译与文本转语音
- 命令行工具支持连续模式、指定语言与 TTS 语音输出
- gTranscribeq 网页应用支持 WAV/MP3/M4A 上传转录与结果下载
- Smart Select 自动语言检测与多方言语言选项

## 适用场景

- 实时录制语音并翻译为指定语言
- 翻译已有的音频文件并生成语音朗读
- 通过网页界面上传音频快速获得转录文本

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L4: This release (v2.1 "Thunder+") of our Real-Time Translation Tool introduces lightning-fast transcription capabilitie
> L9: - **Groq API Integration**: Leveraging Groq's high-speed API for **ultra-fast transcription**, dramatically reducing
> L48: Execute with `python main.py` and the following optional flags:

## 星数曲线

```mermaid
xychart-beta
    title "lliWcWill/liveTranslation_openai-whisper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d5994103d53e` · [字段定义](../../DATASET.md)*
