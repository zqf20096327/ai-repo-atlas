# fat-forensics/fat-forensics

⭐ 79 · Python · BSD-3-Clause · 推送 2026-04-13 · [GitHub](https://github.com/fat-forensics/fat-forensics) · [官网](https://fat-forensics.org) · 组织维护

**评估预测系统公平性、问责性与透明度的 Python 工具箱**

FAT Forensics（fatf）是基于 SciPy/NumPy 的 Python 工具箱，针对数据建模管线的三个环节——数据、模型、预测——实现公平性（fairness）、问责性（accountability）与透明性（transparency）算法。设两种用法：面向研究者的交互式 research mode 用于探索性分析，面向工程实践者的 deployment mode 用于监控预测系统的 FAT 表现。依赖 Python 3.5+，必需依赖仅 NumPy 与 SciPy，另有 scikit-learn、scikit-image、Pillow、matplotlib 等可选依赖按模块启用；以 3-Clause BSD 许可分发，由 Thales 与布里斯托大学合作研究产出，有 JOSS 论文。

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

- 覆盖数据、模型、预测三个层面的 FAT 算法实现
- research mode（探索分析）与 deployment mode（系统监控）两种使用方式
- 必需依赖仅 NumPy/SciPy，可选依赖按模块按需安装（pip install fat-forensics[all]）
- 由 Thales 与布里斯托大学合作研究协议产出，附 JOSS 论文与 ZENODO DOI

## 适用场景

- 研究者对数据集和预测模型做公平性与透明度探索分析
- 工程实践中监控已部署预测系统的 FAT 表现
- 用代理解释器（surrogate explainers）解释模型预测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L66: FAT Forensics (``fatf``) is a Python toolbox for evaluating fairness,
> L73: model *predictions*. We envisage two main use cases for the package, each
> L76: analysis and a *deployment mode* aimed at practitioners who may want to use it

## 星数曲线

```mermaid
xychart-beta
    title "fat-forensics/fat-forensics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-25 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9b4e5818c759` · [字段定义](../../DATASET.md)*
