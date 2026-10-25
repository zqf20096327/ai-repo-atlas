# stk-kriging/stk

⭐ 45 · MATLAB · GPL-3.0 · 推送 2026-01-13 · [GitHub](https://github.com/stk-kriging/stk) · 组织维护

**Matlab/Octave 的克里金（高斯过程）回归与实验设计工具箱**

面向 Matlab 与 GNU Octave 的克里金工具箱：基于高斯过程先验实现插值/回归，提供协方差函数库与协方差矩阵计算、协方差参数估计的 REMAP 过程、预测程序，以及顺序/非顺序实验设计工具。应用定位为计算机实验设计与分析（DACE），也可用于地质统计学、机器学习、非参数回归等。代码模块化、可复用，可用于实现 EGO、SUR 等算法。以全功能发布包（运行 stk_init 初始化）或 Octave 包（pkg install -forge stk）两种形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协方差函数库，支持平稳/非平稳、各向异性、广义协方差
- REMAP 过程估计协方差参数，可纳入参数先验知识
- 顺序与非顺序实验设计工具
- 提供 EGO/SUR 等算法实现基础，附 stk_example_ 系列示例

## 适用场景

- 在 Matlab/Octave 中做克里金/高斯过程回归建模
- 昂贵黑箱函数的全局优化与计算机实验设计
- 实现 SUR 类高级序贯设计算法的研究原型

## 场景标签

 · 领域:科学计算/机器学习

## 证据(README 行号)

> L35:  Description: The STK is a (not so) Small Toolbox for Kriging. Its
> L40:  Gaussian Process (GP) prior. The STK also provides tools

## 星数曲线

```mermaid
xychart-beta
    title "stk-kriging/stk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0c8a0c04c10e` · [字段定义](../../DATASET.md)*
