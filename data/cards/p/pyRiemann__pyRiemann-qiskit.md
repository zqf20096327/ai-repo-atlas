# pyRiemann/pyRiemann-qiskit

⭐ 30 · Python · BSD-3-Clause · 推送 2026-10-08 · [GitHub](https://github.com/pyRiemann/pyRiemann-qiskit) · [官网](https://pyriemann-qiskit.readthedocs.io/) · 组织维护

**面向 BCI/EEG 的量子机器学习分类库（基于 Qiskit 与 pyRiemann）**

Python 库，将 Qiskit 的量子分类算法与 pyRiemann 的黎曼几何结合，用于脑机接口与 EEG 数据的协方差矩阵分类。实现 QSVC、VQC 的封装以及带凸优化的量子 NCH 算法，以切空间向量化的协方差矩阵作为输入，遵循 scikit-learn API 约定。量子后端可为本地模拟器或远程量子硬件；限制包括本地模拟约 36 量子比特、量子算法计算开销大、官方建议仅用于离线分析。提供 PyPI 安装、源码安装与 Docker 镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QSVC/VQC 封装，输入黎曼切空间的向量化协方差矩阵
- 带凸优化与约束规划的量子 NCH（最近凸超球）算法
- 遵循 scikit-learn API 约定
- 支持本地模拟器与 IBM 远程量子后端

## 适用场景

- 在 EEG/BCI 数据上做量子分类实验
- 以切空间特征对比量子与经典 SVM 分类效果
- 作为量子分类实验的研究沙盒

## 场景标签

 · 领域:脑机接口/量子计算

## 证据(README 行号)

> L11: pyRiemann-qiskit bridges quantum computing (via Qiskit) with Riemannian geometry (via
> L13: implements quantum versions of Support Vector Classifiers (QSVC), Variational Quantum
> L21: - 🔬 **Quantum Classifiers**: QSVC and VQC implementations with Riemannian geometry

## 星数曲线

```mermaid
xychart-beta
    title "pyRiemann/pyRiemann-qiskit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9f0da05e4f19` · [字段定义](../../DATASET.md)*
