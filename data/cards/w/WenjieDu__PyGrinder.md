# WenjieDu/PyGrinder

⭐ 71 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/WenjieDu/PyGrinder) · [官网](https://pypots.com/ecosystem/#PyGrinder) · 个人维护

**给数据科学家的 Python 工具包：按多种缺失机制向数据注入缺失值**

PyGrinder 是用于破坏数据完整性的 Python 工具包，提供多种缺失模式在给定数据上制造缺失值，包括 MCAR（完全随机）、MAR（随机）、MNAR（非随机）、子序列缺失与块缺失。它是 PyPOTS（部分可观测时间序列数据挖掘工具箱）的组成部分，原名 PyCorruptor，后为将缺失值生成功能与学习算法解耦而独立。适用场景如评估模型重建被破坏数据的能力、测试模型在部分可观测数据上的表现。以 Python 库形式提供，支持 conda、PyPI 与源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MCAR/MAR/MNAR 等多种缺失机制
- 支持子序列缺失与块缺失模式
- 从 PyPOTS 解耦独立，专司缺失值生成

## 适用场景

- 评估模型重建被破坏数据的能力
- 模拟真实世界的部分可观测数据以测试模型表现
- 为缺失值填补/插值研究构造实验数据

## 场景标签

 · 领域:数据科学/机器学习工具

## 证据(README 行号)

> L3: * a Python toolkit for grinding data beans into the incomplete *
> L55: data. PyGrinder is such a tool to help you corrupt your data, which provides several patterns to create missing val

## 星数曲线

```mermaid
xychart-beta
    title "WenjieDu/PyGrinder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-31 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f8a4754534c4` · [字段定义](../../DATASET.md)*
