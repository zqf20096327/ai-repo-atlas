# eugene-kamenev/Infernix-dgx-spark-gb10

⭐ 22 · C++ · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/eugene-kamenev/Infernix-dgx-spark-gb10) · 个人维护

**面向 DGX Spark 设备的 Qwen 模型 C++/CUDA 推理引擎**

从零编写的 C++20/CUDA 推理引擎，针对 NVIDIA DGX Spark（GB10，sm_121a，128 GB 统一内存，aarch64 Linux）做了端到端调校，支持 Qwen3.5/3.6/3.8/3.8-Flash-Next 模型家族。以 OpenAI 与 Anthropic 兼容 API 提供服务端（流式、工具调用恢复、约束解码），内置混合前缀缓存、七种 KV 缓存格式、MTP 与 n-gram 投机解码。仅支持单机运行，需 CUDA 13.0 与 GCC 13.3 在主机上编译，Docker 镜像声明未经充分测试。README 提供 DGX Spark 上的基准数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 GB10 微架构（48 SMs、24 MiB L2、128 GB LPDDR5X）调校 CUDA 内核与专家放置
- 提供 OpenAI/Anthropic 兼容 API，支持流式、工具调用与 JSON Schema/regex/GBNF 约束解码
- 支持 7 种 KV 缓存格式（bf16/fp8/int8/k8v4/nvfp4/k4v2/vq2）与 MTP+n-gram 投机调度
- 统一内存驻留全部路由专家层（INFERNIX_EXPERTS_ON_GPU=1）

## 适用场景

- 在 DGX Spark 设备上本地部署并服务 Qwen 大模型
- 为 agent 或代理后端提供兼容 OpenAI 的推理 API
- 在统一内存设备上跑大容量量化模型权重

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Infernix** is a high-performance, from-scratch C++20/CUDA inference engine for the Qwen3.5, Qwen3.6, Qwen3.8, and 
> L5: > **Project Lineage & DGX Spark (`GB10`) Retune:** This project is built on the **Infernix** inference engine (which
> L19: - **OpenAI & Anthropic APIs**: `/v1/chat/completions`, `/v1/responses`, `/v1/messages`, and `/v1/decide` with strea


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `348bfd962127` · [字段定义](../../DATASET.md)*
