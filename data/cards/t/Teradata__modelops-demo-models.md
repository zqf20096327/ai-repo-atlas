# Teradata/modelops-demo-models

⭐ 10 · Jupyter Notebook · BSD-3-Clause · 推送 2026-11-24 · [GitHub](https://github.com/Teradata/modelops-demo-models) · [官网](https://www.teradata.com/platform/clearscape-analytics/modelops) · 组织维护

**Teradata Vantage ModelOps 糖尿病预测示例模型仓库**

Teradata 提供的 Vantage ModelOps 演示用途模型代码仓库，示例场景为基于 PIMA 数据集的糖尿病分类预测。仓库按模型管理方式分三类：Git 管理的完整训练/评估/打分代码（含 Python 与 R，附 notebook）、BYOM 方式（生成 PMML 工件并在 Teradata 中动态查询，支持 ONNX 格式）、以及 STO 方式（在数据分区上训练和打分微模型）。目标是提供简单参考实现，而非详尽的数据科学用例教程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Python 与 R 两种语言的糖尿病预测示例
- 支持 BYOM 开放模型格式（PMML/ONNX）在 Teradata 中查询
- STO 按数据分区训练、评估和打分微模型

## 适用场景

- 参考实现自己的 ModelOps 模型接入流程
- 学习如何在 Teradata 中用 PMML/ONNX 做数据库内预测
- 了解 Python/R 模型的训练、评估与打分代码结构

## 场景标签

 · 领域:MLOps/数据平台示例

## 证据(README 行号)

> L3: This repository contains the example Diabetes Prediction model code for Vantage ModelOps. We provide a number of dem
> L9: The example use case we deal with in this demo project is diabetes prediction. More specifically, we use the PIMA di

## 星数曲线

```mermaid
xychart-beta
    title "Teradata/modelops-demo-models 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6823cb906ecd` · [字段定义](../../DATASET.md)*
