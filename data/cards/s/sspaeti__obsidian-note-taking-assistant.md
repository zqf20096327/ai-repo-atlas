# sspaeti/obsidian-note-taking-assistant

⭐ 68 · Python · 推送 2026-08-02 · [GitHub](https://github.com/sspaeti/obsidian-note-taking-assistant) · [官网](https://explore.ssp.sh) · 个人维护

**本地优先的 Obsidian 笔记 RAG 检索系统：语义+图谱查询**

面向 Obsidian 用户的本地知识检索工具，包含摄取管线 CLI 与 Web 应用。读取任意 Markdown 库存，用正则解析 wikilink 构建图，用 BGE-M3（1024 维）在本地生成嵌入存入 DuckDB（VSS 扩展、HNSW 索引），支持语义搜索、反向链接、N 跳图遍历、未链接的语义相似笔记发现（hidden connections）、超边标签共享与图增强搜索。全程本地运行，首次运行需下载约 1.8GB 模型，之后可完全离线。安装基于 uv 与 Python 3.11+。注意 README 中嵌入维度描述存在 1024 与 384/MiniLM 两种说法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DuckDB VSS 扩展 + HNSW 索引的本地向量检索
- 语义嵌入与 wikilink 图结合的 hidden connections 发现
- 100% 本地运行，笔记不上传，支持完全离线
- 同时提供摄取 CLI 与 Web 应用源码

## 适用场景

- 在私人 Obsidian 库中按语义含义而非关键词查找笔记
- 发现语义相关但尚未互相链接的笔记以补充知识网络
- 对日记、工作文档等敏感内容做本地检索而不上传云端

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Local-first knowledge retrieval system for Obsidian notes using DuckDB with vector search. Find accompanied blog.
> L18: - **Your notes never leave your machine**: Everything runs locally with DuckDB and `BAAI/bge-m3` embedding model.
> L106: Each note is split into chunks (~512 tokens), and each chunk is converted to a 384-dimensional vector using `all-M

## 星数曲线

```mermaid
xychart-beta
    title "sspaeti/obsidian-note-taking-assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-29 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b0053f1c7bfe` · [字段定义](../../DATASET.md)*
