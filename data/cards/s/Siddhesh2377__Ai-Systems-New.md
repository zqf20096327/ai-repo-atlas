# Siddhesh2377/Ai-Systems-New

⭐ 33 · C++ · MIT · 推送 2026-05-16 · [GitHub](https://github.com/Siddhesh2377/Ai-Systems-New) · 个人维护

**Android 端侧 AI SDK：LLM 推理、图像生成、图像处理与 TTS 模块**

面向 Android（ARMv8/ARMv9）的端侧 AI SDK，为 ToolNeuron 开发，其他应用需 fork 或 clone 后集成所需模块。包含四个独立 Android 库模块：gguf_lib（基于定制 llama.cpp 分支的 LLM 推理，支持多轮对话、GBNF 语法约束的模型无关工具调用、嵌入）、ai_sd（基于 QNN/MNN 的 Stable Diffusion 文生图、图生图与 inpaint，支持 LoRA）、两个 ONNX Runtime TTS 模块（Supertonic v2 与支持声音克隆的 Chatterbox）。JNI + 原生 C++ 后端，Gradle/CMake 构建，要求 Min SDK 27、arm64-v8a。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- llama.cpp 定制分支的端侧 LLM 推理：流式对话、GBNF 工具调用、KV cache 复用与投机解码
- Stable Diffusion 端侧生成：QNN Hexagon DSP 加速 + MNN CPU 回退，支持 LoRA 与分块 VAE
- 双 TTS 模块：Supertonic v2（5 语言 10 音色）与 Chatterbox（10 秒参考音频声音克隆）
- 四个模块各自独立 JNI 层，无共享原生依赖，可单独引入

## 适用场景

- 在我的 Android 应用里集成离线 LLM 对话与工具调用
- 在骁龙设备上离线运行 Stable Diffusion 生图与 inpaint
- 为应用加入端侧语音合成或声音克隆能力

## 场景标签

`图像生成` `语音合成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L3: On-device AI SDK for Android — LLM inference, image generation, image processing, and text-to-speech. No cloud, no i
> L7: > **Note:** This repo is developed strictly for **ToolNeuron**. If you want to use these SDKs in your own app, fork 
> L13: |**gguf_lib**|LLM inference (chat, embeddings, tool calling)|llama.cpp (custom fork)|`com.dark.gguf_lib`|

## 星数曲线

```mermaid
xychart-beta
    title "Siddhesh2377/Ai-Systems-New 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `865163ef825b` · [字段定义](../../DATASET.md)*
