# eauchs/speech-to-speech-pipeline

⭐ 10 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/eauchs/speech-to-speech-pipeline) · 个人维护

**本地实时语音对话流水线：STT-LLM-TTS，支持打断**

在本地机器上运行的实时对话管线：用 Faster Whisper（CPU、int8 量化）将语音转写为文本，调用本地 OpenAI 兼容 API 的 LLM（SSE 流式）生成回复，再用 MLX Audio 的 Kokoro 模型经 MPS 硬件加速合成语音播放。通过 asyncio、队列、音频分块降低延迟，支持用户开口即切断助手语音的 barge-in。模型、音频设备、静音阈值等经脚本顶部变量配置。MLX TTS 仅在 Apple Silicon 上可用，其他平台仅 STT 与 LLM 部分可运行；安装为 git clone 后 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- STT→LLM→TTS 全本地流水线，支持 barge-in 打断
- LLM 后端为任意本地 OpenAI 兼容 API（LM Studio、Ollama），SSE 流式
- TTS 使用 MLX Audio/Kokoro 4-bit 模型，MPS 硬件加速
- 模型大小、音频设备、静音检测等参数可在脚本中配置

## 适用场景

- 在 Mac 上搭建本地实时语音助手
- 体验带打断机制的语音对话交互
- 在无网络依赖的本地环境串联 STT-LLM-TTS 链路

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: This project implements a real-time conversational pipeline that runs locally on your machine (optimized for macOS w
> L9:  * **STT:** Uses **Faster Whisper** (default: `small` `int8` quantized model) for fast and efficient CPU-based trans
> L10:  * **LLM:** Interacts with any local OpenAI-compatible API (e.g., **LM Studio**, **Ollama**) via SSE streaming.
> L11:  * **TTS:** Uses **MLX Audio** with the **Kokoro** model (default: 4-bit version), optimized for hardware accelerat

## 星数曲线

```mermaid
xychart-beta
    title "eauchs/speech-to-speech-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `75231510e04a` · [字段定义](../../DATASET.md)*
