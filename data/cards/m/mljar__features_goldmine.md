# mljar/features_goldmine

⭐ 16 · Python · Apache-2.0 · 推送 2026-04-23 · [GitHub](https://github.com/mljar/features_goldmine) · [官网](https://mljar.com) · 组织维护

**表格数据自动特征工程库：生成并筛选候选特征**

面向表格机器学习工作流的 Python 包 features_goldmine：读取 pandas DataFrame 与目标列，用多种策略生成候选特征（LightGBM 树路径交互、PCA/ICA 投影、行组统计、多类分类编码、KNN 上下文偏差等），先剔除常数/重复等弱候选，再训练多个小型 LightGBM 模型按重复特征重要性筛选并剪枝，输出仅含选定特征的 DataFrame。提供 fit/transform/save/load API，selectivity 三档与策略开关可调。README 同时给出 51 数据集上 52.9% 胜率的基线对比结果，说明效果依数据而定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十余种候选特征生成策略（树路径交互、PCA/ICA 投影、分类编码、KNN 上下文偏差等）
- 多 LightGBM 模型重复特征重要性筛选与冗余剪枝
- fit/transform/save/load API 与 selectivity 三档可调
- leak-safe out-of-fold 目标编码

## 适用场景

- 在既有 train/test 流水线上一行代码生成新特征并重训模型
- 快速验证工程特征是否提升当前 ML 流水线
- 回归/分类表格任务中自动探索特征交互与类别编码

## 场景标签

 · 领域:机器学习/特征工程

## 证据(README 行号)

> L7: We would like to introduce `features_goldmine`, a Python package built exactly for that problem. It runs multiple fe
> L100: First, the package generates many candidate features using several strategies. Some strategies look for interactio
> L104: Finally, it trains several small LightGBM models and lets the candidates compete against the raw features. Candida

## 星数曲线

```mermaid
xychart-beta
    title "mljar/features_goldmine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `28354bfb4682` · [字段定义](../../DATASET.md)*
