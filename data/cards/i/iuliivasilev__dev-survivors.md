# iuliivasilev/dev-survivors

⭐ 41 · Python · BSD-3-Clause · 推送 2026-02-02 · [GitHub](https://github.com/iuliivasilev/dev-survivors) · [官网](https://iuliivasilev.github.io/dev-survivors/) · 个人维护

**Python 生存分析库：处理删失与异构数据的树模型与集成**

莫斯科国立大学博士项目中开发的生存分析 Python 库，面向医疗（死亡/出院预测）、设备维护（故障预测）与商业分析（客户流失）等场景。基于生存树（CRAID）与集成（Bootstrap/Boosting）建模，支持信息性删失与任意时间-事件分布，预测时保持连续时间；提供 20+ 内置数据集、10+ 个应对删失与不平衡的自定义评估指标，以及含交叉验证与超参搜索的可复现实验模块。依赖 NumPy/Numba 等，经 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRAID 生存决策树及 Bootstrap/Boosting 集成模型
- 处理信息性删失与任意时间-事件分布，预测为连续时间
- 内置 20+ 真实数据集与 10+ 删失感知评估指标
- 含 hold-out、交叉验证、时间感知切分与超参搜索的实验模块

## 适用场景

- 医疗场景做死亡或出院时间的生存预测
- 预测设备故障时间以安排预防性维护
- 客户流失/留存时间建模与分层分析

## 场景标签

 · 领域:机器学习/生存分析

## 证据(README 行号)

> L20: **Survivors** is a Python library for survival analysis designed to handle real-world, messy, and heterogeneous dat
> L31: Survivors was developed during a PhD project at Lomonosov Moscow State University to overcome the limitations of tr
> L84: * **CRAID** – interpretable decision tree model for survival analysis. [1]_

## 星数曲线

```mermaid
xychart-beta
    title "iuliivasilev/dev-survivors 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-27 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e231c04edef9` · [字段定义](../../DATASET.md)*
