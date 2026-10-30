# osiriszjq/impulse_init

⭐ 15 · Jupyter Notebook · MIT · 推送 2025-12-09 · [GitHub](https://github.com/osiriszjq/impulse_init) · 组织维护

**论文官方实现：用卷积初始化提升 ViT 数据效率**

论文 'Convolutional Initialization for Data-Efficient Vision Transformers' 的官方代码实现，作者来自阿德莱德大学。提供修改版 ConvMixer 与 Simple ViT，在 CIFAR-10、CIFAR-100、SVHN 和 Tiny ImageNet 上进行实验；代码基于 vision-transformers-cifar10 仓库。使用方式为先修改 shell 脚本中的数据路径与实验配置，再运行 bash 脚本。提供 Colab 快速体验入口，论文发表于 arXiv（2401.12511），MIT 许可。

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

- 修改版 ConvMixer 与 Simple ViT 的官方实现
- 支持 CIFAR-10/CIFAR-100/SVHN/Tiny ImageNet 数据集
- 提供 Colab 快速体验入口

## 适用场景

- 复现论文中的卷积初始化实验
- 在小型数据集上训练 Vision Transformer
- 作为 ViT 初始化方法研究的代码基础

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L12: This is the official implementation of the paper "Convolutional Initialization for Data-Efficient Vision Transforme
> L33: @article{zheng2024convolutional,

## 星数曲线

```mermaid
xychart-beta
    title "osiriszjq/impulse_init 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dd98ff868269` · [字段定义](../../DATASET.md)*
