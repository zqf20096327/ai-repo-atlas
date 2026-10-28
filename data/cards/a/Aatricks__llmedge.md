# Aatricks/llmedge

⭐ 72 · Kotlin · Apache-2.0 · 推送 2026-08-11 · [GitHub](https://github.com/Aatricks/llmedge) · [官网](https://aatricks.github.io/llmedge/) · 个人维护

**Android 端侧多模态推理库：在设备上运行 LLM/STT/TTS/图像视频生成**

基于 llama.cpp（JNI）的 Android 原生推理库，通过 LLMEdge 门面提供文本生成、流式输出、多轮会话、工具调用与推理（thinking）控制；集成 Whisper.cpp 做语音转文字、Bark.cpp 做语音合成、Stable Diffusion/FLUX.2 做图像生成、Wan 2.1 做视频生成，并含 ML Kit OCR、端侧 RAG 与 safetensors→GGUF 转换（带量化）。支持从 Hugging Face Hub 下载缓存模型，提供低端设备预设，GPU 后端（OpenCL/Vulkan）为可选实验性。API 成熟度按功能区不均，VLM 路径仍属实验性。面向 Android 开发者，以 Maven Central/GitHub Packages 依赖或源码构建接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- llama.cpp JNI 运行 GGUF 模型，含批量解码与 KV cache 复用
- Whisper.cpp STT、Bark.cpp TTS、Stable Diffusion/FLUX.2 图像生成、Wan 2.1 视频生成
- 端侧 safetensors→GGUF 转换，支持 Q8_0/Q4_K_M/IQ2_BN 量化
- Hugging Face 模型下载缓存与低端设备预设（BitNet、SmolVLM2）

## 适用场景

- 在 Android 应用内离线运行 LLM 对话与工具调用
- 给移动应用加端侧语音转文字和语音合成
- 在低端 Android 设备上跑预设小模型做文本或视觉任务

## 场景标签

`推理引擎` `语音识别` `语音合成` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **llmedge** is a lightweight Android library for running GGUF language models fully on-device, powered by llama.cpp.
> L17: - **LLM Inference**: Run GGUF models directly on Android using llama.cpp (JNI)

## 星数曲线

```mermaid
xychart-beta
    title "Aatricks/llmedge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 70 --> 73
    line [71, 72, 72]
```

2026-10-18 71 → 2026-10-28 72（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6ad0d2b5f377` · [字段定义](../../DATASET.md)*
