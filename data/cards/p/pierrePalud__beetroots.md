# pierrePalud/beetroots

⭐ 13 · Python · MIT · 推送 2026-07-23 · [GitHub](https://github.com/pierrePalud/beetroots) · [官网](https://beetroots.readthedocs.io/en/latest/) · 个人维护

**对多谱线观测图做贝叶斯反演的 Python 科研包**

面向星际介质等天文物理研究的 Python 包：通过专用采样算法（Palud et al., 2023, IEEE TSP）对多谱线结构化立方数据进行贝叶斯推断，输出物理参数估计图与可信区间图；同时附带贝叶斯模型适配性检验以评估反演有效性。针对复杂正向模型，配合 nnbma 包用神经网络近似替代数值模拟，加速求值并支持求导。包已应用于星际介质物理条件推断，可经 pip 或源码（poetry）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 非对数凹后验分布的高效采样算法（混合噪声）
- 输出参数估计图与可信区间图
- 贝叶斯模型适配性检验评估推断结果有效性
- 经 nnbma 用神经网络近似复杂正向模型

## 适用场景

- 从多谱线观测数据推断星际介质物理参数分布
- 科研中评估正向模型假设与推断结果的有效性
- 为复杂数值模拟正向模型构建神经网络近似以加速贝叶斯反演

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: Beetroots (BayEsian infErence with spaTial Regularization of nOisy multi-line ObservaTion mapS) is a Python package 
> L26: In the astrophysics applications presented in the documentation, the numerical simulation is replaced with a neural

## 星数曲线

```mermaid
xychart-beta
    title "pierrePalud/beetroots 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4abf8727a68b` · [字段定义](../../DATASET.md)*
