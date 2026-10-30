# anira-project/anira

⭐ 235 · C++ · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/anira-project/anira) · [官网](https://anira-project.github.io/anira/) · 组织维护

**面向实时音频应用的神经网络推理集成 C++ 库**

C++ 库，用于在实时音频应用（如 JUCE/VST3、CLAP 插件）中集成神经网络推理，保证确定性的实时安全执行。支持多种推理后端：LibTorch、ONNX Runtime、LiteRT、TensorFlow Lite（legacy C API，与 LiteRT 互斥）与 ExecuTorch；通过静态线程池管理避免过度订阅并降低延迟，内置基准测试工具。跨 macOS/Linux/Windows/Android/iOS 平台，并可经 WebAssembly 在浏览器中运行（仅 ONNX Runtime 后端）。提供 CMake 子模块、预编译二进制、源码构建三种集成方式及 npm 包（@anira-project/anira）。限制：静态构建下 ExecuTorch 与 LiteRT/TFLite 不能同时使用；WASM 仅支持 ONNX Runtime。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时安全执行：确定性运行时，适配实时音频场景
- 多后端支持：LibTorch、ONNX Runtime、LiteRT/TFLite、ExecuTorch
- 静态线程池管理与内置实时性能基准测试
- 跨平台（含 Android/iOS/WASM），提供 C++ 库与 npm Web 包

## 适用场景

- 在 JUCE/VST3 或 CLAP 音频插件中嵌入实时安全的神经网络推理
- 对比不同神经网络模型、后端与音频配置的实时性能
- 在浏览器中通过 WebAssembly 运行音频神经网络推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: **Anira** is a high-performance library designed to enable easy real-time safe integration of neural network infere
> L35: - **Comprehensive Inference Engine Support**: Integrates common inference engines, LibTorch, ONNXRuntime, LiteRT, T

## 星数曲线

```mermaid
xychart-beta
    title "anira-project/anira 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 233 --> 236
    line [234, 235, 235]
```

2026-10-18 234 → 2026-10-30 235（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `44192987b308` · [字段定义](../../DATASET.md)*
