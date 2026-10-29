# aria-ml/dataeval

⭐ 21 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/aria-ml/dataeval) · [官网](https://dataeval.readthedocs.io) · 组织维护

**计算机视觉数据质量与模型性能评估库：发现数据问题**

Python 库 dataeval，面向数据科学家、开发者与 T&E 工程师，提供覆盖机器学习全生命周期的数据评估工具：数据质量（重复/离群/优先级）、偏差分析、漂移检测与性能估计，支持图像分类与目标检测任务。输入路径分两类：dataeval.core 无状态函数直接处理 NumPy 数组；quality/bias/shift/performance 模块为有状态评估器，接受 NumPy 数组或 MAITE 协议数据集。与 JATIC 产品套件（MAITE 合规数据集/模型）原生互操作。安装支持 pip/uv/conda/GitHub 源码，Python 3.11-3.14，PyTorch 变体选择有详细说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重复项、离群值、平衡性等数据质量评估器与漂移检测
- 偏差分析与性能估计指标，覆盖 ML 全生命周期
- MAITE 协议数据集/模型互操作，兼容 JATIC 产品套件
- core 无状态函数直接处理 NumPy 数组（嵌入/标签/图像哈希/统计）

## 适用场景

- 训练前检测数据集中的近重复与离群样本
- 分析数据偏差与分布漂移对模型的影响
- T&E 工程师对视觉数据集做评估与清理

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: The `dataeval` package provides a rigorous and reliable set of tools for developing
> L26: needed for deployment. DataEval provides AI practitioners with a library of

## 星数曲线

```mermaid
xychart-beta
    title "aria-ml/dataeval 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `184a4adc6545` · [字段定义](../../DATASET.md)*
