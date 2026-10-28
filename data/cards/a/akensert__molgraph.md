# akensert/molgraph

⭐ 65 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/akensert/molgraph) · [官网](https://molgraph.readthedocs.io/en/latest/) · 个人维护

**面向分子机器学习的 TensorFlow/Keras 图神经网络库**

基于 TensorFlow 和 Keras 实现的图神经网络 Python 库，聚焦分子机器学习场景。提供 GraphTensor 复合张量（兼容 tf.data.Dataset 与 keras.Sequential）、多种图卷积/图注意力/消息传递层、预处理与后处理层、位置编码层及图神经网络模型和显著性映射。分子数据经预处理层转为图张量后可直接接入 Keras Sequential API 训练。README 注明 Keras 3 兼容性由后续项目 MolCraft 提供，本库有相关论文预印本。

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

- GraphTensor 复合张量兼容 tf.data.Dataset 与 keras.Sequential
- 提供图卷积/图注意力/消息传递/读出/位置编码等多种 GNN 层
- Keras Sequential API 构建 GNN 模型
- 支持显著性映射（saliency mapping）

## 适用场景

- 构建分子性质预测的 GNN 模型管线
- 在 Keras 工作流中处理分子图数据
- 通过显著性映射解释 GNN 预测结果

## 场景标签

 · 领域:计算化学/生物信息学

## 证据(README 行号)

> L3: **Graph Neural Networks** with **TensorFlow** and **Keras**. Focused on **Molecular Machine Learning**.
> L46:  - Graph convolutional layers

## 星数曲线

```mermaid
xychart-beta
    title "akensert/molgraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-28 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a55d97c76c1d` · [字段定义](../../DATASET.md)*
