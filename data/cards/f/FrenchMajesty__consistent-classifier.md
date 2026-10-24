# FrenchMajesty/consistent-classifier

⭐ 63 · Go · MIT · 推送 2025-11-01 · [GitHub](https://github.com/FrenchMajesty/consistent-classifier) · 个人维护

**用 LLM 与向量聚类为大规模文本生成一致标签的 Go 库**

面向开发者的 Go package，对无约束标签集的大批量未标注文本做分类：文本经 Voyage AI 生成向量后在 Pinecone 向量库中查找相似已分类文本，命中即返回缓存标签，未命中则调用 OpenAI 兼容 LLM 分类，并用并查集（DSU）合并语义相近标签（如 technical_question 与 tech_support）以保证标签一致。组件（嵌入/向量库/LLM）均可替换，通过环境变量配置。包自身不实现速率限制，生产高并发需自行包装接口；10,000 条推文回复基准中缓存命中率超过 95%，LLM 调用减少 90% 以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量相似度缓存减少约 80-95% 冗余 LLM 调用
- 用并查集（DSU）自动合并语义相似标签，返回簇根标签保证一致性
- 嵌入（Voyage AI）/向量库（Pinecone）/LLM（OpenAI 兼容）适配器可插拔替换
- 线程安全、支持 context 与优雅关停，提供 Metrics（唯一标签数、命中率等）

## 适用场景

- 给大规模客服工单或推文回复自动打上一致的主题标签
- 在无预定义标签体系的数据上做开放式分类并自动收敛标签
- 需要降低 LLM 分类成本与延迟的批量标注流程

## 场景标签

 · 领域:文本分类/LLM 应用库

## 证据(README 行号)

> L6: A high-performance Go package for classifying large volumes of unlabeled text data using LLM-powered classification 
> L80: 4. **On Cache Miss**: Calls LLM for classification, then:

## 星数曲线

```mermaid
xychart-beta
    title "FrenchMajesty/consistent-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2b825369926a` · [字段定义](../../DATASET.md)*
