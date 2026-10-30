# jeremiahbohr/literature-mapper

⭐ 16 · Python · MIT · 推送 2026-02-15 · [GitHub](https://github.com/jeremiahbohr/literature-mapper) · 个人维护

**把学术 PDF 转为知识图谱并做受限引用合成的分析库**

面向研究者的 Python 库：将文件夹内 PDF 解析为知识图谱，抽取带置信度的类型化声明（发现/方法/局限），节点间含 SUPPORTS/CONTRADICTS/EXTENDS 语义边；从 OpenAlex 拉取引文数据计算影响力，检测语料库中被引用却缺失的“幽灵”论文与作者，用线性回归做概念时序趋势分析。RAG 智能体仅基于用户语料库合成答案并给出完整引用溯源，默认使用 Gemini 生成与嵌入模型，需 GEMINI_API_KEY 与网络连接。面向 10–500 篇精选文献集合，提供 CLI、Python API 与 GEXF/Gephi 可视化导出。

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

- PDF→知识图谱：类型化声明节点与语义边（SUPPORTS/CONTRADICTS/EXTENDS）
- OpenAlex 引文富化与影响力指标
- 幽灵论文/作者检测：发现语料库中被引用却缺失的工作
- 受限合成 RAG：仅基于语料库作答，附完整引用溯源

## 适用场景

- 系统梳理某个领域的文献并构建可视化知识图谱
- 发现文献综述中遗漏的高被引论文与关键作者
- 在自有文献库上提出研究问题并获得带引用的合成回答

## 场景标签

`知识图谱` `科研工具` `文档解析` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: An AI-powered Python library for systematic analysis of academic literature.
> L7: Literature Mapper transforms a folder of PDFs into a structured, queryable Knowledge Graph. It extracts typed claims
> L19: |**Bounded Synthesis**|RAG agents that answer questions and validate hypotheses using only your corpus, with full c

## 星数曲线

```mermaid
xychart-beta
    title "jeremiahbohr/literature-mapper 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ecd70df6ad5c` · [字段定义](../../DATASET.md)*
