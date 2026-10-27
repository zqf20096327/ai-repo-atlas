# GuillaumeMougeot/biom3d

⭐ 31 · Python · GPL-3.0 · 推送 2026-03-30 · [GitHub](https://github.com/GuillaumeMougeot/biom3d) · [官网](https://biom3d.readthedocs.io/en/latest/index.html) · 个人维护

**自动配置 3D U-Net 训练的体积分割工具，面向显微/医学影像**

Biom3d 是用于 3D 图像语义分割的深度学习工具：自动配置 3D U-Net 的训练流程，提供 GUI、CLI 与 API 三种使用方式，支持即用模型预测与默认训练。面向社区用户（GUI/CLI、即用模型）与深度学习开发者（自定义配置、编写新模块、核心编辑）。默认配置在 BTCV 挑战上达到与 nnU-Net 相同的性能（未含交叉验证）。限制：暂不支持 2D U-Net、3D-Cascade U-Net 与 Pytorch 分布式并行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动配置 3D U-Net 训练流程
- 提供 GUI、CLI 与 API 三种使用方式
- 默认配置在 BTCV 挑战上达到与 nnU-Net 相同的性能
- 模块化代码架构，支持开发者扩展

## 适用场景

- 对 3D 显微/医学影像做语义分割
- 用默认配置快速训练分割模型，无需手动调参
- 开发者在其模块化架构上编写新模块或修改核心

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: Biom3d automatically configures the training of a 3D U-Net for 3D semantic segmentation.
> L26: * Community users, who are interested in using the basic functionalities of Biom3d: GUI or CLI, predictions with re

## 星数曲线

```mermaid
xychart-beta
    title "GuillaumeMougeot/biom3d 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ace07f247c1e` · [字段定义](../../DATASET.md)*
