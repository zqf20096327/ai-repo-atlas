# hofnerb/stabs

⭐ 27 · R · 推送 2026-01-30 · [GitHub](https://github.com/hofnerb/stabs) · [官网](https://cran.r-project.org/package=stabs) · 个人维护

**带有限样本误差控制的高维变量选择稳定性评估 R 包**

R 包，实现重采样过程来评估所选变量的稳定性，并为 Lasso、boosting 等高维变量选择方法提供有限样本误差控制。实现标准稳定性选择（Meinshausen & Bühlmann, 2010）与互补对稳定性选择（Shah & Samworth, 2013）。可与任意用户自定义的变量选择方法结合：通过自定义 fitfun（接受 x、y、q 参数，返回 selected 与 path）接入，或直接用于 mboost 的 boosting 模型。可通过 CRAN 或 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标准稳定性选择与互补对稳定性选择两种实现
- 有限样本误差控制
- 通过 fitfun 接入任意用户自定义变量选择方法
- 可直接应用于 mboost 计算的 boosting 模型

## 适用场景

- 评估 Lasso、boosting 等变量选择结果的稳定性
- 在高维数据上做带误差控制的变量选择
- 将自有选择方法封装为 fitfun 后做稳定性分析

## 场景标签

 · 领域:统计机器学习

## 证据(README 行号)

> L8: **stabs** implements resampling procedures to assess the stability of selected
> L9: variables with additional finite sample error control for high-dimensional
> L10: variable selection procedures such as Lasso or boosting. Both, standard

## 星数曲线

```mermaid
xychart-beta
    title "hofnerb/stabs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `86ef9bada425` · [字段定义](../../DATASET.md)*
