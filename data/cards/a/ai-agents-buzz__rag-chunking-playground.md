# ai-agents-buzz/rag-chunking-playground

⭐ 14 · HTML · MIT · 推送 2026-03-26 · [GitHub](https://github.com/ai-agents-buzz/rag-chunking-playground) · [官网](https://aiagentsbuzz.com/tools/rag-chunking-playground/) · 组织维护

**对比 6 种 RAG 分块策略的可视化工具，带质量评分与成本估算**

纯客户端网页工具：粘贴或加载文档后，用 Fixed/Recursive/Sentence/Markdown/Regex 五种策略（Semantic 标注 coming soon）并行分块，以绿/黄/红三色对分块质量打分，悬停高亮原文位置，BM25 检索测试，并按 OpenAI/Cohere 单价估算嵌入与上下文成本；可导出 LangChain/LlamaIndex/Haystack 代码片段。除 Semantic 计划调用 OpenAI API 外全部在浏览器本地运行，git clone 后直接打开 index.html 即可使用，无构建步骤与依赖。由 AI Agents Buzz（媒体站点）维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 种分块策略并排对比，含质量评分（绿/黄/红）
- 悬停分块在原文中高亮，BM25 查询检索测试
- OpenAI/Cohere 嵌入与上下文成本估算
- 导出 LangChain/LlamaIndex/Haystack 代码片段

## 适用场景

- 调试自己 RAG 系统返回质量差时分块是否断裂
- 在真实文档上选型分块策略并估算成本
- 教学/学习 RAG 分块基础概念

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: > Compare 6 chunking strategies side-by-side — and actually *see* why chunking matters.
> L36: ✅ **Export code:** LangChain, LlamaIndex, Haystack snippets
> L80: Test which chunks get retrieved for a sample query using BM25 ranking

## 星数曲线

```mermaid
xychart-beta
    title "ai-agents-buzz/rag-chunking-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1f151495cd0a` · [字段定义](../../DATASET.md)*
