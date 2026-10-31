# NJUyued/PRG4SSL-MNAR

⭐ 76 · Python · 推送 2025-11-20 · [GitHub](https://github.com/NJUyued/PRG4SSL-MNAR) · 组织维护 · 中文 README

**ICCV 2023 论文官方代码：MNAR 非随机缺失标签下的半监督学习**

论文《Towards Semi-supervised Learning with Non-random Missing Labels》的官方 PyTorch 实现，面向半监督学习研究者。提出基于类别转移跟踪的伪标签校正引导（PRG），在类跟踪矩阵上建图并用马尔可夫随机游走获取类级引导，缓解标注/未标注数据类别分布不一致导致的伪标签偏置。提供单/多 GPU 训练脚本、多种 MNAR 协议（自建/CADR/DARP）与常规设定下的运行命令及预置权重，支持 CIFAR-10/100 和 mini-ImageNet，骨干网默认 WRN-28-2，可换 ResNet-18 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于类跟踪矩阵图上马尔可夫随机游走的伪标签校正引导（PRG）
- 支持 PRG/PRG^Last 两种变体及 CADR、DARP 等多种 MNAR 协议
- 提供 CIFAR-10/100、mini-ImageNet 各设定的复现命令与预训练权重
- 支持单 GPU 与多 GPU（DataParallel/DistributedDataParallel）训练

## 适用场景

- 复现 ICCV 2023 论文在 MNAR 设定下的半监督学习结果
- 在类别分布不一致的标注数据上训练图像分类模型
- 对比 PRG 与 DARP/CADR 等方法在缺失标签场景的表现

## 场景标签

 · 领域:计算机视觉/半监督学习

## 证据(README 行号)

> L3: This repo is the official Pytorch implementation of our paper:
> L25: Semi-supervised learning (SSL) tackles the label missing problem by enabling the effective usage of unlabeled data.

## 星数曲线

```mermaid
xychart-beta
    title "NJUyued/PRG4SSL-MNAR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-31 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e7548bb54b47` · [字段定义](../../DATASET.md)*
