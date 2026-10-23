# explosion/sense2vec

⭐ 1,681 · Python · MIT · 推送 2026-03-27 · [GitHub](https://github.com/explosion/sense2vec) · [官网](https://explosion.ai/blog/sense2vec-reloaded) · 组织维护

**上下文键控词向量库：加载、查询与训练 sense2vec 模型**

sense2vec（Trask et al., 2015）的 Python 实现，提供按词性标签与实体标签区分的多词短语向量，支持作为 spaCy v3 pipeline 组件使用或独立调用，可查询向量、频率与最相似短语，并通过 fastText 基于 GloVe/Word2Vec 训练自有向量。附 2015/2019 Reddit 评论预训练向量（573MB/4GB）下载、Streamlit 交互演示及 Prodigy 标注配方。经 pip 安装，版本 2.0 面向 spaCy v3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按词性/实体标签区分语义的短语向量查询（most_similar 等 API）
- spaCy pipeline 组件，为 Token/Span/Doc 添加扩展属性与方法
- 可用预训练 spaCy 模型、原始文本与 GloVe/Word2Vec 训练自有向量
- 提供 Reddit 2015/2019 预训练向量与 Streamlit 交互演示

## 适用场景

- 在 spaCy 管线中查询区分语义的短语相似词
- 为规则式 NER 或标注引导生成相似短语列表（Prodigy 配方）
- 加载 Reddit 评论预训练向量做语义相似度探索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: sense2vec (Trask et. al, 2015) is a nice
> L5: more interesting and detailed word vectors. This library is a simple Python
> L24: - spaCy **pipeline component** and **extension attributes**.

## 星数曲线

```mermaid
xychart-beta
    title "explosion/sense2vec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 1680 --> 1682
    line [1681, 1681]
```

2026-10-18 1,681 → 2026-10-23 1,681（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5cb301f0915d` · [字段定义](../../DATASET.md)*
