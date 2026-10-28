# schwabauerbriantomas-gif/m2m-vector-search

⭐ 23 · Python · AGPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/schwabauerbriantomas-gif/m2m-vector-search) · 个人维护

**带 GPU 加速与在线学习的向量搜索引擎（Python 库）**

以 pip 包提供的向量搜索引擎：每个向量表示为可学习的高斯 splat（μ/κ/α 三参数），支持基于用户反馈的 Hebbian 在线更新而无需重建索引，提供 HRM2 分层路由、能量模型不确定性量化、SOC 自动剪枝、BM25+向量混合检索（RRF 融合）与 FastAPI REST 接口。后端支持 CPU、NVIDIA CUDA 与 AMD Vulkan，含分布式 edge/cluster 模式，并内置 LangChain BaseRetriever 集成。README 自述为纯 Python/NumPy 单线程实现，原始 QPS 低于 FAISS/HNSW，定位在自适应记忆场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 高斯 splat 表示 + 基于反馈的在线学习（无需重建索引）
- CPU / NVIDIA CUDA / AMD Vulkan 多后端统一 API
- 混合 BM25+向量检索，RRF/加权/纯向量/纯关键词融合
- 原生 LangChain BaseRetriever 实现与 REST API（FastAPI）

## 适用场景

- 为 AI agent 构建可随反馈自适应的持久语义记忆
- 在资源受限设备上做本地向量相似度检索
- 需要带置信度评分的语义搜索与混合关键词检索

## 场景标签

`语义搜索` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L9:  Machine-to-Memory &mdash; A vector search engine with probabilistic Gaussian Splats,
> L64: - **Multi-GPU Backend** — CPU, NVIDIA CUDA, and AMD Vulkan through a single API. Backend selection is transparent.
> L66: - **LangChain Integration** — Native `BaseRetriever` implementation with full CRUD support.

## 星数曲线

```mermaid
xychart-beta
    title "schwabauerbriantomas-gif/m2m-vector-search 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [24, 23, 23]
```

2026-10-18 24 → 2026-10-28 23（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `941d6c454860` · [字段定义](../../DATASET.md)*
