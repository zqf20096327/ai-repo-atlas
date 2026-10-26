# cdslaborg/paramonte

⭐ 307 · Fortran · NOASSERTION · 推送 2026-06-25 · [GitHub](https://github.com/cdslaborg/paramonte) · [官网](https://www.cdslab.org/paramonte) · 组织维护

**多语言串行/并行 Monte Carlo 采样与机器学习科学推断库**

ParaMonte 是面向科学推断的 Monte Carlo 采样与机器学习库，提供任意维密度函数采样（MCMC 等）与 ML 算法，核心可从 C、C++、Fortran、MATLAB、Python 调用（Python 版本正在内部测试，需从上一主版本获取）。设计目标包括模拟全自动化、零外部依赖、确定性可复现与自动重启；并行支持 Coarray、MPI 与 OpenMP，MPI 运行时（Intel MPI/OpenMPI/MPICH）为可选依赖。以 GitHub Release 预编译库或源码构建（CMake、GNU/Intel 编译器）方式分发，主体采用 MIT 许可并要求引用致谢。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 C/C++/Fortran/MATLAB/Python 多语言接口
- 零外部依赖核心，可选 MPI（Coarray/MPI/OpenMP 三种并行范式）
- 确定性可复现与自动重启功能
- GitHub Release 提供预编译库并附带示例代码与构建脚本

## 适用场景

- 对任意维数学密度函数做串行或并行 Monte Carlo 采样
- 科学推断场景下的贝叶斯 MCMC 计算
- 跨 Python/MATLAB/Fortran 等多语言环境复用同一推断库

## 场景标签

 · 领域:科学计算/统计推断

## 证据(README 行号)

> L39: ParaMonte is a serial/parallel library of Monte Carlo routines for sampling mathematical density functions of arbit
> L40: Machine Learning (ML) algorithms for scientific inference, with the design goal of unifying **automation** (of simu

## 星数曲线

```mermaid
xychart-beta
    title "cdslaborg/paramonte 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 306 --> 308
    line [307, 307]
```

2026-10-18 307 → 2026-10-26 307（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `58eae644457b` · [字段定义](../../DATASET.md)*
