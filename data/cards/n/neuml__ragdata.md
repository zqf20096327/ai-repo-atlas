# neuml/ragdata

⭐ 31 · Python · Apache-2.0 · 推送 2026-04-20 · [GitHub](https://github.com/neuml/ragdata) · 个人维护

**为 RAG 构建知识库：生成 txtai 嵌入数据库的工具**

由 txtai 作者（neuml）维护的项目，为常见数据集（ArXiv、Wikipedia）构建 txtai embeddings 数据库，供检索增强生成（RAG）使用。提供各数据集的完整构建流程说明，以 Python 包形式通过 PyPI 或 GitHub 源码安装，支持 Python 3.10+，推荐使用虚拟环境。当前支持的数据集为 ArXiv 与 Wikipedia 两类。

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

- 为 ArXiv 与 Wikipedia 等常见数据集构建 txtai embeddings 数据库
- 每个数据集附完整构建说明
- pip 安装，支持 Python 3.10+

## 适用场景

- 为 RAG 应用准备 ArXiv/Wikipedia 知识库
- 生成可供 txtai 检索的嵌入数据库

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L16: `ragdata` builds knowledge bases for Retrieval Augmented Generation (RAG).
> L18: This project has processes to build txtai embeddings databases for common datasets.

## 星数曲线

```mermaid
xychart-beta
    title "neuml/ragdata 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dbd3c73df7cc` · [字段定义](../../DATASET.md)*
