# Liu-rj/PolyG

⭐ 14 · Python · Apache-2.0 · 推送 2026-04-06 · [GitHub](https://github.com/Liu-rj/PolyG) · 组织维护

**论文配套仓库：自适应图遍历的 GraphRAG 方法与基准 PolyBench**

提供论文 PolyG 的实现与新建基准 PolyBench。PolyBench 基于三个真实知识图谱（学术、文学、电商）构建，含 1,200 道题、覆盖四类基本问题模式及嵌套类型。PolyG 将用户问题分类并分解为基本子问题序列，自适应生成 Cypher 查询（含自纠错机制）在 Neo4j 图数据库上检索上下文，聚合后交由 LLM 生成最终回答。安装需 Python 3.12 环境与 Neo4j 2025.03.0，数据集另发布于 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提出四类问题分类法并据此分解问题
- 自适应生成 Cypher 查询并带自纠错机制，运行于 Neo4j
- PolyBench 含 1,200 道题、3 个领域知识图谱、5 种问题模式
- 基准数据同步发布于 Hugging Face（Liu-rj/PolyBench）

## 适用场景

- 研究者评估 GraphRAG 方法在多样问题模式下的表现
- 在自有知识图谱上执行自适应图遍历式问答
- 获取覆盖学术/文学/电商领域的图问答基准数据

## 场景标签

`RAG` `知识图谱` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repo provides the PolyBench and PolyG implementation of the paper PolyG: Adaptive Graph Traversal for Diverse G
> L7: To better evaluate GraphRAG methods, we propose a complete four-class taxonomy to categorize the basic patterns of k
> L9: With the new benchmark, we find that different question patterns require distinct graph traversal strategies and con

## 星数曲线

```mermaid
xychart-beta
    title "Liu-rj/PolyG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `812b5f3b8e95` · [字段定义](../../DATASET.md)*
