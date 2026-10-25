# dragonfly-ai/slash

⭐ 41 · Scala · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/dragonfly-ai/slash) · [官网](https://dragonfly-ai.github.io/slash/) · 个人维护

**Scala 线性代数与统计库，跨 JVM/Native/JS 平台**

面向 Scala 开发者的数学库：以原生 double 数组存储向量与矩阵数据，通过 Scala 3 的 opaque types、dependent types 与扩展方法提供运算符语法，并在编译期检查向量/矩阵维度匹配。功能覆盖矩阵运算与分解（Cholesky、特征值、LU、QR、SVD）、线性回归、主成分分析、参数与流式概率分布、核函数、直方图文本可视化等。跨编译到 JVM、Native 与 JavaScript 平台，JavaScript 环境使用 Float64Array。以 sbt 依赖形式提供，始于 JAMA 的移植并演化为纯 Scala 实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 矩阵分解：Cholesky、Eigen、LU、QR、SVD
- 编译期维度检查防止向量/矩阵维度不匹配的运行时错误
- 跨编译到 JVM、Scala Native、Scala.js 三平台
- 参数式与流式（在线估计）概率分布及采样

## 适用场景

- 在 Scala 项目中做矩阵运算、线性回归与 PCA
- 构建需要概率分布采样与统计估计的应用
- 跨 JVM/Native/JS 平台复用同一套数学代码

## 场景标签

 · 领域:科学计算/数学库

## 证据(README 行号)

> L2: Scala Linear Algebra & Statistics Hacks
> L8:  Cross compile to JVM, Native, and JavaScript platforms
> L46: - Linear Regression based on both QR Decomposition and Singular Value Decomposition.
> L47: - Principal Components Analysis

## 星数曲线

```mermaid
xychart-beta
    title "dragonfly-ai/slash 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e471b27ad156` · [字段定义](../../DATASET.md)*
