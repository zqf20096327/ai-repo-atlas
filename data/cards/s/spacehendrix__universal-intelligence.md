# spacehendrix/universal-intelligence

⭐ 64 · Python · Apache-2.0 · 推送 2026-04-16 · [GitHub](https://github.com/spacehendrix/universal-intelligence) · 个人维护

**面向开发者的跨平台 AI 组件协议与组件库：标准化模型/工具/智能体**

Universal Intelligence（UIN）提出一套无框架的智能体协议，定义 Universal Model、Universal Tool、Universal Agent 三个规范，把模型、工具、智能体标准化为可组合的构建块，目标是替代 Langchain、Google ADK 等专有框架来构建简单、可移植的智能应用。同时提供社区组件与本地/Colab 游乐场。Universal Model 内嵌模型与多种引擎（transformers、llama.cpp、mlx、web-llm），根据硬件（CUDA/MPS/WebGPU）自动检测并选择量化精度与引擎，降低本地运行门槛；也可通过 OpenRouter 等凭据调用云端模型。以 Python 库（pip 可选 extras）与 JS/TS 两种形态提供，支持云、桌面、Web、移动平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个规范：Universal Model / Universal Tool / Universal Agent，可组合复用
- 自动硬件检测（CUDA/MPS/WebGPU），动态选择量化与引擎（transformers/llama.cpp/mlx/web-llm）
- 声明为无框架（framework-less）智能体协议，构建块可跨平台分发
- 提供社区组件、本地 playground 与 Google Colab 在线游乐场

## 适用场景

- 不依赖 Langchain 等框架构建可移植的智能体应用
- 同一套代码在不同硬件上本地运行模型而无需适配多套栈
- 初学者通过 playground 快速上手模型/工具/智能体组合

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L53: It provides three specifications: `Universal Model`, `Universal Tool`, and `Universal Agent`.
> L65: It aims to be a **framework-less agentic protocol**, removing the need for proprietary frameworks (eg. Langchain, G
> L82: For example, UIN models are designed to automatically detect the current hardware (cuda, mps, webgpu), its availabl

## 星数曲线

```mermaid
xychart-beta
    title "spacehendrix/universal-intelligence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9cce78a24399` · [字段定义](../../DATASET.md)*
