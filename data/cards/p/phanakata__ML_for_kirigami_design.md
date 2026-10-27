# phanakata/ML_for_kirigami_design

⭐ 30 · Jupyter Notebook · BSD-3-Clause · 推送 2026-01-28 · [GitHub](https://github.com/phanakata/ML_for_kirigami_design) · 个人维护

**面向科研者：用深度学习做石墨烯剪纸的拓扑优化设计**

Python 科研代码包，使用类似 VGGNet 的卷积神经网络对石墨烯剪纸（kirigami）结构做回归建模与拓扑优化搜索。提供生成 LAMMPS 分子动力学输入原子构型的 Jupyter notebook、TensorFlow 与 PyTorch 版 CNN 回归训练代码、最优设计搜索代码、scikit-learn 简单预测 notebook，以及有监督自编码器实现正/逆向设计。附带用 AIREBO 势生成的粗粒度网格原始数据集。README 声明包仍在开发中，功能将持续添加；安装方式仅 git clone。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- VGGNet 类 CNN 做石墨烯剪纸性能回归
- TensorFlow 与 PyTorch 双版本 CNN 回归模型
- 有监督自编码器支持正/逆向设计
- 含 LAMMPS 输入构型生成 notebook 与 AIREBO 势数据集

## 适用场景

- 用机器学习加速可拉伸石墨烯剪纸结构的搜索与设计
- 生成 LAMMPS 分子动力学模拟的剪纸原子构型
- 复现论文中的 CNN 回归与自编码器正逆向设计方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L2: Python package to model and to perform topology optimization for graphene kirigami using deep learning. We use convo
> L19: * A python code to perform regression with TensorFlow is avalaible in `models_regression/CNN_regression/tf_fgrid_dn

## 星数曲线

```mermaid
xychart-beta
    title "phanakata/ML_for_kirigami_design 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5c489ccf55b7` · [字段定义](../../DATASET.md)*
