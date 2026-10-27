# yankeexe/llm-rag-with-reranker-demo

⭐ 84 · Python · 推送 2025-12-08 · [GitHub](https://github.com/yankeexe/llm-rag-with-reranker-demo) · [官网](https://youtu.be/1y2TohQdNbo) · 个人维护

**演示 RAG 应用：Ollama + 交叉编码器重排的问答 Demo**

面向 YouTube 视频配套的演示型 LLM 应用：基于 LangChain 构建 RAG 流程，检索后用交叉编码器（Cross-Encoders）对检索结果重排，本地运行时依赖 Ollama，前端为 Streamlit。仓库提供 Makefile 命令完成虚拟环境创建、依赖安装与启动。要求 Python > 3.10 且 SQLite > 3.35；README 提到 ChromaDB 与 SQLite 版本不兼容时的解决方案，另附优化 RAG 的语义缓存（Semantic Cache）视频。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 流程中加入交叉编码器重排
- 配合 Ollama 本地运行 LLM
- Makefile 一键安装与运行（make setup / make run）

## 适用场景

- 运行 RAG + 重排的参考实现学习检索增强流程
- 观看配套视频了解 RAG 优化（语义缓存）

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Demo LLM app with RAG for the YouTube video.
> L5: 🚨 NOTE: **Requires `Python > 3.10` with `SQLite > 3.35`**
> L23: - Ollama

## 星数曲线

```mermaid
xychart-beta
    title "yankeexe/llm-rag-with-reranker-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-27 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `61ba95149138` · [字段定义](../../DATASET.md)*
