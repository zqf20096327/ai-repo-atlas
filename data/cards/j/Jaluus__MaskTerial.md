# Jaluus/MaskTerial

⭐ 24 · Jupyter Notebook · MIT · 推送 2026-01-19 · [GitHub](https://github.com/Jaluus/MaskTerial) · [官网](https://datagen.uslu.tech) · 组织维护

**面向显微图像的 2D 材料薄片检测与分类基础模型**

MaskTerial 是基于实例分割网络的深度学习模型，用于从光学显微图像中实时检测和分类剥离的二维材料薄片。模型先用合成数据生成器（从无标注数据生成逼真显微图像）做大规模预训练，随后仅需 5-10 张图像即可适配新材料；另用不确定性估计模型按光学对比度对预测做最终分类。提供预训练权重（Zenodo）、Colab 演示、Docker 推理服务器与前端，代码/数据/模型以 MIT 许可开源。论文发表于 Digital Discovery，测试环境为 Python 3.12，GPU 安装路径需 CUDA 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实例分割网络检测 2D 材料薄片，预训练后 5-10 张图像即可适配新材料
- 合成数据生成器从无标注数据生成逼真显微图像用于预训练
- 不确定性估计模型按光学对比度对预测做最终分类
- 提供 Colab 演示、Docker 推理服务器与前端、Zenodo 预训练权重与数据集

## 适用场景

- 从显微图像中自动检测二维材料薄片，减少人工标注
- 在低对比度材料（如六方氮化硼）样品中定位薄片
- 新材料的少样本快速适配检测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L13: This repository hosts the code and related resources for the MaskTerial project, a robust Deep-Learning based model
> L20: Here, we present a deep learning model, called MaskTerial, that uses an instance segmentation network to reliably i
> L24: We evaluate our method on eight different datasets comprising five different 2D materials and demonstrate significa

## 星数曲线

```mermaid
xychart-beta
    title "Jaluus/MaskTerial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `408c62845c94` · [字段定义](../../DATASET.md)*
