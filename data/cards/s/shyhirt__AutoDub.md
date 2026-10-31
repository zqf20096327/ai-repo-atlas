# shyhirt/AutoDub

⭐ 31 · Python · 推送 2026-05-04 · [GitHub](https://github.com/shyhirt/AutoDub) · 个人维护

**给视频创作者的自动转录、翻译与配音命令行工具**

Python 命令行脚本：用 OpenAI Whisper 转录视频音频并带时间戳，经 Google Translate 或本地 Ollama（默认 llama3，可指定 Mistral）翻译为 100+ 语言，再用三种 TTS 引擎之一（Edge TTS、Silero、XTTS 语音克隆）合成配音，FFmpeg 混合原声（20%）与配音（150%）输出视频和 SRT 字幕。Silero 与 XTTS 可离线运行；XTTS 需 6-10 秒声音样本、官方标注 GPU recommended。需 Python 3.10 与 ffmpeg 等系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 转录 + 三种 TTS 引擎（Edge/Silero/XTTS 语音克隆）的完整配音流水线
- 可选 Ollama 本地 LLM 翻译，实现全程离线工作流
- 支持 100+ 种语言（Edge TTS），同时生成 SRT 字幕文件
- 输出保留原视频不重编码，原声 20% 与配音 150% 混音

## 适用场景

- 把英语视频自动配音成中文、俄语等其他语言
- 用 6-10 秒声音样本克隆原声优音色进行配音
- 离线环境（Ollama + Silero/XTTS）下完成视频翻译配音

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L7: - 🎙️ **Speech Recognition**: Transcribe audio using OpenAI Whisper
> L12:  - **XTTS**: Voice cloning from 6-10 second samples
> L178: 2. **Transcribe**: Whisper "base" model transcribes with timestamps

## 星数曲线

```mermaid
xychart-beta
    title "shyhirt/AutoDub 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-31 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6246419dd40d` · [字段定义](../../DATASET.md)*
