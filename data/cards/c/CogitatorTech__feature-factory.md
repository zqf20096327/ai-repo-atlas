# CogitatorTech/feature-factory

⭐ 23 · Rust · Apache-2.0 · 推送 2025-12-10 · [GitHub](https://github.com/CogitatorTech/feature-factory) · 组织维护

**Rust 特征工程库：数据变换、编码与特征选择工具集**

基于 Apache DataFusion 构建的 Rust 特征工程库，提供缺失值填充、类别编码、离散化、异常值处理、数值变换、特征创建、日期特征与特征选择等约 40 个 transformer，遵循 fit-transform 范式，API 设计参考 Scikit-learn，并支持 make_pipeline 宏串联多个 transformer。面向使用 Rust 做数据科学流程的开发者。README 声明项目处于早期开发阶段，API 不稳定，尚未充分测试与基准测试；要求 Rust 1.83 或更高版本，通过 cargo 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 约 40 个 transformer 覆盖填充/编码/离散化/特征选择等任务
- 基于 Apache DataFusion 的内存数据处理
- Scikit-learn 风格 fit-transform API 与 pipeline 串联机制
- MIT/Apache-2.0 双许可发布

## 适用场景

- 在 Rust 数据流水线中做缺失值填充与类别编码
- 训练前进行特征选择（相关性/信息值/MRMR 等）
- 将多个预处理步骤串联为可复用的 pipeline

## 场景标签

 · 领域:数据科学/机器学习工具库

## 证据(README 行号)

> L15: Feature Factory is a feature engineering library for Rust built on top
> L19: provides a wide range of components (referred to as transformers) for common feature engineering tasks like imputat
> L24: Feature Factory transformers follow a fit-transform paradigm

## 星数曲线

```mermaid
xychart-beta
    title "CogitatorTech/feature-factory 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [23, 22, 23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `943f9da195c1` · [字段定义](../../DATASET.md)*
