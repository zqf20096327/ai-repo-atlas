# elbruno/ElBruno.VibeVoiceTTS

⭐ 16 · C# · MIT · 推送 2026-07-03 · [GitHub](https://github.com/elbruno/ElBruno.VibeVoiceTTS) · 个人维护

**.NET 文本转语音库：纯 C# ONNX 推理运行 VibeVoice 模型**

基于 Microsoft VibeVoice-Realtime-0.5B 模型的 .NET 文本转语音库：通过 ONNX Runtime 做纯 C# 推理，运行时无 Python 依赖。支持 GPU 加速（DirectML 适配任意 Windows GPU、CUDA 适配 NVIDIA）并自动回退 CPU；模型与 6 个英文声音预设从 HuggingFace 自动下载（另有实验性多语言支持）。提供流式 PCM 分块输出、依赖注入集成和 Microsoft.Extensions.AI ITextToSpeechClient 适配器。限制：流式输出非渐进生成（SupportsProgressiveGeneration 为 false），长句可能产生伪影，非英语效果不定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX Runtime 纯 C# 推理，运行时零 Python 依赖
- DirectML/CUDA GPU 加速，不可用时自动回退 CPU
- 模型与 6 个声音预设从 HuggingFace 自动下载
- Microsoft.Extensions.AI ITextToSpeechClient 适配器与流式 PCM 分块 API

## 适用场景

- 在 .NET 应用中本地生成英文语音，无需 Python 或云服务
- 通过 Microsoft.Extensions.AI 接口统一接入 TTS 能力
- Blazor/MAUI 跨平台应用内置离线语音合成

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L11: A .NET library for text-to-speech synthesis using Microsoft's VibeVoice-Realtime-0.5B — native C# inference via ONN
> L15: - 🔊 **Natural Text-to-Speech** — High-quality speech synthesis powered by VibeVoice-Realtime-0.5B
> L17: - 🤖 **Pure C# Inference** — ONNX Runtime, zero Python dependency at runtime

## 星数曲线

```mermaid
xychart-beta
    title "elbruno/ElBruno.VibeVoiceTTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d06e27dd8f92` · [字段定义](../../DATASET.md)*
