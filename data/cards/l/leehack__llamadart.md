# leehack/llamadart

⭐ 78 · Dart · MIT · 推送 2026-10-23 · [GitHub](https://github.com/leehack/llamadart) · [官网](https://llamadart.leehack.com) · 个人维护

**Dart/Flutter 跨平台端侧 LLM 推理库，统一 API 调 llama.cpp 与 LiteRT-LM**

面向 Dart 与 Flutter 开发者的端侧推理库：单一 API 在 Android、iOS、macOS、Windows、Linux 与 Web 上运行模型，应用无需自建推理服务器。GGUF 模型经 llama.cpp 执行（Metal/Vulkan/WebGPU 后端），.litertlm 模型经 LiteRT-LM 执行（可用 GPU/NPU）。以 pub 包形式分发，运行时资源由构建钩子自动解析，使用者无需本地 C++ 工具链。能力覆盖流式聊天、工具调用、结构化 JSON 输出、嵌入、LoRA、语音识别与合成（实验性）、端侧文生图（预览）；Web 支持为实验性，LiteRT-LM 平台覆盖较窄。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 一套 API 跨 6 个平台运行 GGUF（llama.cpp）与 .litertlm（LiteRT-LM）模型
- 流式聊天、工具调用解析、结构化 JSON 输出、嵌入、LoRA、投机解码
- 实验性语音识别（Qwen3-ASR / LiteRT-LM ASR）与 Qwen3-TTS 合成
- 预览端侧文生图与决策模型（DecisionEngine）；运行时能力按 engine.capabilities 报告

## 适用场景

- 在 Flutter/Dart 应用中离线运行本地 LLM 聊天与工具调用
- 移动端 App 集成端侧模型且不依赖推理服务器
- 浏览器端经 WebGPU 实验性运行模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Cross-platform, on-device LLM inference for Dart and Flutter. One API runs
> L9: no inference server. GGUF models run through llama.cpp and `.litertlm` models
> L195: - GGUF model loading and generation through llama.cpp.

## 星数曲线

```mermaid
xychart-beta
    title "leehack/llamadart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-24 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0b5b1c365746` · [字段定义](../../DATASET.md)*
