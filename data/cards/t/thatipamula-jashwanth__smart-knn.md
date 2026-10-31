# thatipamula-jashwanth/smart-knn

⭐ 33 · Python · MIT · 推送 2026-03-11 · [GitHub](https://github.com/thatipamula-jashwanth/smart-knn) · [官网](https://thatipamula-jashwanth.github.io/SmartEco/) · 个人维护

**特征加权的 KNN 算法库：自动预处理并学习特征重要性**

SmartKNN 是基于最近邻的 Python 学习库，提供回归与分类能力。核心机制包括：通过 MSE 相关性、互信息或随机森林重要性估计特征权重，抑制噪声/弱信息维度，支持暴力搜索与近似最近邻（ANN）后端，可选 GPU 加速邻居搜索，采用 NumPy 向量化与 Numba 加速，暴露 scikit-learn 兼容 API。自动预处理覆盖归一化、NaN/Inf 处理与特征掩码。面向需要 KNN 类算法的数据科学与机器学习开发者，提供 Hugging Face 在线演示。

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

- 三种可配置的特征重要性估计方法（MSE 相关性/互信息/随机森林）
- 暴力搜索与近似最近邻（ANN）双后端，可选 GPU 加速
- scikit-learn 兼容 API，NumPy 向量化与 Numba 加速
- 自动预处理：归一化、NaN/Inf 处理、特征掩码

## 适用场景

- 在含噪声或弱信息特征的数据集上做回归或分类
- 需要特征加权最近邻且要与 scikit-learn 工作流集成
- 大规模数据集上用 ANN 后端做邻居搜索

## 场景标签

 · 领域:机器学习算法库

## 证据(README 行号)

> L35: **SmartKNN** is a nearest-neighbor–based learning method that belongs to the
> L51: The method supports both **regression** and **classification** tasks and

## 星数曲线

```mermaid
xychart-beta
    title "thatipamula-jashwanth/smart-knn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ef65784c11f3` · [字段定义](../../DATASET.md)*
