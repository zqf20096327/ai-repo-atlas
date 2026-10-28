# centre-for-humanities-computing/tweetopic

⭐ 37 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/centre-for-humanities-computing/tweetopic) · [官网](https://centre-for-humanities-computing.github.io/tweetopic/) · 组织维护

**面向短文本的 Python 主题建模库（DMM/GSDMM）**

Python 实现的 Dirichlet 多项式混合（DMM，即 GSDMM）主题建模库，针对推文等短文本进行主题聚类，支持 Gibbs 采样推理，并与 scikit-learn 兼容（可用于 Pipeline、与 CountVectorizer 组合）。0.4.0 起支持 random_state 以获得可复现结果，可对文本流进行拟合。从 PyPI 安装，另推荐配套可视化工具 topicwizard 检查主题结构。参考文献为 Yin & Wang 2014 的短文本聚类方法。

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

- DMM/GSDMM 短文本主题建模实现
- 完整 scikit-learn 兼容（Pipeline、CountVectorizer 组合）
- 支持 random_state 可复现结果与流式拟合
- 可搭配 topicwizard 进行主题可视化

## 适用场景

- 对推文等短文本语料做主题聚类
- 在 scikit-learn 流水线中嵌入主题模型
- 可视化检查主题结构与词-文档关系

## 场景标签

 · 领域:NLP/机器学习

## 证据(README 行号)

> L3: :zap: Blazing Fast topic modelling over short texts in Python
> L41: from tweetopic import DMM

## 星数曲线

```mermaid
xychart-beta
    title "centre-for-humanities-computing/tweetopic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f5e09d5882f` · [字段定义](../../DATASET.md)*
