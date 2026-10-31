# VectorInstitute/fed-rag

⭐ 150 · Python · Apache-2.0 · 推送 2026-06-22 · [GitHub](https://github.com/VectorInstitute/fed-rag) · [官网](https://vectorinstitute.github.io/fed-rag/) · 组织维护

**面向研究者的 RAG 系统微调框架，支持集中式与联邦式架构**

FedRAG 是由 Vector Institute 维护的开源框架，用于在集中式或联邦（federated）架构下微调检索增强生成（RAG）系统，覆盖多种 RAG 微调方法（如 RA-DIT）与自定义联邦聚合策略示例。框架提供轻量抽象层，并可与 HuggingFace、LlamaIndex、LangChain 集成。以 Python 包形式通过 pip 或 conda-forge 安装，也可从源码构建；提供官方文档站与示例目录，面向开展 RAG 与联邦学习研究的开发者与科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集中式与联邦式两种架构下的 RAG 微调
- 支持 RA-DIT 等微调方法与自定义联邦聚合策略
- 提供 HuggingFace / LlamaIndex / LangChain 集成
- pip 与 conda-forge 双通道安装，含 HuggingFace 等扩展包

## 适用场景

- 在联邦学习场景下微调 RAG 系统
- 复现或实现 RA-DIT 等 RAG 微调方法
- 在已有 HuggingFace / LangChain 工具链上接入 RAG 微调

## 场景标签

`RAG` `微调` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L13: FedRAG is an open-source framework for fine-tuning Retrieval-Augmented
> L14: Generation (RAG) systems across both centralized and federated architectures.
> L104: FedRAG is developed and maintained by the Vector Institute.

## 星数曲线

```mermaid
xychart-beta
    title "VectorInstitute/fed-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-31 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a62f4788f145` · [字段定义](../../DATASET.md)*
