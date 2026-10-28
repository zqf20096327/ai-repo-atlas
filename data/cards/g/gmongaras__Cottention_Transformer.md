# gmongaras/Cottention_Transformer

⭐ 21 · Cuda · 推送 2025-11-15 · [GitHub](https://github.com/gmongaras/Cottention_Transformer) · 个人维护

**论文官方实现：用余弦注意力的线性 Transformer（BERT/GPT）**

论文《Cottention: Linear Transformers With Cosine Attention》的官方代码实现，将 softmax 注意力替换为余弦注意力以获得线性复杂度。提供 BERT 与 GPT 两种架构的训练、BERT 微调与推理脚本，附带自定义 CUDA 核需单独编译安装；多 GPU 训练通过 torchrun 与 SLURM 脚本示例说明。提供 Hugging Face 与 Google Drive 上的预训练模型下载，README 列出 GLUE 各任务与 GPT 困惑度的实验数值。GPT 相关数据集因匿名评审原因暂未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 余弦注意力（Cottention）替代 softmax 注意力的官方实现
- 提供 BERT/GPT 训练脚本与 torchrun 多 GPU/SLURM 示例
- BERT 微调与推理脚本（infer.py）
- 预训练模型托管在 Hugging Face 与 Google Drive

## 适用场景

- 复现论文中 Cottention BERT/GPT 的训练与评测结果
- 在 GLUE 任务上微调并推理 Cottention BERT 模型
- 研究线性/余弦注意力机制的实现细节

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains the official implementation of the paper "Cottention: Linear Transformers With Cosine Atten
> L5: Paper found here: https://arxiv.org/abs/2409.18747
> L83: An inference playground can be utilized with pretrained models by running the `BERT_Trainer/infer.py` and replacing

## 星数曲线

```mermaid
xychart-beta
    title "gmongaras/Cottention_Transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `54bf5fd80e17` · [字段定义](../../DATASET.md)*
