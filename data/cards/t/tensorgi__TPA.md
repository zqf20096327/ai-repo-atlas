# tensorgi/TPA

⭐ 464 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/tensorgi/TPA) · [官网](https://tensorgi.github.io/TPA) · 组织维护

**Tensor Product Attention Transformer (T6) 官方预训练代码**

NeurIPS 2025 Spotlight 论文 "Tensor Product Attention Is All You Need" 的官方实现仓库，基于 nanoGPT 代码库构建。提供 T6 模型的数据准备脚本（支持 Fineweb-Edu-100B 与 OpenWebText）、多 GPU 分布式预训练（bash 脚本或 torchrun）、以及集成 lm-evaluation-harness 的基准评测流程；另含 FlashTPA prefilling/decoding 的 Python 与 Triton 实现。硬件要求 A100/H100，至少 8×80G 显存，面向研究人员复现与扩展该架构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tensor Product Attention 机制实现，用于降低 KV cache 大小
- 支持 Fineweb-Edu-100B 与 OpenWebText 数据准备脚本
- 多 GPU 分布式预训练（pretrain.sh / torchrun）
- FlashTPA prefilling/decoding 的 Python 与 Triton 实现，集成 lm-evaluation-harness 评测

## 适用场景

- 复现或预训练 T6 架构模型
- 研究 Tensor Product Attention 与 FlashTPA 机制
- 在标准基准上评测预训练后的 T6 模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L10: **[NeurIPS 2025 Spotlight]** **Tensor ProducT ATTenTion (TPA) Transformer** (T6) is a state-of-the-art transformer 
> L12: This repository contains the official code for the paper "Tensor Product Attention Is All You Need".

## 星数曲线

```mermaid
xychart-beta
    title "tensorgi/TPA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 463 --> 465
    line [464, 464]
```

2026-10-18 464 → 2026-10-26 464（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `12b4134471ef` · [字段定义](../../DATASET.md)*
