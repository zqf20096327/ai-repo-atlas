# upgini/upgini

⭐ 358 · Python · BSD-3-Clause · 推送 2026-10-20 · [GitHub](https://github.com/upgini/upgini) · [官网](https://upgini.com) · 组织维护

**面向 ML 管道的外部数据特征搜索与增强库**

Upgini 是一个 Python 数据搜索与增强库：用户以带标签的训练数据集发起搜索，通过 date、phone、email/HEM、IP、国家、邮编等搜索键，从数百个公共、社区与商业外部数据源中查找并生成能提升模型准确率的相关特征；内部使用 LLM、GNN、RNN 做特征生成与搜索键补全。提供 Scikit-learn 兼容接口（FeaturesEnricher），支持二分类/多分类/回归/时序预测任务，可计算增强后的准确率提升与稳定性验证，部分数据源需要 API key。给 ML/AI 流水线开发者和数据科学竞赛参与者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从数百个外部数据源自动搜索相关特征并计算准确率提升
- 基于 LLM/GNN/RNN 的自动特征生成与搜索键补全
- 支持 239 国、最长 41 年历史的数据源与多源集成
- Scikit-learn 兼容接口，支持分类/回归/时序预测任务

## 适用场景

- 为我的监督学习模型寻找能提升准确率的外部特征
- Kaggle 竞赛中用现成外部特征加速特征工程
- 验证外部数据对模型准确率提升的稳定性（out-of-time 检验）

## 场景标签

 · 领域:数据科学/特征工程

## 证据(README 行号)

> L19: **Upgini** is an intelligent data search engine with a Python library that helps you find and add relevant features
> L27: ⭐️ Automated feature generation from the sources: feature generation with LLM‑based data augmentation, RNNs, and Gr

## 星数曲线

```mermaid
xychart-beta
    title "upgini/upgini 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 357 --> 359
    line [358, 358]
```

2026-10-18 358 → 2026-10-22 358（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `092054e7cbac` · [字段定义](../../DATASET.md)*
