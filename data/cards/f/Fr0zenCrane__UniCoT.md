# Fr0zenCrane/UniCoT

⭐ 237 · Python · Apache-2.0 · 推送 2026-05-31 · [GitHub](https://github.com/Fr0zenCrane/UniCoT) · 组织维护

**ICLR 2026 论文项目：扩展 MLLM 的文本-视觉统一思维链推理框架**

Uni-CoT 将 Chain-of-Thought 推理扩展到多模态领域，基于 Bagel-7B-MoT 训练 UniCoT-7B-MoT 模型，用于可靠图像生成与编辑、视觉与物理推理、视觉规划和多模态故事理解。采用两级推理架构：宏观 CoT 负责任务分解（顺序/并行/渐进三种规划机制），微观 CoT 含自反思机制。提供推理、评测（WISE/KRIS/RISE）与 SFT 训练脚本，另发布 Self-Reflection-6K 与 Breakdown-3K 两个数据集。并行与渐进分解、RL 框架仍在路线图中未发布；推理需至少一张 40GB 显存 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两级推理架构：宏观任务分解（顺序/并行/渐进）+ 微观自反思
- 基于 Bagel-7B-MoT 的 UniCoT-7B-MoT 权重发布于 Hugging Face
- 提供 SFT 全量微调与 LoRA 微调脚本
- 发布 UniCoT-Self-Reflection-6K 与 UniCoT-Breakdown-3K 训练数据集

## 适用场景

- 需要自反思机制的推理式文本生成图像/图像编辑
- 在 WISE、KRIS Bench 等推理基准上复现评测结果
- 基于公开数据集微调多模态推理模型

## 场景标签

`图像生成` `多模态` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L33: To tackle this, we introduce **Uni-CoT**, a unified reasoning framework that extends CoT principles to the **multim
> L54: - ✅ **2025.07.29** &mdash; We released **UniCoT-7B-MoT v0.1** on Huggingface, which extends Bagel-7B-MoT model to p

## 星数曲线

```mermaid
xychart-beta
    title "Fr0zenCrane/UniCoT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 236 --> 238
    line [237, 237]
```

2026-10-18 237 → 2026-10-25 237（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `11f061cf95e3` · [字段定义](../../DATASET.md)*
