# danielegrattarola/spektral

⭐ 2,403 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/danielegrattarola/spektral) · [官网](https://graphneural.network) · 个人维护

**基于 Keras/TensorFlow 2 的图神经网络 Python 库**

面向图深度学习的 Python 库，构建于 Keras API 与 TensorFlow 2 之上，目标是提供简洁而灵活的图神经网络（GNN）构建框架。实现 GCN、GraphSAGE、GAT、GIN 等多种卷积层，以及 MinCut、DiffPool、Top-K 等池化层；提供图表示、操作与变换的工具集，1.0 版引入 Graph/Dataset 数据容器、Loader 批处理类、transforms 模块与 GeneralConv/GeneralGNN 通用模型类，附带 QM7、ModelNet10/40 数据集及 OGB 封装。支持 Python 3.6+，可在 Ubuntu/macOS/Windows 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 GCN、GraphSAGE、GAT、GIN、APPNP 等多种图卷积层
- 提供 MinCut、DiffPool、Top-K、SAG 等池化层
- 1.0 版提供 Graph/Dataset 容器、Loader 批处理与 transforms 模块
- 内置 QM7、ModelNet10/40 数据集与 OGB 数据集封装

## 适用场景

- 对社交网络用户做节点分类
- 预测分子性质
- 用 GAN 生成新图或做链接预测
- 对图数据节点做聚类

## 场景标签

 · 领域:机器学习/图深度学习

## 证据(README 行号)

> L2: Spektral is a Python library for graph deep learning, based on the Keras API and TensorFlow 2.
> L3: The main goal of this project is to provide a simple but flexible framework for creating graph neural networks (GNNs
> L5: You can use Spektral for classifying the users of a social network, predicting molecular properties, generating new 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `333a0ee889bb` · [字段定义](../../DATASET.md)*
