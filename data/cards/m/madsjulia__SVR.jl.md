# madsjulia/SVR.jl

⭐ 19 · C++ · GPL-3.0 · 推送 2026-09-15 · [GitHub](https://github.com/madsjulia/SVR.jl) · [官网](http://mads.gitlab.io) · 组织维护

**Julia 支持向量回归库，封装 libSVM 做回归预测**

Julia 语言的 SVR.jl 包，调用 libSVM 库实现支持向量回归分析与预测，提供 RBF、LINEAR、POLY 等核函数选项，可读取 libSVM 格式输入文件。它是 MADS（Model Analysis & Decision Support）的组成模块，被 MADS、SmartTensors、SmartML 等项目使用。安装需 Julia 1.12 及以上，通过 Pkg.add 安装；README 附带正弦函数拟合与 libSVM 测试数据示例。

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

- 基于 libSVM 实现支持向量回归（fit/predict）
- 支持 RBF / LINEAR / POLY 等核函数
- 可读取 libSVM 格式输入文件
- MADS 模块，被 SmartTensors / SmartML 等项目使用

## 适用场景

- 在 Julia 中做支持向量回归建模与预测
- 作为 MADS / SmartTensors 工作流的机器学习组件
- 读取并处理 libSVM 格式数据集

## 场景标签

 · 领域:机器学习/数据分析

## 证据(README 行号)

> L3: Support Vector Regression (SVR) analysis in Julia utilizing the libSVM library.
> L30: Mads.plotseries([y SVR.fit(y, permutedims(X); kernel_type=SVR.RBF)], "figures/rbf.png"; title="RBF", names=["Truth"

## 星数曲线

```mermaid
xychart-beta
    title "madsjulia/SVR.jl 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [20, 19, 19]
```

2026-10-18 20 → 2026-10-29 19（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d4e845624351` · [字段定义](../../DATASET.md)*
