# mewmix/nabu

⭐ 62 · Kotlin · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/mewmix/nabu) · 个人维护

**Android 端侧 TTS 与 LLM 对话测试台，含电子书朗读**

面向 Android 设备的本地推理应用：TTS 侧以 ONNX Runtime（NNAPI/CPU）运行 Kokoro-82M、Supertonic v2/v3、Soprano 1.1；LLM 侧以 LiteRT .task 模型（MediaPipe 运行时）做本地对话，并通过 LlamaCppBackend 实验性加载导入的 .gguf 文件。提供电子书工作流（EPUB/PDF/TXT 解析、逐行预生成 WAV）与 LLM+TTS 循环朗读。内置可选本地 REST API 服务器（默认 127.0.0.1:8455），暴露 OpenAI 兼容 /v1/chat/completions 与 TTS 端点，支持 OpenAI tools 规范的 agentic 调用，可让 OpenCode/Open Interpreter 以 Nabu 作为后端。实验性支持 Codex OAuth 远程模型。限制：API 无鉴权层；GGUF 仅限手动导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种 ONNX TTS 引擎（Kokoro/Supertonic/Soprano）端侧运行与切换比较
- LiteRT .task 本地 LLM 对话与实验性 .gguf（llama.cpp 后端）导入
- 本地 REST API 提供 OpenAI 兼容 chat/completions 与 TTS 端点，支持 tools 规范
- 电子书工作流：解析 EPUB/PDF/TXT 并逐行预生成 WAV 音频

## 适用场景

- 在手机上离线对比多个 TTS 引擎的效果
- 把电子书转成语音离线收听并保存书签
- 让 OpenCode/Open Interpreter 等工具以手机作为 LLM/TTS 后端
- 端侧运行小参数 LLM 进行本地对话与朗读

## 场景标签

`聊天机器人` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: Nabu is an on-device test bench for TTS and chat:
> L4: - ONNX Runtime (`NNAPI`/CPU) TTS with Kokoro-82M v1.0, Supertonic v3, Supertonic v2, and Soprano 1.1 (80M) via sopra
> L22: - `LLM workbench`: run local chat models from managed LiteRT `.task` downloads or imported `.gguf` files.

## 星数曲线

```mermaid
xychart-beta
    title "mewmix/nabu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6812d06ecb4b` · [字段定义](../../DATASET.md)*
