# Augus1999/bayesian-flow-network-for-chemistry

⭐ 31 · Python · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/Augus1999/bayesian-flow-network-for-chemistry) · [官网](https://augus1999.github.io/bayesian-flow-network-for-chemistry/) · 组织维护

**面向化学任务的贝叶斯流网络模型库：分子/蛋白质生成与性质预测**

ChemBFN 的 PyTorch 实现仓库，以单一模型覆盖 SMILES/SELFIES 从头分子生成、蛋白质序列生成、模板优化（mol2mol）、无分类器引导的单/多目标条件生成与上下文补全（inpaint）生成，并支持分子性质/活性预测与反应产率预测的微调，可通过 ODE 求解器加速采样。内置 MLFF 可将生成的 SMILES 转为三维构象。以 Python 包 bayesianflow_for_chem 发布于 PyPI，提供预训练模型与 CSV 数据处理类 CSVData。由广岛大学团队开发，配套论文发表于 JCIM 与 J. Cheminform。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SMILES/SELFIES 从头分子生成与蛋白质序列生成
- 无分类器引导的单/多目标条件生成与 inpaint 补全
- 支持分子性质/活性预测与反应产率预测微调
- 内置 MLFF 将生成 SMILES 转为三维构象，ODE 求解器加速采样

## 适用场景

- 从头设计满足多目标性质的分子
- 基于模板做分子优化与片段补全
- 微调模型做分子性质或反应产率预测

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: This is the repository of the PyTorch implementation of ChemBFN model.
> L18: * SMILES or SELFIES-based *de novo* molecule generation
> L21: * Classifier-free guidance conditional generation (single or multi-objective optimisation)

## 星数曲线

```mermaid
xychart-beta
    title "Augus1999/bayesian-flow-network-for-chemistry 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ecc9dccda9aa` · [字段定义](../../DATASET.md)*
