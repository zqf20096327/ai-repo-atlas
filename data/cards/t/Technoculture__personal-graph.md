# Technoculture/personal-graph

⭐ 105 · Jupyter Notebook · MIT · 推送 2026-02-23 · [GitHub](https://github.com/Technoculture/personal-graph) · 组织维护

**Python 知识图谱库：为 AI 应用构建工作与长期记忆**

基于 libsql（SQLite 引擎）的 Python 库，用于创建、管理、查询知识图谱，面向 LLM 的工作记忆与长期记忆场景。支持 Turso DB 实现每用户一库的私有图谱、经 Sqlite-vss 与 Instructor 的自然语言查询、Ollama 本地 LLM 与嵌入模型的本地执行，可导出数据到 Networkx 与 PyG 用于机器学习。示例覆盖对话记忆、按深度分数检索、检索问答（dspy 集成）等；DuckDB 支持与图神经网络算法（TransE、Query2Box）标注为 WIP。MIT 许可证，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 libsql/SQLite 的知识图谱存储与查询
- 支持 Ollama 本地 LLM 与嵌入模型的本地执行
- Turso DB 每用户一库的私有图谱
- 可导出 Networkx / PyG 供机器学习使用

## 适用场景

- 为 LLM 应用构建工作记忆，检索上下文回答问题
- 按对话深度等条件检索构建长期记忆
- 本地离线运行知识图谱问答流程

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: Personal-Graph is a Python library for creating, managing, and querying knowledge graphs. It aims to help solve work
> L13: - ✅ Supports local execution with Ollama LLMs and Embedding Models

## 星数曲线

```mermaid
xychart-beta
    title "Technoculture/personal-graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-30 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ad86932f9309` · [字段定义](../../DATASET.md)*
