# NVIDIA/TensorRT-LLM

⭐ 14,850 · Python · NOASSERTION · 推送 2026-10-18 · [GitHub](https://github.com/NVIDIA/TensorRT-LLM) · [官网](https://nvidia.github.io/TensorRT-LLM) · 组织维护

**开发者在 NVIDIA GPU 上高效运行 LLM 推理的优化库**

NVIDIA 开源的 LLM 与视觉生成模型推理优化库：提供针对 attention、GEMM、MoE 等常见操作的定制 kernel，以及 Prefill-Decode 分离、Wide Expert Parallelism、Speculative Decoding 等运行时优化。基于 PyTorch 架构，提供高层 Python LLM API，覆盖单卡到多卡、多节点部署，内置多种并行策略，并可与 NVIDIA Dynamo 和 Triton Inference Server 集成；含 Python 和 C++ 运行时组件。Quick Start、安装指南、支持硬件与模型清单、性能基准文档均指向官方文档站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 48,421 位贡献者
- 涨星:近 1 天 **+12**(自 20261016 起算)

## 能力要点

- 提供针对 attention/GEMM/MoE 等操作的定制 kernel 与运行时算法优化
- 基于 PyTorch 的 Python LLM API，支持单 GPU 到多 GPU/多节点部署
- 内置多种并行策略，可扩展、可用原生 PyTorch 代码自定义预定义模型
- 支持扩散模型视觉生成，与 NVIDIA Dynamo 和 Triton Inference Server 集成

## 适用场景

- 在 NVIDIA GPU 上部署 LLM 推理服务
- 对 DeepSeek、Llama 等模型做多 GPU/多节点推理优化
- 运行视觉生成（扩散模型）推理任务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L263: TensorRT LLM is an open-sourced library for optimizing LLM and Visual Gen inference. It provides state-of-the-art 
> L265: Architected on PyTorch, TensorRT LLM provides a high-level Python LLM API that supports a wide range of inference 
> L267: TensorRT LLM is designed to be modular and easy to modify. Its PyTorch-native architecture allows developers to ex

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `42c4a84942df` · [字段定义](../../DATASET.md)*
