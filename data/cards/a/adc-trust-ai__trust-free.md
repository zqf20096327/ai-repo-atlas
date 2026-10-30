# adc-trust-ai/trust-free

⭐ 16 · Jupyter Notebook · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/adc-trust-ai/trust-free) · [官网](https://adc-trust-ai.github.io/trust/) · 个人维护

**可解释线性模型树回归/分类库，附自动解释报告**

TRUST 算法的官方 Python 实现：基于稀疏线性模型树（叶节点拟合 Elastic Net 线性模型而非常数），支持回归、多类分类与实验性时间序列任务。内置 explain()/compare()/importance() 等方法自动生成自然语言解释报告、树图（需 Graphviz）、多种变量重要性（Permutation、Ghost Variables、ALE、SHAP）。含独立工具 TurboSolve（OLS 求解器）与合成数据生成器。免费版限制数据集 ≤5000 行、≤20 列，面向概念验证、研发与教学；基于作者 PRICAI 2025 论文，作者为威斯康星大学麦迪逊分校统计学博士研究生。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 线性模型树 + 叶节点稀疏线性模型的混合架构
- 自动生成自然语言解释报告与逐预测解释（explain/compare）
- 多种变量重要性方法（Permutation、Ghost Variables、ALE、SHAP）
- 免费版数据集限制 ≤5000 行、≤20 列，TurboSolve 与数据生成器无限制可用

## 适用场景

- 金融、医疗等需要可解释且可审计预测的场景
- 教学中演示线性模型树与变量重要性
- 研发阶段在中小数据集上做可解释回归/分类建模

## 场景标签

 · 领域:可解释机器学习

## 证据(README 行号)

> L15: **trust-free** is a Python package for fitting interpretable regression models using Transparent, Robust, and Ultra
> L45: TRUST [1] is a next-generation algorithm based on (sparse) **Linear Model Trees** (LMTs), which I developed as part

## 星数曲线

```mermaid
xychart-beta
    title "adc-trust-ai/trust-free 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0c006190ff36` · [字段定义](../../DATASET.md)*
