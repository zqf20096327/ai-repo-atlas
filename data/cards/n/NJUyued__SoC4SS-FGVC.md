# NJUyued/SoC4SS-FGVC

⭐ 14 · Python · MIT · 推送 2025-11-20 · [GitHub](https://github.com/NJUyued/SoC4SS-FGVC) · 组织维护

**半监督细粒度图像分类方法的官方 PyTorch 实现（AAAI 2024）**

论文 "Roll with the Punches: Expansion and Shrinkage of Soft Label Selection for Semi-supervised Fine-Grained Learning" 的官方 PyTorch 代码，面向计算机视觉研究者复现实验。方法核心包括置信度感知的 k 选择（--alpha）与类别转移跟踪 CTT（基于 centroids 的 k-means 聚类与 label_matrix），通过软标签选取的扩张与收缩处理半监督细粒度学习。支持 Semi-Fungi 与 Semi-Aves 两个数据集、分布内/分布外两类未标注数据、多种骨干网络（ResNet 系列/WRN/CNN-13），提供单 GPU 与多 GPU（DataParallel/DistributedDataParallel）训练及预训练模型加载，并附各配置下的 Top1/Top5 精度与 checkpoint。需自行下载配置数据集与 Python 环境。

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

- 置信度感知 k 选择（--alpha）与类别转移跟踪（CTT）机制
- 支持 Semi-Fungi / Semi-Aves 数据集，分布内与分布外未标注数据两种设定
- 可选 ResNet-18/50/101、WRN、PreAct ResNet、CNN-13 等骨干网络
- 支持单 GPU、DataParallel 与 DistributedDataParallel 训练，附各配置精度与 checkpoint

## 适用场景

- 复现 AAAI 2024 论文的半监督细粒度分类实验结果
- 在鸟类/真菌细粒度数据上做半监督学习实验对比
- 基于提供的 checkpoint 做评估或二次研究

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repo is the official Pytorch implementation of our paper:
> L32: - `--net [resnet18/resnet50/resnet101/wrn/wrnvar/preresnet/cnn13]`: By default, ResNet-50 is used for experiments. 

## 星数曲线

```mermaid
xychart-beta
    title "NJUyued/SoC4SS-FGVC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `51a7d00faef8` · [字段定义](../../DATASET.md)*
