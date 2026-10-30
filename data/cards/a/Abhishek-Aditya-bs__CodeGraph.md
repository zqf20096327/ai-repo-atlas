# Abhishek-Aditya-bs/CodeGraph

⭐ 22 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/Abhishek-Aditya-bs/CodeGraph) · [官网](https://codegraph-website.pages.dev) · 个人维护

**把任意代码库转为 Neo4j 知识图谱并用自然语言查询的 GraphRAG 工具**

将任意代码库（GitHub 仓库或本地文件夹）解析为存于 Neo4j 的知识图谱（类、函数、接口、文件等实体及关系），并在同一数据库中叠加 OpenAI text-embedding-3-large 的 3072 维向量索引，通过桥接层让一次自然语言查询同时执行图遍历与语义检索，再由 LLM 合成有出处的回答。面向开发者，以 Streamlit 界面运行完整六步工作流（输入、摄取、建图、索引、查询、管理），支持 Docker Compose 一键启动。运行需 OpenAI API key 与 Neo4j，嵌入模型与 LLM 模型可从配置切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识图谱与 3072 维向量索引共存于单一 Neo4j 数据库，桥接层连接结构层与语义层
- 自然语言查询先做向量检索、实体映射、图遍历，再由 LLM 合成带代码出处与相似度分数的回答
- Streamlit 界面运行完整流水线：输入校验、可配置分块、LLM 实体抽取、索引与数据库管理
- Docker Compose 一键启动应用与 Neo4j，镜像多阶段构建、非 root 运行并带健康检查

## 适用场景

- 用自然语言询问陌生代码库的架构与端到端流程
- 在大代码库中做语义+结构混合的代码检索
- 为代码理解与维护提供带结构上下文的问答

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3:  CodeGraph turns any codebase into a Neo4j knowledge graph of its files, classes, functions and interfaces —
> L27: CodeGraph keeps both and bridges them. It builds a **knowledge graph** of typed code entities and a
> L82: 4. **LLM synthesis** — combine semantic matches and structural context into a grounded prompt and generate a conver

## 星数曲线

```mermaid
xychart-beta
    title "Abhishek-Aditya-bs/CodeGraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `99a9024292f0` · [字段定义](../../DATASET.md)*
