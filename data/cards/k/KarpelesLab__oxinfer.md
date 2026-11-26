# KarpelesLab/oxinfer

⭐ 3 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/KarpelesLab/oxinfer) · [官网](https://karpeleslab.github.io/oxinfer/) · 组织维护

**纯 Rust 本地推理引擎：在任意设备上运行语言/视觉/图像/语音/嵌入模型**

oxinfer 用纯 Rust 实现本地推理，无需 BLAS 或机器学习框架，直接从 checkpoint（safetensors、GGUF、MLX）读取权重，用手写 SIMD 内核与自有线程池实现全部运算。支持聊天与视觉语言模型（含 MoE、超大模型从存储流式加载）、图像生成与编辑、视频、语音转文本、语音合成与嵌入。CPU 路径为基线且处处可用，Metal/CUDA/Vulkan/WebGPU 在运行时检测，超出内存的模型可从存储流式读权重。提供 OpenAI 与 Anthropic 兼容 API、浏览器内 WebAssembly 构建、Web GUI 与模型目录。版本为 0.0.x，API 与文件格式可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 纯 Rust 实现，无 BLAS/无 ML 框架，手写 SIMD 内核（NEON、AVX2、wasm simd128）
- CPU 路径为参考实现，GPU（Metal/CUDA/Vulkan/WebGPU）运行时检测、构建期零链接
- 超大模型（至 1TB+）从存储流式加载，可在低于权重大小的内存上运行
- 提供 OpenAI 兼容 /v1 与 Anthropic 兼容 /v1/messages API 及浏览器 WebGPU 运行

## 适用场景

- 在没有 GPU 或内存不足的设备上运行大模型
- 本地起一个 OpenAI 兼容服务器给 opencode/Claude Code/Aider 等客户端使用
- 在浏览器标签页内直接运行小模型（WebGPU）
- 本地进行图像生成、OCR、语音转写与 TTS/语音克隆

## 场景标签

`推理引擎` `图像生成` `语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L8: Local inference in pure Rust for language, vision, image, speech and embedding models: run
> L61: Supported models. No BLAS, no ML framework: weights are read straight out of
> L34: The same address serves an OpenAI-compatible API (`/v1`) and Anthropic's (`/v1/messages`). The


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `aafa769024b4` · [字段定义](../../DATASET.md)*
