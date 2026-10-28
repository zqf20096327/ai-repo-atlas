# radionets-project/radionets

⭐ 20 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/radionets-project/radionets) · [官网](https://radionets.readthedocs.io/en/latest/) · 组织维护

**用卷积神经网络重建射电干涉数据的深度学习框架**

Python 深度学习框架，面向射电干涉数据的模拟与分析：用卷积神经网络重建已校准观测并生成高分辨率图像。流程覆盖数据集模拟（MNIST 与高斯源）、模型训练（基于 pytorch 与 fastai）、以及评估（u-v 空间与图像空间绘图、MS-SSIM、视角与流量差直方图，并与 wsclean 对比）。以 Python 包提供，各任务通过安装到 PATH 的可执行脚本配合 toml 配置文件运行；模拟功能正迁往 pyvisgen 仓库，本仓库保留训练与评估部分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 卷积神经网络重建射电干涉观测，输出高分辨率图像
- 训练/评估/模拟脚本以 toml 配置驱动，数据存为 hdf5，模型存为 pickle
- 评估含 MS-SSIM、视角/源面积/流量差直方图并与 wsclean 对比
- 基于 pytorch 与 fastai 的训练框架

## 适用场景

- 射电天文学者用 CNN 重建干涉观测图像
- 训练并评估射电源重建的深度学习模型
- 生成射电干涉模拟数据集用于模型训练

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: Deep-learning framework for the simulation and analysis of radio interferometric data in Python. The goal is to reco
> L8: convolutional Neural Networks to create high-resolution images. For further information, please have a look at our p

## 星数曲线

```mermaid
xychart-beta
    title "radionets-project/radionets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `10b68559dce3` · [字段定义](../../DATASET.md)*
