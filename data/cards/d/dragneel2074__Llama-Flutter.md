# dragneel2074/Llama-Flutter

⭐ 27 · C++ · MIT · 推送 2026-07-21 · [GitHub](https://github.com/dragneel2074/Llama-Flutter) · [官网](https://pub.dev/packages/llama_flutter_android) · 个人维护

**在 Android 上运行 GGUF 模型的 Flutter 插件（基于 llama.cpp）**

面向 Flutter 开发者的 Android 端插件，封装 llama.cpp（b8201）在 Android 上加载 GGUF 模型并生成文本。提供 Dart API（Pigeon 类型安全），支持流式 token 输出、中途停止、18 个生成参数（温度/惩罚/mirostat/seed 等）、7 种聊天模板及按文件名自动检测，支持 Vulkan GPU 加速与 GPU 检测 API（返回设备名、显存、推荐层数）。限 Android 平台，需 Flutter 3.24+、Android API 26+、NDK r27+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 llama.cpp 在 Android 加载 GGUF 模型并流式生成文本
- Vulkan GPU 加速与 GPU 检测 API（含推荐层数 0/16/99）
- 18 个生成参数与 7 种聊天模板，支持按文件名自动检测模板
- ARM64 NEON/dot product 优化

## 适用场景

- 在 Flutter 应用中本地运行 GGUF 模型做文本生成或聊天
- 在 Android 设备上检测 GPU 能力并决定 CPU/GPU 层数分配
- 为应用内嵌离线 LLM 推理能力

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: Run GGUF models on Android with llama.cpp - A simple, MIT-licensed Flutter plugin.
> L10: - **Android Only** - Optimized specifically for Android

## 星数曲线

```mermaid
xychart-beta
    title "dragneel2074/Llama-Flutter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-30 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `739ae0d83ecb` · [字段定义](../../DATASET.md)*
