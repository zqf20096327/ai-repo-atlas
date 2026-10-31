# tattn/LocalLLMClient

⭐ 219 · Swift · MIT · 推送 2026-08-26 · [GitHub](https://github.com/tattn/LocalLLMClient) · 个人维护

**Swift 包：在 iOS/macOS/Linux 上运行本地 LLM**

面向 Apple 平台开发者的 Swift package，封装 llama.cpp、Apple MLX 与 Foundation Models 框架三种后端，提供统一的 Swift API 与流式输出，运行 GGUF / MLX 模型，支持多模态图像处理与 tool calling（均标注实验性）。附带 CLI 工具可从终端直接推理，并给出 iOS/macOS 示例应用。要求 iOS 17.0+ / macOS 14.0+ / Xcode 16.0+，项目自述仍为实验性、API 可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 API 封装 llama.cpp / Apple MLX / Foundation Models 三种推理后端
- 流式输出、实验性多模态图像处理与 tool calling
- 提供 CLI 工具与 iOS/macOS 示例应用
- 测试模型覆盖 LLaMA 3、Gemma、Qwen、Phi 系列

## 适用场景

- 在 iOS/macOS 应用中嵌入本地 LLM 推理
- 用 Swift 统一调用 llama.cpp 与 MLX 后端
- 在 iPhone/Mac 上跑多模态模型做图像理解

## 场景标签

`推理引擎` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L6: A Swift package to interact with local Large Language Models (LLMs) on Apple platforms.
> L207: This package uses llama.cpp, Apple's MLX and Foundation Models framework for model inference.

## 星数曲线

```mermaid
xychart-beta
    title "tattn/LocalLLMClient 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 218 --> 220
    line [219, 219]
```

2026-10-18 219 → 2026-10-31 219（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ae3f49e31f42` · [字段定义](../../DATASET.md)*
