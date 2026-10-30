# S1LV3RJ1NX/mal-code

⭐ 27 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/S1LV3RJ1NX/mal-code) · 个人维护

**书籍配套代码：用 PyTorch 从零实现五种 LLM 架构**

书籍《My Adventures with Large Language Models》的配套代码仓库，逐章用 PyTorch 从零构建五种架构：Vanilla Encoder-Decoder Transformer、GPT-2（可加载 OpenAI 权重）、Llama 3.2-3B（RMSNorm/RoPE/SwiGLU/GQA，可加载 Meta 权重）、KV Cache/MQA/GQA 推理优化，以及含 Multi-Head Latent Attention、DeepSeekMoE、FP8 量化的 DeepSeek 实现。每章含 CPU 小规模与 GPU 全规模两套可运行代码，配 uv 环境安装说明。面向已掌握 Python/PyTorch 的 ML 工程师、研究人员与资深开发者。代码 MIT 许可，书本文本另受版权保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种架构从零实现：Transformer/GPT-2/Llama 3.2/KV Cache/DeepSeek（MLA+MoE+FP8）
- GPT-2 与 Llama 3.2 章节支持加载官方预训练权重
- 每章提供 CPU 小规模与 GPU 全规模两套变体
- 基于 uv 的环境安装流程（uv sync）

## 适用场景

- 跟随书籍逐章动手实现现代 LLM 架构
- 在本地复现 GPT-2 预训练或 Llama 加载实验
- 学习 KV Cache、GQA、MLA、MoE 等推理与架构机制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: This is the companion code repository for the book _My Adventures with Large Language Models_ by Prathamesh Saraf.
> L13: The book walks you through building five LLM architectures from scratch in PyTorch. Every chapter has runnable, end

## 星数曲线

```mermaid
xychart-beta
    title "S1LV3RJ1NX/mal-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8754342901d0` · [字段定义](../../DATASET.md)*
