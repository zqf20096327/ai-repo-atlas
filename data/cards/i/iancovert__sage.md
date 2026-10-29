# iancovert/sage

⭐ 294 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/iancovert/sage) · 组织维护

**用 Shapley 值计算黑盒模型全局特征重要性的 Python 库**

SAGE（Shapley Additive Global importancE）是面向机器学习从业者的模型可解释性库：基于博弈论 Shapley 值量化每个特征对模型预测力的贡献，并刻画特征间交互。模型无关，自动转换 XGBoost、CatBoost、LightGBM、sklearn 与 PyTorch 模型，其他模型需封装为可调用函数。提供置信区间、收敛检测、分组特征、多种特征移除近似与四种 Shapley 值估计器（置换采样、KernelSAGE、迭代采样、符号估计），并可计算无标签场景的 Shapley Effects。配套论文发表于 NeurIPS 2020。

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

- 基于 Shapley 值的模型无关全局特征重要性估计
- 自动模型转换支持 XGBoost/CatBoost/LightGBM/sklearn/PyTorch
- 四种 Shapley 值估计器可选，附带置信区间与收敛检测
- 支持特征分组、多种缺失特征近似方式与 Shapley Effects 无标签解释

## 适用场景

- 解释训练好的模型中哪些特征最重要
- 模型监控中识别损害性能的特征
- 高维数据集上用特征分组加速收敛

## 场景标签

 · 领域:机器学习可解释性

## 证据(README 行号)

> L3: **SAGE (Shapley Additive Global importancE)** is a game-theoretic approach for understanding black-box machine learn
> L25: SAGE is model-agnostic, so you can use it with any kind of machine learning model (linear models, GBMs, neural netw

## 星数曲线

```mermaid
xychart-beta
    title "iancovert/sage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 293 --> 295
    line [294, 294]
```

2026-10-18 294 → 2026-10-29 294（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b6feb1e8776e` · [字段定义](../../DATASET.md)*
