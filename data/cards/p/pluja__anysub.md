# pluja/anysub

⭐ 3,110 · TypeScript · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/pluja/anysub) · 个人维护

**自托管网页工具：音视频转字幕并在线编辑导出**

Anysub（前身为 Whishper）是一个自托管的字幕生成工具：上传音视频文件，用 Whisper 在本机转录，再在带波形时间线的编辑器中修正文字与时间轴，导出 SRT、WebVTT、LRC、纯文本或 JSON。支持词级时间、字幕过快/过长/重叠警告、断点续传上传、可搜索素材库，以及管理页配置模型、上传限制、磁盘空间与 worker。需 Linux x86-64 与 Docker 运行；GPU 加速需 NVIDIA 卡与 Container Toolkit，AMD/Intel GPU 暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 转录，模型范围从 tiny 到 large-v3-turbo
- 字幕编辑器含波形时间线、撤销与自动保存
- 导出 SRT/WebVTT/LRC/纯文本/JSON
- 支持本机或外部服务商（如 OpenAI、Groq）转录

## 适用场景

- 把录音或视频批量转成带时间轴的字幕
- 在网页编辑器中校正字幕文字与时间
- 在自家服务器上自托管处理音视频转录

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Anysub (formerly Whishper) makes subtitles from audio and video. Upload a recording, let Whisper transcribe it, then
> L9: - Transcription with Whisper, from the `tiny` model to `large-v3-turbo`.

## 星数曲线

```mermaid
xychart-beta
    title "pluja/anysub 星数(近 9 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-25", "2026-11-26"]
    y-axis "stars" 3105 --> 3111
    line [3107, 3106, 3107, 3108, 3106, 3107, 3106, 3107, 3110]
```

2026-11-11 3,107 → 2026-11-26 3,110（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a276cb219d5e` · [字段定义](../../DATASET.md)*
