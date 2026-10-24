# textvec/textvec

⭐ 197 · Python · MIT · 推送 2025-11-26 · [GitHub](https://github.com/textvec/textvec) · 组织维护

**监督文本向量化工具：面向文本分类的 TFIDF 替代方法集**

Python 库，实现 11 种经典监督式文本向量化方法（TfIcf、Tfor、Sif 等），接口与 scikit-learn 的 vectorizer 一致，可在现有流水线中以少量改动替换 TFIDF。README 提供多个数据集上 TFIDF 与各方法的准确率对比表，并附论文出处。兼容 Python 3.9+，通过 pip 或源码安装。文档仍在 TODO 状态，未完成。

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

- 实现 11 种监督式/经典文本向量化方法
- 接口与 scikit-learn vectorizer 一致
- 提供多数据集上与 TFIDF 的准确率对比表
- 各方法附论文出处（3 篇参考文献）

## 适用场景

- 文本分类任务中替换 TFIDF 尝试监督式加权方案
- 对比多种词频加权方法在自有数据集上的表现
- 用于特征选择或集成模型的特征构造

## 场景标签

 · 领域:NLP/文本挖掘

## 证据(README 行号)

> L4: Textvec is a text vectorization tool, with the aim to implement all the "classic" text vectorization NLP methods in 
> L54: ### Currently implemented methods:

## 星数曲线

```mermaid
xychart-beta
    title "textvec/textvec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-24 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `57dcbf5f4cb6` · [字段定义](../../DATASET.md)*
