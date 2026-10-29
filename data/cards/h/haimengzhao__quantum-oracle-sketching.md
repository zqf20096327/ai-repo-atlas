# haimengzhao/quantum-oracle-sketching

⭐ 116 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/haimengzhao/quantum-oracle-sketching) · 个人维护

**论文配套代码：量子oracle sketching 算法的 JAX 实现**

论文 "Exponential quantum advantage in processing massive classical data" 的代码仓库，实现 Quantum Oracle Sketching（QOS）量子算法：用随机经典样本实例化量子查询算法所需的 oracle，将经典数据载入量子叠加态，无需全数据集内存开销。提供 JAX 实现（含 QSVT、振幅放大等）、快速入门 notebook、合成基准脚本，以及在 IMDb/20 Newsgroups/PBMC68k/Dorothea 四个真实数据集上的 SVM 分类与 PCA 降维实验流水线，并与特征哈希、稀疏 JL 等经典 sketch 方法对比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QOS 两种模拟模式：主动随机采样（qos_sampling.py）与期望酉实现（qos.py）
- JAX 实现的 QSVT，含振幅放大、求逆、阈值等
- 四个真实数据集的 SVM/PCA 实验与多种经典 oblivious sketch 基线对比
- 计算任务支持断点续跑与多核并行

## 适用场景

- 复现论文的基准图与真实数据集实验
- 通过 notebook 学习量子 oracle sketching 基本用法
- 对比量子方法与经典 sketching 方法的机器规模-性能关系

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Code repository for our paper "Exponential quantum advantage in processing massive classical data".
> L10: - Core implementations of **quantum oracle sketching** in JAX.
> L14: - Real-dataset experiments (classification and dimension reduction) for demonstrating the exponential memory advant

## 星数曲线

```mermaid
xychart-beta
    title "haimengzhao/quantum-oracle-sketching 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 114 --> 117
    line [115, 116, 116]
```

2026-10-18 115 → 2026-10-29 116（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `e410cf8cbd49` · [字段定义](../../DATASET.md)*
