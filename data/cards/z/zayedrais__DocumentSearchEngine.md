# zayedrais/DocumentSearchEngine

⭐ 55 · Jupyter Notebook · 推送 2026-09-01 · [GitHub](https://github.com/zayedrais/DocumentSearchEngine) · 个人维护

**基于 TF-IDF 与 Google USE 的语义文档搜索引擎示例项目**

以 20newsgroup 数据集（约 1.1 万篇文档）为数据源的语义文档检索代码项目，README 以教程形式逐步展示：数据清洗与预处理（小写化、分词、去停用词、词形还原），再用两种方法构建检索——TF-IDF 向量化配合余弦相似度排序，以及 TensorFlow Hub 上的 Google Universal Sentence Encoder（DAN 版，输出 512 维向量）做语义检索。面向学习文本分析与语义检索的开发者，依赖 Python 3.5+、NLTK、Scikit-learn 与 TensorFlow-GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TF-IDF + 余弦相似度的文档检索实现
- 接入 Google Universal Sentence Encoder（DAN 版，512 维向量）的语义检索路径
- 覆盖从清洗、分词、去停用词到词形还原的完整预处理流程
- 以 20newsgroup（约 11K 文档）为演示数据集

## 适用场景

- 学习 TF-IDF 与词向量两种文本检索方法的实现
- 参考新闻组类文档的清洗与词形还原预处理代码
- 了解 USE 模型在语义相似度检索中的应用方式

## 场景标签

`语义搜索` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L1: In this post, we will be building a semantic documents search engine by using 20newsgroup open-source dataset.
> L51:  2.Document search engine with Google Universal sentence encoder

## 星数曲线

```mermaid
xychart-beta
    title "zayedrais/DocumentSearchEngine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-30 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `7f53720f0fb7` · [字段定义](../../DATASET.md)*
