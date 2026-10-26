# msuzen/isingLenzMC

⭐ 53 · Jupyter Notebook · NOASSERTION · 推送 2026-05-12 · [GitHub](https://github.com/msuzen/isingLenzMC) · 个人维护

**一维 Ising 模型蒙特卡洛模拟的 R 包（含 C 核心）**

R 语言科学计算包，提供 Metropolis 与 Glauber 单自旋翻转动力学的一维 Ising 模型蒙特卡洛模拟，支持周期性边界条件，并附带传递矩阵等精确解工具函数；核心部分用 C 库实现。面向统计物理研究者，用于测量有效遍历性、幂律等功能扩散分析。包已被两篇同行评审论文使用，examples 目录提供论文结果复现脚本；部分功能（有限尺寸缩放、自相关、自助误差棒等）尚未进入主包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Metropolis 与 Glauber 动力学的一维 Ising 模型模拟
- 传递矩阵等 1D 精确解工具函数
- 核心 C 库实现，CRAN 有稳定发布版
- examples 目录复现两篇论文结果

## 适用场景

- 统计物理中模拟一维 Ising 模型的相变与自旋玻璃行为
- 测量单自旋翻转动力学的有效遍历性与幂律
- 复现相关论文数据集与分析流程

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L18: in general, for example phase transitions and neural networks. This package provides
> L19: utilities to simulate one dimensional Ising Model with Metropolis and Glauber Monte
> L20: Carlo with single flip dynamics in periodic boundary conditions. Utility functions

## 星数曲线

```mermaid
xychart-beta
    title "msuzen/isingLenzMC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b6b54ec55cef` · [字段定义](../../DATASET.md)*
