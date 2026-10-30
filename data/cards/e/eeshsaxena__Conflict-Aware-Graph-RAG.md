# eeshsaxena/Conflict-Aware-Graph-RAG

⭐ 16 · Jupyter Notebook · 推送 2026-07-16 · [GitHub](https://github.com/eeshsaxena/Conflict-Aware-Graph-RAG) · 个人维护

**冲突感知的知识图谱 RAG 系统：检测时序矛盾并给出校准置信度**

基于 Neo4j 的知识图谱 RAG 系统，在 TruthfulRAG v4 基线上实现 9 项改进：从文档集合自动推断 schema 构建图谱，检测事实间的时序矛盾并用时间衰减评分（半衰期 8.66 年）解决；检索采用 BM25 与语义嵌入的 RRF 融合与基于熵的路径过滤；回答附带解释链与校准置信度（熵/支持度/时近度加权），支持声明验证（SUPPORTED/REFUTED/UNCERTAIN）。后端可选 Ollama、Groq、Google、Anthropic。附 Python 主管线、Web 演示（LangChain 与 v5 双聊天机器人对比）与 Docker 部署，面向科研与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 时间衰减评分与跨文档佐证解决时序矛盾事实
- BM25+语义嵌入 RRF 混合检索与熵基路径过滤
- 校准置信度（0.40×熵+0.30×支持+0.30×时近度）与解释链审计轨迹
- 声明验证输出 SUPPORTED/REFUTED/UNCERTAIN 判定
- 自适配熵采样跳过极值路径，约降 35% 延迟

## 适用场景

- 在含时间演化事实（如法规更替、医学指南更新）的语料上做可靠问答
- 对比普通 RAG 与冲突感知 RAG 的回答质量
- 验证声明是否被知识图谱证据支持

## 场景标签

`RAG` `知识图谱` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L5: A conflict-aware Knowledge-Graph RAG system implementing 9 novel improvements over the TruthfulRAG v4 baseline (arXi
> L37: LLM_PROVIDER=ollama          # ollama | groq | google | anthropic

## 星数曲线

```mermaid
xychart-beta
    title "eeshsaxena/Conflict-Aware-Graph-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e4936f88f39a` · [字段定义](../../DATASET.md)*
