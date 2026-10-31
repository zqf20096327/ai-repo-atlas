# pswpswpsw/nif

⭐ 76 · Jupyter Notebook · LGPL-2.1 · 推送 2026-10-29 · [GitHub](https://github.com/pswpswpsw/nif) · [官网](https://pswpswpsw.github.io/nif) · 个人维护

**时空 PDE 数据的网格无关降维库（Neural Implicit Flow）**

面向参数化时空场降阶建模的 Python 库，基于 TensorFlow 2.x 与 Keras 模型子类化实现，提供 NIF、NIFMultiScale 等模型类，支持单节点多 GPU 数据并行训练、Adam 后接 L-BFGS 微调的训练调度、tfrecord 大规模数据训练、子网络提取、输入输出 Jacobian/Hessian 计算、剪枝与量化压缩，以及多尺度问题的数据归一化。附 8 个 Google Colab 教程 Notebook，要求中标注 tensorflow-gpu 与 tensorflow_probability 等依赖，许可证为 LGPL-2.1，成果发表于 JMLR 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Keras 子类化的 NIF 模型类族（含多尺度与线性表示变体）
- 单节点多 GPU 数据并行与 L-BFGS 微调训练调度
- tfrecord 转换器支持百 GB 级数据的模型训练
- 剪枝、量化与 Jacobian/Hessian 层（可用于 Sobolev 训练）

## 适用场景

- 对自适应网格求解器输出的时空场做降维与降阶建模
- 拟合含高频成分的多尺度时空数据并控制伪信号
- 压缩 ParameterNet 子网络用于模型存储或部署

## 场景标签

 · 领域:科学计算/机器学习

## 证据(README 行号)

> L7: - NIF is a mesh-agnostic dimensionality reduction paradigm for parametric spatial temporal fields. For decades, dime
> L11: - NIF is built on top of Keras, in order to minimize user's efforts in using the code and maximize the existing fun
> L17: - Built on top of **Tensorflow 2.x** with **Keras model subclassing**, hassle-free for many up-to-date advanced con

## 星数曲线

```mermaid
xychart-beta
    title "pswpswpsw/nif 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-31 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b91b0e010345` · [字段定义](../../DATASET.md)*
