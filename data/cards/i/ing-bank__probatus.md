# ing-bank/probatus

⭐ 154 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/ing-bank/probatus) · [官网](https://ing-bank.github.io/probatus) · 组织维护

**验证回归与分类模型及其训练数据的 Python 工具库**

ING 银行维护的 Python 包，面向回归、二分类与多分类模型的验证与解释：interpret 模块提供基于 SHAP 的模型解释工具；sample_similarity 通过相似性建模比较两个数据集（如训练集与 out-of-time 测试集）；ShapRFECV 提供基于 SHAP 特征重要性的交叉验证递归特征消除。支持 Python 3.10–3.13，通过 pip 安装，文档托管在 GitHub Pages。

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

- 基于 SHAP 的模型解释工具（probatus.interpret）
- 两数据集相似性建模比较（probatus.sample_similarity）
- 基于 SHAP 特征重要性的交叉验证递归特征消除（ShapRFECV）

## 适用场景

- 为线性/树模型做 SHAP 解释与特征重要性分析
- 比较训练集与 out-of-time 测试集的分布相似性
- 对二分类/多分类/回归任务做递归特征消除

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **Probatus** is a python package that helps validate regression & (multiclass) classification models and the data u
> L13: - probatus.interpret provides shap-based model interpretation tools
> L15: - probatus.feature_elimination.ShapRFECV provides cross-validated Recursive Feature Elimination using shap feature 

## 星数曲线

```mermaid
xychart-beta
    title "ing-bank/probatus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 153 --> 155
    line [154, 154]
```

2026-10-18 154 → 2026-10-22 154（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `88297c6701ce` · [字段定义](../../DATASET.md)*
