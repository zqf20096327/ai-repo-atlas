# RaguTeam/RAGU

⭐ 138 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/RaguTeam/RAGU) · 组织维护 · 中文 README

**模块化 GraphRAG 框架：从文本构建知识图谱并多策略检索问答**

面向开发者的 Python GraphRAG 框架：将原始文本抽取为 NEREL 本体类型化的实体与关系（29 实体/49 关系类型），经 Leiden 社区检测聚合成知识图谱，并提供本地邻域、全局社区摘要、朴素向量 RAG、混合引擎四种检索策略及查询规划包装器（复杂问题分解为子查询逐级传递）。抽取管线含单步 LLM、两阶段 LLM 与基于 Qwen-3-0.6B 微调的 RAGU-lm（面向俄语）。全程异步，支持批量嵌入、限速重试缓存客户端与流式输出。提供 PyPI 安装与源码安装两种途径，附带俄英文档与论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种检索策略（local/global/naive/mixed）+ 查询规划包装器
- NEREL 本体类型化抽取（29 实体、49 关系类型）+ Leiden 社区聚类
- 三种抽取管线：单步 LLM、两阶段 LLM、RAGU-lm（Qwen-3-0.6B 微调）
- 异步设计：批量嵌入/向量查询、限速重试缓存客户端

## 适用场景

- 把文档语料构建成知识图谱后做图谱增强问答
- 对整个语料做宽泛主题性提问（全局社区摘要检索）
- 俄语文本的知识图谱抽取与问答（RAGU-lm 路径）
- 对比不同检索策略在同一语料上的效果

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L17: RAGU builds a knowledge graph from raw text and answers questions over it. It is
> L21: - **Retrieval that fits the question.** Local graph neighborhoods, global
> L89: RAGU ships four retrieval strategies plus a query-planning wrapper. Each engine

## 星数曲线

```mermaid
xychart-beta
    title "RaguTeam/RAGU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 137 --> 139
    line [138, 138]
```

2026-10-18 138 → 2026-10-24 138（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `257c62f89e68` · [字段定义](../../DATASET.md)*
