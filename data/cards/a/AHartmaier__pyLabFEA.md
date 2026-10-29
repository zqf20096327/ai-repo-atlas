# AHartmaier/pyLabFEA

⭐ 70 · Jupyter Notebook · GPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/AHartmaier/pyLabFEA) · [官网](https://ahartmaier.github.io/pyLabFEA/) · 组织维护

**轻量级纯 Python 固体力学有限元分析教学与科研库**

面向教学与科研的纯 Python 有限元分析库，覆盖固体力学与弹塑性材料本构建模。支持基于模块化材料数据 schema 导入力学行为数据，训练机器学习屈服函数并用作弹塑性 FEA 的本构模型；训练的 ML 流动规则可以 UMAT 形式用于商业 FEA 软件 Abaqus。提供面向对象建模 API、Jupyter notebook 教程与 Python 示例脚本，依赖 NumPy、SciPy、scikit-learn、Matplotlib。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 轻量纯 Python 有限元求解器（固体力学、弹塑性材料）
- 训练机器学习屈服函数用作弹塑性 FEA 本构模型
- 按模块化材料数据 schema 导入力学行为数据
- ML 流动规则可作为 UMAT 用于 Abaqus

## 适用场景

- 教学场景中演示线性和非线性有限元分析
- 基于材料数据训练 ML 屈服函数并用于本构建模
- 将 ML 本构模型以 UMAT 接入 Abaqus 仿真流程

## 场景标签

`科研工具` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L16: introduces a lightweight pure-python version of FEA for solid mechanics and elastic-plastic materials. pyLabFEA can
> L24: - Flexible methods for material definitions, from conventional continuum elasticity and plasticity methods to train

## 星数曲线

```mermaid
xychart-beta
    title "AHartmaier/pyLabFEA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 68 --> 71
    line [69, 70, 70]
```

2026-10-18 69 → 2026-10-29 70（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ddacdaf64e4c` · [字段定义](../../DATASET.md)*
