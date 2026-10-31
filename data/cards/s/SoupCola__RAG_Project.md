# SoupCola/RAG_Project

⭐ 16 · Jupyter Notebook · 推送 2025-11-25 · [GitHub](https://github.com/SoupCola/RAG_Project) · 个人维护 · 中文 README

**全本地化部署的 RAG 系统分步教程（6 个 Notebook）**

以 Jupyter Notebook 形式组织的 RAG（检索增强生成）系统教程，面向希望学习构建和优化 RAG 系统的开发者。内容从基础问答系统（文档加载、文本分割、Chroma 向量库）进阶到查询优化、多数据源路由、高级索引与检索、交叉编码器重排序与混合检索，最后覆盖 Embedding 微调（BCE 模型转换、本地 Qwen 生成领域问答对、微调评估）。所有模型本地化部署，README 说明可在 3090 显卡上运行。通过 pip 安装依赖后按顺序运行各笔记本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个进阶 Notebook 覆盖 RAG 基础到 Embedding 微调
- 所有模型本地化部署，无云端依赖要求（README 声明 3090 可运行）
- 包含 BCE 嵌入模型微调与本地 Qwen 生成领域问答对的流程

## 适用场景

- 我想系统学习 RAG 系统从构建到优化的完整流程
- 我想学习如何针对特定领域微调 Embedding 模型
- 我想在本地 GPU 环境实践检索、重排序与混合检索技术

## 场景标签

`RAG` `教程课程` `微调` · 领域:知识与检索

## 证据(README 行号)

> L3: 本项目是一个完整的RAG系统教程，涵盖了从基础概念到高级技术的全面内容。通过Jupyter Notebook的形式，逐步讲解如何构建和优化一个高效的检索增强生成系统。本项目使用的所有模型都是本地化部署的，在3090上可以运行。
> L16: ### 01 - 本地问答系统 (Local QA System)

## 星数曲线

```mermaid
xychart-beta
    title "SoupCola/RAG_Project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `27d902e4f133` · [字段定义](../../DATASET.md)*
