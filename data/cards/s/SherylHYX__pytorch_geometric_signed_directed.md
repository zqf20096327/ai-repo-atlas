# SherylHYX/pytorch_geometric_signed_directed

⭐ 150 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/SherylHYX/pytorch_geometric_signed_directed) · [官网](https://pytorch-geometric-signed-directed.readthedocs.io/en/latest/) · 组织维护

**PyTorch Geometric 的符号/有向图神经网络扩展库**

面向图神经网络研究者的 Python 扩展库，为 PyTorch Geometric 提供符号图与有向图上的模型、层、聚类与嵌入方法，实现来自多篇发表论文（NeurIPS、LoG、AAAI、SDM 等）。另含网络生成方法（SSBM/DSBM 等）、真实数据集加载器（Telegram、Cora_ml、CiteSeer、WikiCS 等）、任务专用损失与评估函数、预处理工具，并提供示例代码。依赖 Python>=3.10、PyTorch>=2.4、PyG>=2.6、NetworkX>=2.7，MIT 许可，论文被 LoG 2023 接收。

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

- 实现符号图/有向图的 GNN 模型与层（MagNet、SDGNN、SSSNET、MSGNN、DiGCN 等）
- 提供符号/有向随机块模型等合成网络生成方法
- 内置多个真实数据集加载器与数据类
- 提供任务专用损失函数、评估方法与预处理工具

## 适用场景

- 在符号/有向图上做节点分类、聚类或链接预测研究
- 复现相关论文方法或对比基线
- 加载符号/有向图常用数据集进行实验

## 场景标签

 · 领域:图机器学习/科研软件

## 证据(README 行号)

> L9: *PyTorch Geometric Signed Directed* is a signed and directed extension library for PyTorch Geometric. It follows the
> L11:  The library consists of various signed and directed geometric deep learning, embedding, and clustering methods fro

## 星数曲线

```mermaid
xychart-beta
    title "SherylHYX/pytorch_geometric_signed_directed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-31 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `384b8f1c92ce` · [字段定义](../../DATASET.md)*
