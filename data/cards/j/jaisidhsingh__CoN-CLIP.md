# jaisidhsingh/CoN-CLIP

⭐ 40 · Python · NOASSERTION · 推送 2026-04-03 · [GitHub](https://github.com/jaisidhsingh/CoN-CLIP) · 个人维护

**WACV 2025 论文官方代码：含否定理解能力的 CLIP 模型**

发布论文 "Learning the Power of No" 的官方代码、模型权重与数据集。核心为 CoN-CLIP：用 CC-Neg 数据集对 CLIP（ViT-L/14、ViT-B/16、ViT-B/32）微调，使其具备否定（negation）理解能力。提供 Google Drive 权重下载、Python 加载代码、CC-Neg 基准数据集的加载与 VLM 评测方法、微调脚本，以及在 8 个零样本图像分类数据集和 SugarCREPE 组合性理解任务上的评测流程。面向多模态视觉语言模型方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CoN-CLIP 提供三种 CLIP 骨干的检查点（ViT-L/14、ViT-B/16、ViT-B/32）
- CC-Neg 数据集：否定理解评测基准
- 支持用 CC-Neg 微调 CLIP 与零样本图像分类评测
- 在 SugarCREPE 组合性理解任务上进行评测

## 适用场景

- 加载 CoN-CLIP 检查点做含否定的图文匹配或分类
- 用 CC-Neg 基准评测 CLIP 类 VLM 的否定理解
- 复现论文微调流程

## 场景标签

`模型评测` `多模态` `微调` · 领域:评测与运维

## 证据(README 行号)

> L1: # Learning the Power of “No”: Foundation Models with Negations (WACV 2025) [Paper]
> L3: This repository releases the official code, checkpoints, and data for our paper (arXiv preprint can be found here). 

## 星数曲线

```mermaid
xychart-beta
    title "jaisidhsingh/CoN-CLIP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4999f2610b14` · [字段定义](../../DATASET.md)*
