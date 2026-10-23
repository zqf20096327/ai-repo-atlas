# feyninc/chonkie

⭐ 4,801 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/feyninc/chonkie) · [官网](https://docs.chonkie.ai) · 组织维护

**面向 RAG 流水线的轻量文本分块（chunking）库**

Chonkie 是一个 Python 文本分块库，用于 RAG 应用的数据摄取环节：提供 10+ 种分块器（token、句子、递归、语义、神经、LLM 驱动的 SlumberChunker、代码、表格等），并围绕分块组织了完整管线组件——Chefs/Fetchers 做预处理与数据加载、Refineries 加重叠与嵌入、Porters 导出 JSON/HuggingFace datasets、Handshakes 将分块直接写入 10+ 向量数据库（Chroma、Qdrant、Milvus 等）。支持 16+ 嵌入提供方与 5+ LLM 提供方，遵循最小安装原则按需安装可选依赖，也可通过 Docker 以自托管 REST API 形式运行。开箱支持 56 种语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10+ 种分块器，含 SIMD 加速的 FastChunker（宣称 100+ GB/s）与 LLM 驱动的 SlumberChunker
- 45+ 集成：嵌入提供方、LLM、向量化数据库（Chroma/Qdrant/Milvus 等）
- Pipeline 组件化串联预处理、分块、精炼与导出
- 可经 Docker 以自托管 REST API 运行，管线配置存于本地 SQLite

## 适用场景

- 为 RAG 系统在入库前做文本分块与嵌入
- 把分块结果直接写入 Chroma/Qdrant/Milvus 等向量库
- 以 REST API 形式向任意应用提供分块服务

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L14: _The lightweight ingestion library for fast, efficient and robust RAG pipelines_
> L25: **🔄 End-to-end**: Fetch, CHONK, refine, embed and ship straight to your vector DB!
> L127: Chonkie provides several chunkers to help you split your text efficiently for RAG applications. Here's a quick ove

## 星数曲线

```mermaid
xychart-beta
    title "feyninc/chonkie 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 4791 --> 4802
    line [4792, 4797, 4801]
```

2026-10-18 4,792 → 2026-10-23 4,801（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 mid · 依据 README sha `db43423db690` · [字段定义](../../DATASET.md)*
