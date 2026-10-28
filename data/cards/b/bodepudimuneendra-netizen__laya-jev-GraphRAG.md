# bodepudimuneendra-netizen/laya-jev-GraphRAG

⭐ 51 · Python · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG) · 个人维护

**数据库无关的 Agentic GraphRAG 框架，可切换本地/云决策模型**

加在现有图数据库之上的 GraphRAG 框架：4 阶段流水线（Ingestion→Pre-Retrieval→Traversal→Post-Retrieval）在 Neo4j、Memgraph、Apache AGE、Kùzu 上以统一接口运行，通过环境变量切换。决策层不用逐跳 LLM 调用，而由可替换的 System One 模型（本地 Laya，421M，CUDA，约 1.2 GB VRAM / 云端 Jev API）以 Score/Noul/Choice 三个原语完成边校验、意图路由、A* 遍历与幻觉门控；生成式 LLM（Llama-3.1-8B）仅在末尾综合一次。Ablation 模式并行记录 Laya 与 Jev 决策生成 JSONL，可作 RLCD 训练数据微调 Laya。面向需要在自有图库上构建带评测的 RAG 能力的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 阶段流水线统一接口支持 Neo4j/Memgraph/Apache AGE/Kùzu，环境变量切换
- Score/Noul/Choice 三原语决策模型，模型与数据库双轴独立可换
- 自定义 A* 遍历与幻觉门控、引文校验
- Ablation 模式记录 Laya/Jev 双决策 JSONL，作为 RLCD 微调数据

## 适用场景

- 在已有 Neo4j/Memgraph 图数据库上叠加 GraphRAG 检索能力
- 本地 GPU 上运行零 API 依赖的私有 GraphRAG 引擎
- 收集本地与云模型决策对照数据用于微调本地模型

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: **laya-jev-GraphRAG** is a **graph-database-agnostic Agentic GraphRAG framework** — a production-ready intelligence 
> L35: This framework solves all three — replacing LLM routing with System One models, actively verifying every edge durin
> L44: The generative LLM (Llama-3.1-8B) only runs **once**, at the very end, to synthesise the already-verified subgraph 

## 星数曲线

```mermaid
xychart-beta
    title "bodepudimuneendra-netizen/laya-jev-GraphRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0d86e40ece47` · [字段定义](../../DATASET.md)*
