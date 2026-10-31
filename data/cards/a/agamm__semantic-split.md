# agamm/semantic-split

⭐ 110 · Python · 推送 2026-06-29 · [GitHub](https://github.com/agamm/semantic-split) · 个人维护

**按语义相似度对文本分块的 Python 库，用于 LLM/向量库预处理**

提供基于语义相似度的句子分组与分块能力，将语义相近的句子聚合为 chunk，用于给 LLM 提示词或向量数据库做预处理。机制上依赖 SentenceTransformers 计算相似度、spaCy 做句子切分，含 SimilarSentenceSplitter 等接口。安装需先下载 spaCy 英文模型，再 pip 安装；带 GPU 时可装 torch CUDA 版，无 GPU 提供 CPU 版 torch 安装方式。限制：README 自述部分功能依赖 CUDA，测试通过 poetry 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SentenceTransformers 与 spaCy 的语义相似度分块
- 提供 SimilarSentenceSplitter / SentenceTransformersSimilarity 等接口
- 输出语义分组的 chunk 列表，供向量库或提示词使用

## 适用场景

- 为向量数据库入库前的文本做语义分块预处理
- 缩短并聚焦 LLM 提示词，控制 token 用量
- 检索问答场景中把相关句子聚成 chunk 以提升召回质量

## 场景标签

 · 领域:NLP/LLM 数据预处理

## 证据(README 行号)

> L5: A Python library to chunk/group your text based on semantic similarity - ideal for pre-processing data for Language 
> L22: 1. We want to pre-process the article - so each query is fast (point B). So we split it into semantic chunks using 

## 星数曲线

```mermaid
xychart-beta
    title "agamm/semantic-split 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-31 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0249de558d42` · [字段定义](../../DATASET.md)*
