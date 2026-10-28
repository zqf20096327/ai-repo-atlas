# lmassaron/gemma_from_scratch

⭐ 37 · Jupyter Notebook · NOASSERTION · 推送 2026-09-28 · [GitHub](https://github.com/lmassaron/gemma_from_scratch) · 个人维护

**教学向 Gemma 3 从零实现：PyTorch 训练与推理**

基于纯 PyTorch 的 Gemma 3 decoder-only transformer 最小化实现，受 nanoGPT 与 Sebastian Raschka 笔记本启发，面向学习模型架构与训练流程的开发者。提供两条工作流：用官方 tokenizer 加载 Hugging Face 预训练 270M 权重做推理，或用 GPT-2 tokenizer 在自有数据（如 TinyStories）上从零训练。架构含全局/滑动窗口注意力、SwiGLU、RMSNorm、RoPE；训练脚本支持混合精度、梯度累积与梯度裁剪。需从源码克隆安装，依赖 requirements.txt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemma 3 架构教学实现：RoPE、RMSNorm、SwiGLU、全局+滑动窗口注意力
- 支持官方 270M 预训练权重推理与自有数据从零训练两种工作流
- 训练含混合精度（bfloat16）、梯度累积、warmup+cosine 调度
- 数据准备支持多核并行 tokenize 与内存映射处理超内存数据集

## 适用场景

- 学习 Gemma 3 transformer 架构的代码级实现
- 在小数据集（如 TinyStories）上从零训练小型语言模型
- 对照官方预训练权重验证自实现架构的正确性

## 场景标签

`模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository provides a clear and minimal implementation for training a Gemma-like language model from scratch us
> L11: 1. Inference with Official Gemma Weights: The inference_google_gemma.py script uses the official Gemma tokenizer an
> L12: 2. Training a Model From Scratch: The prepare_dataset.py and train.py scripts allow you to train a model on your ow

## 星数曲线

```mermaid
xychart-beta
    title "lmassaron/gemma_from_scratch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a05a4bd1c76c` · [字段定义](../../DATASET.md)*
