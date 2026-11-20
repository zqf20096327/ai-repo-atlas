# qdrant/qdrant-markdown-indexer

⭐ 10 · Python · 推送 2026-06-10 · [GitHub](https://github.com/qdrant/qdrant-markdown-indexer) · 个人维护

**把 Markdown 文档经 OpenAI 嵌入索引到 Qdrant 的管道**

提供将 Markdown 文件批量索引到 Qdrant 向量数据库的简易管道：通过 .env 配置 Qdrant Cloud 主机、API key 与 OpenAI API key，用 Poetry 安装依赖，以 Python 模块命令运行，指定本地文档目录与 URL 前缀后生成嵌入并写入 Qdrant。README 未说明分块策略、检索界面或其他功能，面向需要自建文档向量索引的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Markdown 文件索引进 Qdrant 向量数据库
- 使用 OpenAI embeddings 生成向量
- Poetry 管理依赖，单命令运行索引管道

## 适用场景

- 为文档站构建向量检索索引
- 把本地 Markdown 知识库导入 Qdrant Cloud

## 场景标签

 · 领域:LLM 基础设施/向量检索

## 证据(README 行号)

> L1: # Index markdown files into Qdrant using OpenAI embeddings
> L22: python -m markdown_search.index --docs-dir '/path/to/docs' --url-prefix 'https://example.com/docs'

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-markdown-indexer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `3372121d16f3` · [字段定义](../../DATASET.md)*
