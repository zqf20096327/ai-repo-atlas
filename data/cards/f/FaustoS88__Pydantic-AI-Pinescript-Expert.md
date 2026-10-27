# FaustoS88/Pydantic-AI-Pinescript-Expert

⭐ 67 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/FaustoS88/Pydantic-AI-Pinescript-Expert) · 个人维护

**基于 Pydantic AI 的 Pine Script v6 专家 RAG 问答与代码生成 agent**

面向 TradingView Pine Script v6 使用者的 RAG 智能体：用爬虫抓取官方文档并存入 PostgreSQL+pgvector 向量库，通过混合检索（BM25+向量、MMR、重排序、Anthropic Contextual Retrieval）与 LLM 生成回答和自定义指标/策略代码。提供 Streamlit 网页界面（含持久会话历史）、命令行交互与单次查询三种方式，默认走 OpenAI，也可通过 OpenRouter 路由多模型（含 Anthropic、Google 预设）。运行需 Python 3.9+、PostgreSQL/pgvector 与 OpenAI API key，检索质量用 RAGAS 评测（Faithfulness 0.833）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全量 Pine Script v6 文档向量化与混合检索（BM25+向量、重排序、MMR）
- 生成自定义 TradingView 指标与策略代码
- Streamlit/CLI/单次查询三种交互方式，网页端保留会话历史
- 多 LLM 后端：默认 OpenAI，可经 OpenRouter 切换 Claude、Gemini 等预设

## 适用场景

- 用自然语言查询 Pine Script v6 文档与函数用法
- 让 AI 生成可运行的 TradingView 指标或策略代码
- 通过网页界面持续对话调试脚本编写问题

## 场景标签

`RAG` `文档问答` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: A Retrieval-Augmented Generation (RAG) AI Agent built with Pydantic AI that serves as an expert on Pine Script v6, T
> L13: - **Code Generation**: Creates custom indicators and strategies based on user requirements

## 星数曲线

```mermaid
xychart-beta
    title "FaustoS88/Pydantic-AI-Pinescript-Expert 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-27 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `057373f2f68e` · [字段定义](../../DATASET.md)*
