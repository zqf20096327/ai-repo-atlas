# runpod-workers/worker-faster_whisper

⭐ 144 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/runpod-workers/worker-faster_whisper) · [官网](https://runpod.io) · 组织维护

**将 faster-whisper 封装为 RunPod serverless 端点的转录 worker**

RunPod 官方 worker 仓库之一，把 faster-whisper 语音转录封装为 serverless 端点：接收音频 URL 或 base64 输入，支持 tiny 到 turbo 共 10 种 Whisper 模型选择，输出 plain_text、formatted_text、srt、vtt 格式的转录与英译，并提供温度、beam search、VAD 静音过滤、词级时间戳等解码参数。面向在 RunPod 平台部署无服务器 GPU 推理的开发者，依赖 RunPod 的 worker 运行环境。

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

- 支持 10 种 Whisper 模型（tiny 至 turbo、distil 系列）
- 音频 URL 或 base64 输入，输出 plain_text/formatted_text/srt/vtt 四种格式
- 提供翻译到英文与 Silero VAD 静音过滤、词级时间戳选项
- 暴露温度、beam_size 等解码参数

## 适用场景

- 在 RunPod 上部署按需调用的语音转文字 API
- 生成带时间戳的字幕文件（SRT/VTT）
- 将非英语音频转录并翻译为英文

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Faster Whisper is designed to process audio files using various Whisper models, with options for transcription forma
> L26: |`model`|str|Choose a Whisper model. Choices: "tiny", "base", "small", "medium", "large-v1", "large-v2", "large-v3"

## 星数曲线

```mermaid
xychart-beta
    title "runpod-workers/worker-faster_whisper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-26 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `cc054cba1c47` · [字段定义](../../DATASET.md)*
