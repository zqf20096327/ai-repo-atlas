# marc-shade/Video-Transcription

⭐ 16 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/marc-shade/Video-Transcription) · 个人维护

**视频转写并生成 AI 人格的本地网页应用（Whisper+Ollama）**

基于 Streamlit 的视频转写工具：上传视频文件后提取音频并用 Whisper 转写为文本，支持多语言翻译、带可点击时间戳的交互式播放器、转写内搜索，并可导出 SRT/VTT/Markdown/JSON/TXT 五种格式。额外功能是从转写内容分析说话风格生成 AI 人格，并与该人格对话。AI 处理通过本地 Ollama 完成，支持动态模型选择；依赖 Python 3.10+、FFmpeg 与 Ollama，提供 Docker Compose 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 视频转写，支持多视频格式与时间戳
- 从转写生成 AI 人格并可与人格对话
- 本地 Ollama 处理，动态模型选择
- 导出 SRT/VTT/MD/JSON/TXT 多种格式

## 适用场景

- 上传视频获得带时间戳的文字转写并导出字幕
- 生成基于视频内容的 AI 人格进行对话
- 本地离线完成转写与 AI 处理

## 场景标签

`语音识别` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12: A powerful video transcription tool that not only transcribes videos but also generates AI personas that can engage
> L59: - 🎬 Video to text transcription using Whisper
> L63: - 🤖 AI persona generation from transcripts

## 星数曲线

```mermaid
xychart-beta
    title "marc-shade/Video-Transcription 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `9d8456ad6fc5` · [字段定义](../../DATASET.md)*
