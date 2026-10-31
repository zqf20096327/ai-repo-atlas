# boost-R/FDboost

⭐ 21 · R · 推送 2026-04-12 · [GitHub](https://github.com/boost-R/FDboost) · 组织维护

**R 包：用梯度提升拟合函数数据回归模型**

FDboost 是一个 R 包，通过分量式梯度提升算法拟合函数数据回归模型，覆盖 scalar-on-function、function-on-scalar、function-on-function 以及 density-on-scalar 回归模型。使用文档包括 JSS 教程论文、含示例代码的手册和多篇 vignettes。安装方式支持从 CRAN 安装发布版，或通过 pak 从 GitHub 安装开发版；问题反馈走 GitHub Issues。

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

- 分量式梯度提升算法拟合函数回归
- 支持 scalar-on-function / function-on-scalar / function-on-function 回归
- 支持 density-on-scalar 密度回归
- 提供教程论文、手册与多篇 vignettes

## 适用场景

- 对函数型数据进行回归建模与变量选择
- 拟合一元响应或多类函数响应的回归模型
- 学习函数回归方法（教程论文与示例代码）

## 场景标签

 · 领域:统计机器学习/函数数据分析

## 证据(README 行号)

> L9: The package FDboost fits regression models for functional data, i.e.,
> L10: scalar-on-function, function-on-scalar, and function-on-function regression models,
> L11: by a component-wise gradient boosting algorithm.

## 星数曲线

```mermaid
xychart-beta
    title "boost-R/FDboost 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e4664a32960d` · [字段定义](../../DATASET.md)*
