# Srinivas26k/srvdb

⭐ 15 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/Srinivas26k/srvdb) · [官网](https://srinivas26k.github.io/srvdb/) · 个人维护

**嵌入式向量数据库：本地语义搜索、RAG 与 AI 记忆，无需服务器**

开源嵌入式向量数据库，以 Python 和 Rust 库形式提供：在应用进程内存储 embeddings 于本地磁盘，支持语义搜索、本地 RAG 与 AI agent 记忆，无需服务器、Docker 或网络连接。Rust 核心、SIMD 距离内核，提供 flat/HNSW/IVF/SQ8/PQ 索引模式；持久化语义保证 persist() 返回后数据可抵御崩溃与断电。线程安全，每次调用释放 GIL。Apache-2.0 许可。

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

- 进程内运行、完全离线，无服务器与网络依赖
- persist() 后的崩溃安全保证，含崩溃测试
- 六种索引模式：exact/HNSW/IVF/SQ8/PQ/auto，SQ8 与 PQ 可缩减 4×–32× 存储
- Python 与 Rust 双语言接口，无 Python 运行时依赖

## 适用场景

- 本地 LLM 上对私有文档做 RAG
- AI agent 跨重启的记忆存储（remember/recall/forget）
- 桌面、CLI、笔记应用的进程内语义搜索
- 离线或物理隔离环境中 CI 里跑 RAG 测试

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L23: **SrvDB** (spelled S-R-V-D-B) is an open-source **embedded vector database**
> L50: - **Local RAG** over private documents with a local LLM
> L91: from sentence_transformers import SentenceTransformer   # pip install sentence-transformers

## 星数曲线

```mermaid
xychart-beta
    title "Srinivas26k/srvdb 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-26 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e8a0cf10d827` · [字段定义](../../DATASET.md)*
