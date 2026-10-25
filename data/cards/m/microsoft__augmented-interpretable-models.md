# microsoft/augmented-interpretable-models

⭐ 42 · Jupyter Notebook · MIT · 推送 2025-11-10 · [GitHub](https://github.com/microsoft/augmented-interpretable-models) · [官网](https://www.nature.com/articles/s41467-023-43713-1) · 组织维护

**论文配套代码：训练时用 LLM 增强可解释线性/树模型**

Aug-imodels 论文（Nature Communications, 2023）的实验复现代码库。方法是在训练阶段利用预训练语言模型增强可解释模型（AugLinearClassifier/AugTreeClassifier 及回归版本），产出的预测器保持线性或树结构、scikit-learn 兼容。日常使用建议通过 imodelsX 库（pip install imodelsx）获得简单接口；本仓库面向复现论文实验的科研用户，README 仅含 quickstart 示例与参考文献。

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

- 训练时以预训练语言模型增强可解释线性/树模型
- 提供 AugLinear/AugTree 分类与回归四类估计器
- 与 scikit-learn 接口兼容

## 适用场景

- 复现 Aug-imodels 论文实验
- 在需要可解释性的预测任务中采用线性/树结构模型
- 通过 imodelsX 库快速试用 Aug 系列估计器

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: Augmenting Interpretable Models with LLMs during Training
> L3: This repo contains code to reproduce the experiments in the Aug-imodels paper (Nature Communications, 2023). For a s

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/augmented-interpretable-models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `eb7c55732c12` · [字段定义](../../DATASET.md)*
