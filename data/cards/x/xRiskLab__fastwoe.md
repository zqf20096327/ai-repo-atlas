# xRiskLab/fastwoe

⭐ 24 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/xRiskLab/fastwoe) · 组织维护

**分类任务中类别特征的 WOE 编码与统计推断 Python 库**

面向机器学习从业者的 Python 库，基于 scikit-learn TargetEncoder 实现类别特征的 Weight of Evidence 编码，覆盖二分类与多分类（one-vs-rest）。提供 WOE 值的标准误与置信区间、信息值（IV）的 delta 方法标准误与卡方显著性检验、单调性约束、决策树与 FAISS KMeans 数值分箱、特殊编码值处理及 Good 链式法则条件 WOE。遵循 scikit-learn 预处理 transformer 接口，通过 pip 安装，需 Python 3.9+ 与 scikit-learn 1.3.0+，FAISS 与 Matplotlib 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 scikit-learn TargetEncoder 的 WOE 编码，支持多分类 one-vs-rest
- WOE 标准误、置信区间与 IV 的显著性检验
- 单调性约束、高基数控制与决策树/FAISS KMeans 数值分箱
- Good 链式法则条件 WOE（计数式与层次 softmax 式）

## 适用场景

- 信用评分卡建模中对类别特征做可解释编码
- 为逻辑回归模型生成 WOE 特征并评估 IV 显著性
- 处理含特殊编码值（如 -999）与缺失值的特征分箱

## 场景标签

 · 领域:机器学习/计算统计

## 证据(README 行号)

> L11: FastWoe is a Python library for efficient **Weight of Evidence (WOE)** encoding of categorical features and statist
> L17: - **Fast WOE Encoding**: Leverages scikit-learn's `TargetEncoder` for efficient computation
> L26: - **Compatible with scikit-learn**: Follows scikit-learn's preprocessing transformer interface

## 星数曲线

```mermaid
xychart-beta
    title "xRiskLab/fastwoe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `432a4a93b73a` · [字段定义](../../DATASET.md)*
