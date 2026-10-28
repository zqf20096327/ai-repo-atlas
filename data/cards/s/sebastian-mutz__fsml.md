# sebastian-mutz/fsml

⭐ 26 · Fortran · MIT · 推送 2026-07-29 · [GitHub](https://github.com/sebastian-mutz/fsml) · [官网](https://fsml.mutz.science) · 个人维护

**面向科研的 Fortran 统计与机器学习库**

FSML 是用 Fortran 2008 编写的统计与机器学习工具库，提供五大模块：基础统计（均值、方差、相关）、假设检验（t 检验、Mann–Whitney U）、线性过程（多元 OLS 回归、判别分析）、非线性过程（k-means 聚类）与统计分布函数。核心过程保持纯函数以便并行化与测试，由非纯封装处理可选参数与错误。依赖最少（仅需 Fortran 2008 与 stdlib），以 FPM 包形式分发并附示例与测试。作者由其 15 年间积累的 Fortran 代码重写整理而来，配套手册含教程与 API 文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五大模块：STS/TST/LIN/NLP/DST 覆盖常用统计与机器学习过程
- 核心过程为纯函数以简化并行化与测试，非纯封装处理可选参数与错误
- 依赖最少：仅需 Fortran 2008 及以上与 stdlib
- 以 FPM 包分发，附示例与测试

## 适用场景

- 在 Fortran 科研应用中直接做统计检验与回归分析
- 需要与 Python/R 接口风格相近的 Fortran 统计库
- 对纯函数与可并行化有要求的数值计算项目

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: `FSML` (Fortran Statistics and Machine Learning) is a scientific toolkit consisting of common statistical and machin
> L20: FSML has five thematic modules: Basic statistics (STS), hypothesis tests (TST), linear procedures (LIN), non-linear

## 星数曲线

```mermaid
xychart-beta
    title "sebastian-mutz/fsml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `844db15391ed` · [字段定义](../../DATASET.md)*
