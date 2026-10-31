# kurianbenoy/Indic-Subtitler

⭐ 95 · Jupyter Notebook · MIT · 推送 2026-10-25 · [GitHub](https://github.com/kurianbenoy/Indic-Subtitler) · [官网](https://indicsubtitler.in/) · 个人维护

**印度语言视频/音频转写与字幕翻译的开源平台**

面向内容创作者、教育与媒体从业者的开源字幕平台：上传音频/视频或提供 YouTube ID，调用 ML 模型（SeamlessM4T_v2_large、faster-whisper、WhisperX、微调 Whisper）将印度语言语音转写为字幕并翻译到其他语言。架构为 FastAPI 后端（计划部署于 Modal.com 等无服务器平台）+ Next.js 前端，API 以 base64 音频或 yt_id 为输入。faster-whisper 与 WhisperX 为可选 ASR 后端，各模型覆盖的印度语言数量不同。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持上传音频与 YouTube ID 两种输入的转写 API
- 四个 ASR 模型选项：SeamlessM4T、faster-whisper、WhisperX、微调 Whisper
- 转写与字幕翻译到多种印度语言
- FastAPI 后端 + Next.js 前端架构

## 适用场景

- 创作者为泰米尔语等母语视频生成英语/印地语等字幕
- 教育内容翻译为学生母语以便理解
- 媒体从业者给新闻、影片制作字幕

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: > An open source subtitling platform 💻 for transcribing videos/audios in Indic languages and translating subtitles a
> L124: - POST request for the webendpoints: `generate_seamlessm4t_speech`, `generate_faster_whisper_speech`, `generate_wh

## 星数曲线

```mermaid
xychart-beta
    title "kurianbenoy/Indic-Subtitler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-31 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d6196227c455` · [字段定义](../../DATASET.md)*
