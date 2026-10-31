# MysterionRise/adaptive-knowledge-graph

⭐ 18 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/MysterionRise/adaptive-knowledge-graph) · 个人维护

**本地优先的知识图谱 AI 导师：面向开放教材的带引用问答与自适应测验**

面向开放教科书（OpenStax 美国史、经济学）的本地优先 AI 导师原型：从教材抽取概念与关系到 Neo4j 知识图谱，检索前用 spaCy/YAKE 识别概念并做图扩展，OpenSearch 融合 BM25 与 BGE-M3 向量检索（RRF），Ollama 本地 LLM 生成带编号引用的回答；测验由 LLM 生成并用 BKT 贝叶斯模型更新逐概念掌握度。隐私模式 PRIVACY_LOCAL_ONLY=true 下数据仅本地。README 自称概念验证原型而非生产系统，需约 16 GB RAM 与多个 Docker 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 知识图谱扩展查询的 RAG 管线，回答带编号引用与来源
- BKT 贝叶斯知识追踪驱动的自适应测验难度与先修推荐
- 混合检索：OpenSearch BM25 + BGE-M3 kNN + RRF 融合 + 可选交叉编码重排
- 53 题金标集评测 KG 扩展与普通检索的对比

## 适用场景

- 在本地对教科书提问并获得带引用出处的回答
- 按自身掌握度生成自适应难度的测验并获先修知识点推荐
- 交互式浏览教材概念图谱与学习路径

## 场景标签

`知识图谱` `文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: A local-first AI tutor for open textbooks: knowledge-graph-enhanced retrieval
> L13: local LLM served by Ollama. It comes with two
> L58: - **Adaptive quizzes.** The LLM generates multiple-choice questions at a

## 星数曲线

```mermaid
xychart-beta
    title "MysterionRise/adaptive-knowledge-graph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `10f1bdc88f99` · [字段定义](../../DATASET.md)*
