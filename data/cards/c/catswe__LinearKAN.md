# catswe/LinearKAN

⭐ 20 · Python · Apache-2.0 · 推送 2025-11-12 · [GitHub](https://github.com/catswe/LinearKAN) · [官网](https://catswe.github.io/KANditioned) · 个人维护

**面向研究者的快速 Kolmogorov-Arnold 网络 PyTorch 层实现**

基于 PyTorch 的 KAN 层实现：利用均匀线性 B 样条结构，将样条求值化为常数时间索引计算加两点线性插值，并重新表述为动态输入索引的稀疏-稠密矩阵乘法（SpMM，经 cuSPARSE）以加速训练与推理。提供 embedding_bag 与 embedding 两种实现选择、随机/恒等/零三种初始化、可视化样条映射方法，建议配合 torch.compile 与归一化层使用。README 自述含大量待办项（2:4 稀疏、Triton 核、基准测试等），部分功能为进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 均匀线性 B 样条求值化为索引查找+两点插值
- 表述为动态输入索引稀疏-稠密矩阵乘法（cuSPARSE）
- embedding_bag / embedding 两种实现可选
- KANLayer 可视化各样条映射（visualize_all_mappings）

## 适用场景

- 在 PyTorch 项目中替换/加入 KAN 层进行模型实验
- 研究 KAN 与 MLP 的性能对比
- 探索 2:4 半结构化稀疏与量化加速路线

## 场景标签

 · 领域:深度学习/神经网络组件

## 证据(README 行号)

> L1: # LinearKAN: A very fast implementation of Kolmogorov-Arnold Networks via Dynamic Input-Indexed Matrix Multiplicatio
> L3: Kolmogorov-Arnold Networks (KANs) training and inference are accelerated by orders of magnitude through exploiting t
> L24: from kanditioned.kan_layer import KANLayer

## 星数曲线

```mermaid
xychart-beta
    title "catswe/LinearKAN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9636b66e1b8c` · [字段定义](../../DATASET.md)*
