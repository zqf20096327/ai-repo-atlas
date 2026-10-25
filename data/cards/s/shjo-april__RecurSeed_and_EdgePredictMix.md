# shjo-april/RecurSeed_and_EdgePredictMix

⭐ 44 · Python · 推送 2026-07-25 · [GitHub](https://github.com/shjo-april/RecurSeed_and_EdgePredictMix) · 组织维护

**弱监督语义分割论文官方实现：RecurSeed 与 EdgePredictMix 方法**

论文《RecurSeed and EdgePredictMix: Single-stage learning is sufficient for Weakly-Supervised Semantic Segmentation》（arXiv 2204.06754）的官方 PyTorch 实现。面向使用图像级标签做弱监督语义分割（WSSS-IL）的研究者：RecurSeed 通过递归迭代交替减少漏检与误检，EdgePredictMix 是利用相邻像素概率差的对象边缘增强数据增广。提供训练、推理与评测完整流程，含 AffinityNet 随机游走多阶段方案与 DeepLabv2/v3+ 实现，在 PASCAL VOC 2012 与 MS COCO 2014 上训练（单卡 RTX A6000 约 24 小时），并放出权重与伪标签。代码在 Ubuntu 20.04 + NVIDIA GPU/CUDA 环境测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RecurSeed 递归迭代减少类激活图的漏检与误检
- EdgePredictMix 数据增广利用相邻像素概率差表达对象边缘
- 提供单阶段与多阶段（随机游走 + DeepLabv2/v3+）完整训练推理流程
- 公开预训练权重、预测掩码与 VOC 伪标签

## 适用场景

- 复现 WSSS 论文实验结果或评测权重
- 在 VOC/COCO 上训练图像级标签的弱监督分割模型
- 获取或改进 WSSS 伪标签质量
- 在其代码基础上开展后续研究（如 MARS）

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: This repository is the official implementation of "RecurSeed and EdgePredictMix: Single-stage learning is sufficient
> L22: Although weakly-supervised semantic segmentation using only image-level labels (WSSS-IL) is potentially useful, its

## 星数曲线

```mermaid
xychart-beta
    title "shjo-april/RecurSeed_and_EdgePredictMix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `90494cb7ef49` · [字段定义](../../DATASET.md)*
