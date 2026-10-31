# JacksonBurns/astartes

⭐ 103 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/JacksonBurns/astartes) · [官网](https://jacksonburns.github.io/astartes/) · 个人维护

**sklearn 兼容的 ML 数据集算法化划分库**

提供 train_val_test_split 与 train_test_split 函数，作为 sklearn 对应函数的替换接口，将数据按随机或多种算法化采样方式（Kennard-Stone、Sphere Exclusion、DBSCAN 等，含插值与外推两类）划分为训练/验证/测试集，用于模型验证与评估内外推性能。面向化学信息学与一般数值数据的机器学习研究者；分子特征化通过可选的 molecules 子包（aimsim 后端）支持。支持 pip 与 conda-forge 安装，附 Colab 演示笔记本与 JOSS 论文。

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

- sklearn 兼容的 train_val_test_split / train_test_split 函数
- 多种理性划分算法（Kennard-Stone、Sphere Exclusion、DBSCAN 聚类等），分插值/外推两类
- 可选分子特征化（astartes[molecules]，基于 aimsim）
- generate_regression_results_dict 快速比较不同划分对 sklearn 兼容模型性能的影响

## 适用场景

- 替换 sklearn 的 train_test_split 做更严格的训练/验证/测试三划分
- 化学信息学中按分子相似性做插值或外推式数据划分
- 比较不同采样算法对回归模型性能的影响
- 直接调用 Kennard-Stone 等采样器获取样本索引

## 场景标签

 · 领域:机器学习/化学信息学

## 证据(README 行号)

> L61: `astartes` addresses both of these points by implementing an `sklearn`-compatible `train_val_test_split` function.
> L66: `astartes` is generally applicable to machine learning involving both discovery and inference _and_ model validatio
> L78: By default, `astartes` will split data randomly. Additionally, a variety of algorithmic sampling approaches can be 

## 星数曲线

```mermaid
xychart-beta
    title "JacksonBurns/astartes 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-28 103 → 2026-10-31 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3da76e27f1a1` · [字段定义](../../DATASET.md)*
