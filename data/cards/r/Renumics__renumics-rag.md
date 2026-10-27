# Renumics/renumics-rag

⭐ 211 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Renumics/renumics-rag) · 组织维护

**RAG 助手演示与数据可视化：回答问题并探索检索数据**

基于 LangChain 和 Streamlit 的检索增强生成助手演示：对 HTML 文档建索引后，可通过 CLI（retrieve/answer）或 Web 应用提问并获得带来源片段的回答。特色是用 Renumics Spotlight 对问题与文档片段做交互式探索，以相似度图（UMAP 降维嵌入）展示检索情况。支持 OpenAI/Azure OpenAI 或 Hugging Face 模型，嵌入模型、检索器与 LLM 可配置；当前仅支持索引 HTML 文件。提供 pip/uv 安装与可编辑模式本地开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- create-db 建索引后以 CLI 或 Web 应用问答，回答附可展开的来源片段
- Renumics Spotlight 交互式探索问题与文档片段，UMAP 相似度图可视化
- OpenAI/Azure OpenAI 与 Hugging Face 模型可切换，检索参数可在 GUI 调整
- 附 Formula One 维基百科演示数据集与 500+ 问题的评估示例

## 适用场景

- 用自有 HTML 文档搭建可问答的 RAG 演示
- 可视化分析 RAG 系统中哪些文档片段被检索命中
- 学习 RAG 数据的探索性分析与评估方法

## 场景标签

`RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Retrieval-augmented generation assistant demo using LangChain and Streamlit.
> L143: After submitting some questions, you can explore them using Renumics Spotlight by clicking the red explore button 

## 星数曲线

```mermaid
xychart-beta
    title "Renumics/renumics-rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 210 --> 213
    line [212, 211, 211]
```

2026-10-18 212 → 2026-10-27 211（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f4e1fe482656` · [字段定义](../../DATASET.md)*
