# mmschlk/shapiq

⭐ 790 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/mmschlk/shapiq) · [官网](https://shapiq.readthedocs.io) · 组织维护

**Python 库：计算任意阶 Shapley 交互以解释模型预测**

shapiq 是用于机器学习博弈论解释的 Python 包：提供任意阶 Shapley 交互近似、博弈论算法基准（shapiq_benchmark）与内置游戏集合（shapiq_games），并以 shapiq.Explainer 解释模型预测中的特征交互与协同效应。它扩展 shap 包的用法，支持以 SHAP 相同方式计算 Shapley 值，并提供网络图、Force Plot 等可视化，以及面向大规模特征的 ProxySPEX 近似器和 TabPFN 专用解释器。面向研究博弈论的学者与需要解释模型的终端用户。要求 Python 3.12+，NeurIPS 论文发表，MIT 许可。

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

- 任意阶 Shapley 交互近似与协同效应量化
- 兼容 SHAP 用法，index='SV' 即得 Shapley 值
- 内置基准测试与游戏集合 extras（shapiq[games]/[benchmark]）
- 提供 ProxySPEX 大规模特征近似器与 TabPFNExplainer

## 适用场景

- 解释我的模型预测中特征间的交互效应
- 以 SHAP 相同流程计算并扩展到交互值
- 对博弈论解释算法做基准测试
- 可视化特征归因与交互网络图

## 场景标签

 · 领域:可解释机器学习

## 证据(README 行号)

> L18: Shapley Interaction Quantification (`shapiq`) is a Python package for (1) approximating any-order Shapley interacti
> L45: You can explain your model with `shapiq.explainer` and visualize Shapley interactions with `shapiq.plot`.
> L62: If you are used to working with SHAP, you can also compute Shapley values with `shapiq` the same way:

## 星数曲线

```mermaid
xychart-beta
    title "mmschlk/shapiq 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 788 --> 791
    line [789, 790, 790]
```

2026-10-18 789 → 2026-10-22 790（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4fcb8613f209` · [字段定义](../../DATASET.md)*
