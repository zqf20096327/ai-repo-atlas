# mauriceqch/2021_pc_perceptual_loss

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-02-06 · [GitHub](https://github.com/mauriceqch/2021_pc_perceptual_loss) · 组织维护

**3D 点云深度感知度量的论文代码：训练与复现脚本**

论文《A deep perceptual metric for 3D point clouds》（EI 2021）的官方代码仓库：实现用于 3D 点云质量评估的感知损失神经网络模型，提供训练 notebook、ModelNet40 训练数据集、预训练模型（binary 与 TDF 两种表示），以及复现 ICIP2020 主观数据集实验的主 notebook。基于 Python 3.6.9 与 Tensorflow 1.15.0（CUDA 10.0.130、cuDNN 7.4.2），建议在 Ubuntu 上运行，含数据集重打包与点云处理脚本。

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

- 提供感知损失神经网络模型与训练 notebook
- 仓库内置 ModelNet40 训练数据集与预训练模型（binary/TDF）
- 主 notebook 可复现论文全部结果
- 附带 ICIP2020 主观数据集重打包脚本

## 适用场景

- 复现论文中 3D 点云质量评估实验结果
- 基于 ModelNet40 训练点云感知度量模型
- 用预训练模型预测点云 MOS 分数

## 场景标签

 · 领域:计算机视觉/点云处理

## 证据(README 行号)

> L1: # A deep perceptual metric for 3D point clouds
> L66:  └── perceptual_model.py Perceptual loss neural network model
> L90: The notebook in `src/train_perceptual.ipynb` performs the training of the models described in the paper.

## 星数曲线

```mermaid
xychart-beta
    title "mauriceqch/2021_pc_perceptual_loss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a65b72b0bdc8` · [字段定义](../../DATASET.md)*
