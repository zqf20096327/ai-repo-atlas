# ananthu-aniraj/pdiscoformer

⭐ 22 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/ananthu-aniraj/pdiscoformer) · [官网](https://ananthu-aniraj.github.io/pdiscoformer/) · 个人维护

**ECCV 2024 论文官方实现：ViT 无监督部件发现与细粒度分类**

论文《PDiscoFormer: Relaxing Part Discovery Constraints with Vision Transformers》（ECCV 2024 Oral）的官方 PyTorch 实现。利用自监督 DINOv2 ViT 特征，配合总变差（TV）先验放松部件需小而紧凑的几何约束，在 CUB、PartImageNet、Oxford Flowers、NABirds 四个细粒度分类数据集上做无监督部件发现与分类。提供数据预处理脚本、训练与评测说明、model zoo，模型可经 torch hub 与 HuggingFace 获取。通过 conda environment.yml 安装依赖，PyTorch 测试至 2.3 版本。面向计算机视觉研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DINOv2 ViT 与 TV 先验的无监督部件发现
- 支持 CUB、PartImageNet、Oxford Flowers、NABirds 四个数据集
- 模型可经 torch hub 与 HuggingFace 获取
- 提供训练/评测脚本与预处理工具

## 适用场景

- 复现论文中的部件发现与细粒度分类实验
- 在自选细粒度数据集上训练可解释部件发现模型
- 基于预训练模型做部件分割评测

## 场景标签

 · 领域:计算机视觉/细粒度分类

## 证据(README 行号)

> L1: # PDiscoFormer: Relaxing Part Discovery Constraints with Vision Transformers
> L7: Computer vision methods that explicitly detect object parts and reason on them are a step towards inherently interpr
> L13: 1. The code has been updated to support the NABirds dataset. The corresponding evaluation metrics and pre-trained m

## 星数曲线

```mermaid
xychart-beta
    title "ananthu-aniraj/pdiscoformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `393ccfb73972` · [字段定义](../../DATASET.md)*
