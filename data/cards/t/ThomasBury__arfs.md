# ThomasBury/arfs

⭐ 145 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/ThomasBury/arfs) · 个人维护

**Python 全相关特征选择库：Leshy/BoostAGroota/GrootCV 三算法**

实现基于 shadow features 的全相关特征选择：Leshy（改自 Boruta）、BoostAGroota（改自 BoostARoota）与 GrootCV（基于 LightGBM 重复折交叉验证与 SHAP 重要性）。三者提供 sklearn 风格 fit/transform 接口，Leshy 与 BoostAGroota 可接受兼容的树估计器，支持 native/SHAP/置换三种重要性。另含缺失、基数、共线性预处理与 MRmr 排序、Lasso 选择、TreeGrouper/TreeDiscretizer 有监督分箱。README 明确说明比较不构成校准的错误发现率控制；存在破坏性 API 变更需重拟合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Leshy/BoostAGroota/GrootCV 三种全相关特征选择算法
- sklearn 风格 fit/transform 接口，支持自定义树估计器与样本权重
- 提供 native、SHAP、置换三种特征重要性方法
- 附带缺失/基数/共线性预处理与 MRmr、Lasso 选择、有监督分箱

## 适用场景

- 建模前筛选携带目标信息的全部特征（含冗余特征）
- 处理类别特征与高基数特征的重要性评估
- 在不平衡分类任务中做特征选择（可传 class_weight）

## 场景标签

 · 领域:机器学习/特征工程

## 证据(README 行号)

> L13: This package implements Leshy (based on Boruta), BoostAGroota (based on BoostARoota) and GrootCV. They expose sklea
> L21: `$ pip install arfs`

## 星数曲线

```mermaid
xychart-beta
    title "ThomasBury/arfs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-25 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `da4ebc84325e` · [字段定义](../../DATASET.md)*
