# fspinna/pyrregular

⭐ 25 · Python · BSD-3-Clause · 推送 2026-10-18 · [GitHub](https://github.com/fspinna/pyrregular) · [官网](https://fspinna.github.io/pyrregular/) · 个人维护

**不规则时间序列的 Python 框架：34 个数据集与分类基准**

ICLR 2026 论文配套的 Python 框架，处理采样不均匀、缺失观测、变长序列的不规则时间序列。提供 34 个标准化数据集（按需从 Hugging Face 下载、版本固定）、保留不规则性的稀疏 xarray 表示（可转换为 sktime/aeon/tslearn/PyPOTS 的稠密数组），以及 13 个分类管线（含论文评估的 12 个分类器）。回归功能仍在开发中；管线封装第三方库，上游版本变化可能破坏复现，需固定版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 34 个天然不规则数据集统一格式，按需下载且版本固定
- 稀疏 xarray 表示，支持转换到 sktime/aeon/tslearn/PyPOTS
- 13 个即用分类管线，含论文评估的 12 个分类器
- list_paper_models()/get_paper_model() 复现论文设置

## 适用场景

- 用统一格式加载不规则时间序列数据集做分类实验
- 复现或对比 ICLR 2026 基准中的分类器结果
- 把不规则数据稠密化后接入 sktime/tslearn 等现有库

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: Pyrregular is a Python framework for irregular time series: irregularly sampled
> L16: - **models and benchmarks**: ready-to-use classification and regression pipelines,

## 星数曲线

```mermaid
xychart-beta
    title "fspinna/pyrregular 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `17065597363c` · [字段定义](../../DATASET.md)*
