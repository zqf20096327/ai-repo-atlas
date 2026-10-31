# mohsengh/SCFS

⭐ 14 · Python · 推送 2026-06-10 · [GitHub](https://github.com/mohsengh/SCFS) · 个人维护

**论文官方实现：无监督特征选择，联合子空间聚类与自适应相似度学习**

SCFS 是 2020 年发表于 Engineering Applications of Artificial Intelligence 的论文官方代码实现，面向科研用户。方法在统一优化框架中联合学习子空间表示、聚类结构、自适应相似度矩阵与 L2,1 正则化稀疏回归，按变换矩阵 W 行的 L2 范数对特征排序，实现无监督特征选择。论文在 9 个基准数据集（生物、人脸、语音、文本）上与 LS、UDFS、NDFS 等 10 种方法比较。README 未给出安装命令或运行说明，仓库声明供学术研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 联合优化框架：子空间学习+聚类分析+自适应相似度学习+稀疏回归
- 特征按变换矩阵 W 行的 L2 范数排序
- L2,1 正则化稀疏特征选择与收敛保证的优化算法
- 论文在 9 个基准数据集上与 10 种方法实验比较

## 适用场景

- 高维基因表达数据的特征选择
- 聚类前做无监督降维预处理
- 复现论文实验或基准对比

## 场景标签

 · 领域:机器学习/生物信息学

## 证据(README 行号)

> L6: Official implementation of the paper:
> L8: **Unsupervised Feature Selection Based on Adaptive Similarity Learning and Subspace Clustering**
> L43: The proposed SCFS framework jointly performs:

## 星数曲线

```mermaid
xychart-beta
    title "mohsengh/SCFS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `74a93451de32` · [字段定义](../../DATASET.md)*
