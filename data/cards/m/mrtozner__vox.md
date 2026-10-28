# mrtozner/vox

⭐ 50 · Rust · Apache-2.0 · 推送 2026-04-12 · [GitHub](https://github.com/mrtozner/vox) · 个人维护

**本地优先的 Rust 语音 AI 框架：STT/TTS/说话人分离/语音对话**

Rust 编写的本地语音 AI 框架，流水线为 VAD(Silero)→STT(Whisper/Sherpa)→说话人识别→TTS(Kokoro/Piper/Qwen3 等)，无 API key、无云端，模型首次运行时自动下载。提供 CLI（vox listen/speak/chat/serve）、内嵌单文件 Web UI（5 个标签页）、REST + 4 条 WebSocket 通道，以及 Python 绑定（maturin 构建）。各组件通过 Rust trait 可插拔替换。说话人分离与 Live Talk（可打断的全双工语音对话，需 Ollama）标注为实验性。支持 macOS/Linux/Windows 与树莓派 4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- VAD→STT→说话人识别→TTS 全本地流水线，离线可用
- 多后端可插拔：Whisper/Distil-Whisper/Sherpa STT，Kokoro/Piper/Qwen3/Pocket/Chatterbox TTS
- HTTP + WebSocket API 与内嵌单文件 Web UI
- ECAPA-TDNN 说话人分离（实验性），Live Talk 可打断语音对话

## 适用场景

- 在本机搭建离线语音转写与语音合成服务
- 通过 WebSocket 搭配本地 Ollama LLM 做语音对话应用
- 在树莓派等边缘设备上运行低占用语音流水线
- 用 Rust trait 或 Python 绑定把语音能力嵌入自己的项目

## 场景标签

`语音识别` `语音合成` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L2:  Local-first voice AI framework. Speech-to-text, text-to-speech, speaker diarization, and voice chat &mdash; all run
> L11: Mic --> VAD (Silero) --> STT (Whisper/Sherpa) --> Speaker ID --> Your Code --> TTS (Kokoro/Piper/Qwen3) --> Speaker
> L16: - **Speech-to-Text** &mdash; Whisper, Distil-Whisper (6x faster), Sherpa-ONNX (streaming + multilingual)
> L17: - **Text-to-Speech** &mdash; Kokoro (57 voices, 9 languages), Piper (multilingual), Qwen3 (state-of-the-art), Pocke

## 星数曲线

```mermaid
xychart-beta
    title "mrtozner/vox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f2fa0aab392f` · [字段定义](../../DATASET.md)*
