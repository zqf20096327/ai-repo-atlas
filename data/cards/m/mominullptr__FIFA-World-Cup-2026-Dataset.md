# mominullptr/FIFA-World-Cup-2026-Dataset

⭐ 68 · Python · CC0-1.0 · 推送 2026-10-18 · [GitHub](https://github.com/mominullptr/FIFA-World-Cup-2026-Dataset) · [官网](https://mominullptr.github.io/FIFA-World-Cup-2026-Dataset/) · 个人维护

**2026 世界杯 3NF 关系型数据集：104 场比赛与球员数据**

覆盖 2026 年 FIFA 世界杯（48 队、104 场比赛）的 3NF 关系型数据集：12 张表含球队、球场地理信息、1,248 名球员注册数据、逐分钟比赛事件、VAR 记录、xG 指标与逐队逐场统计，数据来自 FIFA.com 及验证供应商。数据经 9 阶段程序化校验与 30 场人工抽查（99.87% 准确率），并附 65 特征的防泄漏 ML 预测矩阵与基线基准。以 SQLite、Parquet、CSV 三种格式分发，面向体育分析与机器学习研究者，配有 Research Square 数据描述论文（在审）与引用格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 张 3NF 关系表，SQLite/Parquet/CSV 三格式分发
- 104 场比赛完整结果、事件、阵容与 xG 数据
- 65 特征防泄漏 ML 预测矩阵（ELO、FIFA 排名、滚动状态等）
- 9 阶段程序化校验 + 30 场 TSG 人工抽查（99.87%）

## 适用场景

- 做世界杯比赛结果预测的机器学习建模
- 用 SQL 做足球赛事数据的关系型建模与分析
- 体育分析研究论文的数据来源（附引用格式）

## 场景标签

 · 领域:体育数据/数据科学

## 证据(README 行号)

> L47: **The most complete and actively maintained FIFA World Cup 2026 relational benchmark.** A clean, authentic, 3NF-nor
> L112: Skip tedious feature engineering. This repository provides pre-engineered machine learning matrices:

## 星数曲线

```mermaid
xychart-beta
    title "mominullptr/FIFA-World-Cup-2026-Dataset 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-27 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a947380cb652` · [字段定义](../../DATASET.md)*
