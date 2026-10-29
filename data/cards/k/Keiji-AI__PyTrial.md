# Keiji-AI/PyTrial

⭐ 131 · Python · BSD-2-Clause · 推送 2026-08-01 · [GitHub](https://github.com/Keiji-AI/PyTrial) · [官网](https://pytrial.readthedocs.io/en/latest/) · 组织维护

**面向药物开发与临床试验的 Python AI 任务库**

Python 机器学习包，为 ML 研究者与医疗从业者提供临床试验相关任务的现成流水线，覆盖患者结局预测、试验点选择、试验结果预测、患者-试验匹配、试验相似性检索与试验数据模拟六类任务，算法复现自近期顶会论文。所有任务遵循 load data → define model → fit and predict 的统一接口，提供预处理演示数据与分任务教程，另含 ICD9/10 与药物知识图谱等附加资源。需先安装 PyTorch，推荐从 GitHub 源码安装，Python 3.7 上测试，不推荐暂从 PyPI 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六类临床试验任务的现成流水线（结局预测、患者-试验匹配等）
- 所有任务统一 fit/predict 接口
- 提供预训练 BERT 模型、ICD9/10 与药物知识图谱等附加资源
- 每个算法附带预处理演示数据与交互示例

## 适用场景

- 我用它复现顶会的临床试验 AI 算法做研究
- 我在医疗数据上做患者结局或试验结果预测
- 我做患者与临床试验的匹配分析

## 场景标签

 · 领域:生物医学/药物开发

## 证据(README 行号)

> L28: - :key: Off-the-shelf pipelines for various clinical trial tasks proposed in the most recent top-venue papers.
> L30: - :fire: A comprehensive implementation of many AI for drug development tasks:
> L31: 	- Patient outcome prediction.

## 星数曲线

```mermaid
xychart-beta
    title "Keiji-AI/PyTrial 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 129 --> 132
    line [130, 131, 131]
```

2026-10-18 130 → 2026-10-29 131（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fad9ab95cc33` · [字段定义](../../DATASET.md)*
