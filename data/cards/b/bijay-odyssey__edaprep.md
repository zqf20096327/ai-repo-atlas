# bijay-odyssey/edaprep

⭐ 16 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/bijay-odyssey/edaprep) · 个人维护

**面向 pandas 的防泄漏 EDA 与 ML 预处理库，带可解释规划器**

Python 库，为表格数据提供数据剖析、EDA 报告（quick/standard/deep 三级）与自动预处理流水线：推断语义类型并报告置信度，自动决定缺失值填补、离群值处理、类别编码与缩放等操作，每个决策附英文理由。通过将学习到的统计量限定在 fit 内计算来结构性防止训练/测试泄漏，并有逐行变换一致性测试断言。计划为可序列化数据，可打印、diff、复现。明确不涵盖模型训练、重采样、NLP、深度学习等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AutoPipeline 自动规划预处理并附每步理由（explain）
- 结构性防数据泄漏：transform 为纯函数，有整帧/逐行一致性测试
- 语义类型推断（带置信度）替代 dtype 粗分列
- 三级 EDA 分析（quick/standard/deep），含 VIF 与 Benjamini-Hochberg 校正

## 适用场景

- 表格 ML 任务前做防泄漏的 train/test 预处理
- 生成带理由说明的数据剖析与 EDA 报告
- 审计与覆写自动预处理决策并保持可复现

## 场景标签

 · 领域:数据科学/机器学习工具

## 证据(README 行号)

> L8: Transparent, leakage-safe EDA and ML preprocessing, with an explainable planner.
> L183: feature selection, datetime expansion, leakage-safe train/test preparation, pipelines,
> L186: **Out, deliberately:** model training, resampling, hyperparameter search, NLP,

## 星数曲线

```mermaid
xychart-beta
    title "bijay-odyssey/edaprep 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `64f288c44900` · [字段定义](../../DATASET.md)*
