# itsmevictor/clean-transcribe

⭐ 26 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/itsmevictor/clean-transcribe) · 个人维护

**CLI 工具：转录 YouTube/本地音视频并用 LLM 清理成稿**

面向终端用户的命令行工具：读取 YouTube URL 或本地音视频文件（mp3/wav/mp4/mkv 等），用本地（Whisper、Voxtral）或 API（OpenAI、Gemini、Mistral）转录模型生成文本，再调用用户选定的 LLM 去除语气词、修正语法、分段整理；输出 TXT/SRT/VTT 三种格式，SRT/VTT 清理时保留时间轴。LLM 接入基于 Simon Willison 的 llm 包，支持 Gemini、ChatGPT、Claude 及本地模型；可指定起止时间、清洗风格（presentation/conversation/lecture）或跳过清理。通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 YouTube URL 与多种本地音视频格式输入
- 本地（Whisper/Voxtral）与 API 转录模型可选
- LLM 清理：去语气词、修语法、分段，保留原意
- 输出 TXT/SRT/VTT，字幕格式清理时保留时间轴

## 适用场景

- 把 YouTube 视频转成可读文稿或笔记
- 为视频生成清理过语法的 SRT/VTT 字幕
- 讲座/播客录音整理为结构化文本

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A command-line tool to turn any YouTube video, local audio or video file into a clean, readable text transcript. It 
> L9: 3. **Flexible transcription models**: Choose from various local (Whisper, Voxtral) and API-based (OpenAI, Gemini, Mi

## 星数曲线

```mermaid
xychart-beta
    title "itsmevictor/clean-transcribe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bf517821b292` · [字段定义](../../DATASET.md)*
