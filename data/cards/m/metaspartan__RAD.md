# metaspartan/RAD

⭐ 3 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/metaspartan/RAD) · 个人维护

**面向 AMD/NVIDIA GPU 的 Rust+ROCm/HIP LLM 推理引擎**

以 Rust 编写、基于 ROCm/HIP 与 CUDA 的多模态 LLM 推理引擎，原生运行 Inkling-2-Mini 与 DeepSeek-V4.1-Flash 等 MoE 模型，支持 DFlash 2/DSpark 投机解码、256K 长上下文与多用户连续批处理。提供兼容 OpenAI、Anthropic、vLLM、SGLang、llama.cpp 的 API 服务器（端口 6733），含 Prometheus /metrics、API 鉴权与数据并行路由。面向在 AMD Radeon AI PRO R9700 或 NVIDIA DGX Spark 硬件上进行单用户/多用户推理服务的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 DFlash 2 与 DSpark 投机解码，声明 100% bit-exact 输出对齐
- 兼容 OpenAI/Anthropic/vLLM/SGLang/llama.cpp 的 API 服务器，支持连续批处理与 Paged KV
- 单卡 R9700 上 2K–256K 长上下文推理与多用户批处理服务
- 内置 GPU Vision（mmproj-F16.gguf）与工具调用

## 适用场景

- 在 AMD R9700 上部署本地 LLM 推理服务
- 多用户并发的长上下文对话/代码服务
- 需要 OpenAI 兼容 API 接入本地模型的场景

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **RAD** is a high-performance, from-scratch multimodal LLM inference engine written in **Rust**, **ROCm/HIP**, and *
> L15: - **Full OpenAI, Anthropic, vLLM, SGLang & llama.cpp API Server:** Continuous batching (`B<=128`), Paged KV, chunke


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `d1b3b64f7930` · [字段定义](../../DATASET.md)*
