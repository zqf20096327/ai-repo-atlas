# neo4j-partners/hands-on-lab-neo4j-and-amazon

⭐ 59 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/neo4j-partners/hands-on-lab-neo4j-and-amazon) · 组织维护

**面向数据科学家的 Neo4j 与 Amazon Bedrock GraphRAG 实操教程**

Neo4j 合作方维护的动手实验（Hands-On Lab）教程仓库，主题为使用 Neo4j、Amazon Bedrock 与 Model Context Protocol 构建 GraphRAG 与 agentic AI 应用。实验数据为 SEC 10-K 公司财报构建的预置知识图谱，覆盖三条路线：无代码的 Aura Agents、基于 neo4j-graphrag 库与 LangGraph 的 Python GraphRAG 开发（向量/VectorCypher/混合/Text2Cypher 检索策略），以及通过 REST API 与 MCP 的程序化集成。需要浏览器访问 AWS Console 与 Neo4j Aura Console，非可安装运行的产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置 SEC 10-K 知识图谱（公司/风险因素/财务指标等 7 类节点）
- 四种检索策略：向量、图增强、混合、Text2Cypher
- 无代码 Aura Agents 与 LangGraph/MCP 两条 Agent 开发路线
- Embedding 维度不匹配时重建向量索引的实操说明（OpenAI 1536 vs Titan 1024）

## 适用场景

- 学习 GraphRAG 检索模式的分步实操
- 在 AWS 上部署 Neo4j 知识图谱与 Bedrock 推理
- 通过 MCP 与 REST API 将 Aura Agents 接入应用

## 场景标签

`教程课程` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: In this hands-on lab, you'll learn about Neo4j, Amazon Bedrock, and the Model Context Protocol (MCP). The lab is des
> L13: You'll work with a real-world dataset of SEC 10-K company filings to learn fundamental GraphRAG patterns. We'll sta
> L28: To get started, follow the labs in the agenda below in order.

## 星数曲线

```mermaid
xychart-beta
    title "neo4j-partners/hands-on-lab-neo4j-and-amazon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-27 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f76af1250038` · [字段定义](../../DATASET.md)*
