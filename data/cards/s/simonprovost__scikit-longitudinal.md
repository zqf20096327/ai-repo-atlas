# simonprovost/scikit-longitudinal

⭐ 84 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/simonprovost/scikit-longitudinal) · [官网](https://scikit-longitudinal.readthedocs.io/latest/) · 个人维护

**面向纵向（长期追踪）数据的 Scikit-Learn 风格机器学习库**

构建在 Scikit-Learn 之上的 Python 库，面向纵向数据的监督学习（当前聚焦分类任务）：提供 LongitudinalDataset 数据准备工具与 LexicoGradientBoostingClassifier 等估计器，用于处理、分析与预测同一对象在多个时间点重复测量的数据（如患者多年体检指标预测健康风险）。接口设计与 Scikit-Learn 生态系统集成，支持 Python 3.10–3.13，pip 安装，附 JOSS 论文可供引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纵向数据专用估计器（如 LexicoGradientBoostingClassifier）
- LongitudinalDataset 数据准备与处理工具
- 与 Scikit-Learn 生态系统集成
- 支持 Python 3.10–3.13，pip 安装

## 适用场景

- 用患者多年重复体检指标做健康风险分类预测
- 对长期追踪的纵向数据集进行预处理与建模
- 在 Scikit-Learn 工作流中引入纵向数据专用算法

## 场景标签

 · 领域:健康/医疗机器学习

## 证据(README 行号)

> L30: `Scikit-longitudinal` (Sklong) is a machine learning library tailored for Longitudinal machine (supervised) learnin
> L35: similar to checking in on patients to see how they change. For instance, doctors may monitor a patient's blood pres

## 星数曲线

```mermaid
xychart-beta
    title "simonprovost/scikit-longitudinal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-24 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fbb98d457330` · [字段定义](../../DATASET.md)*
