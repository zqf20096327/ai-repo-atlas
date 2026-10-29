# qmlcode/qmllib

⭐ 28 · Python · MIT · 推送 2026-02-21 · [GitHub](https://github.com/qmlcode/qmllib) · [官网](https://qmlcode.org) · 组织维护

**分子与固体机器学习的表示和核函数工具库**

Python/Fortran 工具包，为分子和固体性质的机器学习提供表示（representation）与核（kernel）等基础构件，而非高层框架（无 model.train() 抽象）。实现 FCHL19/FCHL18、Coulomb Matrix、Bag of Bonds、SLATM、ACSF、AARAD 等表示，并附各方法论文引用。通过 PyPI 提供 Linux/macOS 预编译 wheel（OpenBLAS/Accelerate、OpenMP），源码安装需 Fortran 编译器与 BLAS。从原 QML 包迁移而来，接口有破坏性变更，采用自由函数设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 FCHL19/FCHL18、Coulomb Matrix、Bag of Bonds、SLATM、ACSF、AARAD 等分子表示
- Python/Fortran 实现，预编译 wheel 带优化 BLAS 与 OpenMP 支持
- 自由函数设计，不提供高层模型训练抽象
- 附各表示方法对应的论文引用信息

## 适用场景

- 为分子/固体性质预测构建机器学习特征表示
- 科研中复现或使用 FCHL 等量子机器学习方法
- 从原 qml 包迁移到更新的核心库接口

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: `qmllib` is a Python/Fortran toolkit for representation of molecules and solids for machine learning of properties 
> L14: `qmllib` represents the core library functionality derived from the original QML package, providing a powerful tool

## 星数曲线

```mermaid
xychart-beta
    title "qmlcode/qmllib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f0b79f79bb1a` · [字段定义](../../DATASET.md)*
