# ErickWendel/neo4j-ai-experiments

⭐ 80 · JavaScript · MIT · 推送 2026-01-08 · [GitHub](https://github.com/ErickWendel/neo4j-ai-experiments) · [官网](https://ewbr.cc/rag-ai-neo4j) · 个人维护

**视频教程源码：用本地模型将自然语言转为 Neo4j Cypher 查询**

配套视频教程的示例工程：集成 Neo4j 图数据库与本地 AI 模型（Ollama 运行 gemma:7b 与 deepseek-coder:6.7b），实现自然语言到 Cypher 查询的转换，并含向量检索与 RAG 示例。运行依赖 Ollama、Docker（Neo4j 容器）与 Node.js v22+，通过 npm 安装依赖、种子脚本初始化数据库，应用对重复查询做响应缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 Cypher 查询的示例实现
- Neo4j 向量检索与 RAG 示例
- 基于 Ollama 运行 gemma:7b 与 deepseek-coder:6.7b 本地模型
- Docker Compose 启动 Neo4j 并提供数据库种子脚本

## 适用场景

- 学习如何将 Neo4j 与本地 LLM 结合构建查询系统
- 参考 RAG 与向量检索在图数据库中的实现方式
- 跟随视频教程复现完整环境搭建流程

## 场景标签

`教程课程` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: This project integrates Neo4j with AI models to generate Cypher queries from natural language prompts. It utilizes l
> L7: This is the source code shown on my video tutorial, consider watching it first!

## 星数曲线

```mermaid
xychart-beta
    title "ErickWendel/neo4j-ai-experiments 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-25 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `87f784a8ffa9` · [字段定义](../../DATASET.md)*
