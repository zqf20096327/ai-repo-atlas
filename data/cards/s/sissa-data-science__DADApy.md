# sissa-data-science/DADApy

⭐ 156 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/sissa-data-science/DADApy) · [官网](https://dadapy.readthedocs.io/) · 组织维护

**高维数据流形表征的 Python 库，供科研数据分析**

面向高维空间流形表征的 Python 包，提供五类算法：内蕴维度估计（Two-NN/Gride/I3D/BID）、密度估计（kNN/PAk/BMTI 等）、密度峰值聚类、流形比较（邻域重叠/信息不平衡）与因果分析。部分方法（DiffImbalance、CausalGraph）可经 GPU 版 JAX 运行。包内含 Cython 生成的 C 扩展，安装时自动编译；仅支持 Linux/macOS，Windows 需用 WSL。由 SISSA 数据科学团队维护，多数算法附发表论文出处。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类内蕴维度估计器与多种密度估计器
- 密度峰值聚类及其改进算法
- 邻域重叠与信息不平衡等流形比较工具
- DiffImbalance/CausalGraph 类支持经 GPU 版 JAX 运行

## 适用场景

- 估计高维数据集的内蕴维度
- 对高维数据做密度估计与密度峰值聚类
- 比较不同表示空间的信息含量与因果关系
- 为科研论文做基于距离的流形分析

## 场景标签

 · 领域:数据科学/机器学习

## 证据(README 行号)

> L8: DADApy is a Python package for the characterization of manifolds in high-dimensional spaces.
> L44: - Intrinsic dimension estimators

## 星数曲线

```mermaid
xychart-beta
    title "sissa-data-science/DADApy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 154 --> 157
    line [155, 156, 156]
```

2026-10-18 155 → 2026-10-27 156（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a5c0999d296a` · [字段定义](../../DATASET.md)*
