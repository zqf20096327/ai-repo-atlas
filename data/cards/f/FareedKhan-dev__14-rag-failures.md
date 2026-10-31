# FareedKhan-dev/14-rag-failures

⭐ 34 · Jupyter Notebook · MIT · 推送 2025-12-04 · [GitHub](https://github.com/FareedKhan-dev/14-rag-failures) · [官网](https://medium.com/@fareedkhandev/solving-14-common-rag-failures-through-knowledge-graphs-7125a8837a17) · 个人维护

**14 个 Notebook 演示朴素 RAG 失败场景及知识图谱解法**

面向 RAG 开发者的实践教程库：包含 14 个自包含 Python Notebook，每个先模拟标准向量检索 RAG 在多跳推理、实体歧义、矛盾事实、否定查询、时序序列等场景的失败，再用 NetworkX 知识图谱方法（图遍历、边验证、中心性算法等）给出对照解法。技术栈使用 TinyLlama-1.1B 本地推理、LangChain 编排、FAISS 向量库、sentence-transformers 嵌入。通过 git clone 安装，可在 Google Colab 免费版运行，无需大型 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个 Notebook 各演示一种向量检索失败模式与图谱解法
- 使用 TinyLlama-1.1B 本地推理，可在 Colab 免费版运行
- LangChain + FAISS + NetworkX 技术栈，每个 Notebook 自包含

## 适用场景

- 学习标准 RAG 在推理与结构化查询场景的局限
- 了解 Graph RAG 的具体实现模式（图遍历、时序边、交集查询等）
- 作为知识图谱增强检索的入门教程与代码参考

## 场景标签

`知识图谱` `RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L8: **A practical cookbook demonstrating why Vector Search fails at reasoning and how Graph RAG solves it.**
> L19: This repository contains **14 Python Notebooks** that simulate specific edge cases where standard RAG fails. Each n
> L65: You can run any notebook directly. Each notebook is self-contained:

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/14-rag-failures 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `163f49a5b7f6` · [字段定义](../../DATASET.md)*
