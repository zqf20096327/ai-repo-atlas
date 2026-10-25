# VCG-team/DiffSegmenter

⭐ 59 · Jupyter Notebook · 推送 2026-07-05 · [GitHub](https://github.com/VCG-team/DiffSegmenter) · [官网](https://vcg-team.github.io/DiffSegmenter-webpage/) · 组织维护

**免训练的扩散模型开放词汇语义分割官方实现（TIP 2025）**

论文 'Diffusion Model is Secretly a Training-free Open Vocabulary Semantic Segmenter' 的官方代码实现：利用预训练扩散模型直接生成开放词汇语义分割结果，无需训练，在 VOC、COCO、Pascal Context 数据集上提供生成与评测脚本。面向计算机视觉科研人员，需 Linux、CUDA>=11.7、Python>=3.8 环境，通过 conda 建环境并 pip 安装依赖，手动下载数据集并修改路径后运行。

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

- 基于扩散模型免训练直接生成开放词汇语义分割结果
- 提供 voc/coco/Pascal Context 三类数据集脚本
- 含 MIoU 评测脚本（结果记录于 eval.txt）

## 适用场景

- 复现论文的开放词汇语义分割实验
- 在自定义数据集上评测扩散模型的分割能力

## 场景标签

`目标检测` `模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L1: # Diffusion Model is Secretly a Training-free Open Vocabulary Semantic Segmenter
> L61: For the setting of Open Vocabulary Semantic Segmentation， our model does not require training; it directly produces
> L63: The ‘open_vocabulary’ folder contains code for open vocabulary semantic segmentation. It includes scripts for the v

## 星数曲线

```mermaid
xychart-beta
    title "VCG-team/DiffSegmenter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 57 --> 60
    line [58, 59, 59]
```

2026-10-18 58 → 2026-10-25 59（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b35962f9dd10` · [字段定义](../../DATASET.md)*
