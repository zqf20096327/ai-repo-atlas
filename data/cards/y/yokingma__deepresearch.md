# yokingma/deepresearch

⭐ 19 · TypeScript · Apache-2.0 · 推送 2025-11-25 · [GitHub](https://github.com/yokingma/deepresearch) · 个人维护 · 中文 README

**基于 LangGraph 的深度研究 Agent，自动迭代检索并生成带引用回答**

以 npm 包 deepsearcher 形式提供的 DeepResearch Agent：基于 LangGraph.js 构建研究流程，包含生成初始查询、调用搜索引擎适配器（SearcherFunction）或 RAG 检索、反思与知识缺口分析、迭代补充查询，最终由 LLM 汇总为带来源引用的回答。模型支持任意 OpenAI 接口兼容的 LLM，搜索引擎通过适配器接入。面向希望在 Node.js 应用中集成自动化深度检索能力的开发者。代码逻辑参考了 Google 的 Gemini LangGraph 项目。

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

- LangGraph 驱动的研究流程：查询生成→检索→反思→迭代精炼
- 支持任意 OpenAI 接口兼容模型与自定义搜索引擎适配器
- 支持 web 搜索引擎或 RAG 检索两种知识来源
- 通过 streamEvents() 流式输出节点事件

## 适用场景

- 在 Node.js 应用中集成自动化深度检索与带引用的回答生成
- 结合自有 RAG 知识库做多轮研究式问答
- 需要追踪研究过程各节点事件的自定义前端

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: DeepResearch Agent with LangGraph, using any LLM models, search engine, RAG retrieval.
> L8: A LangGraph-powered research agent that performs comprehensive web research through dynamic query generation, iterat
> L17: - 🧠 Deep Research Agent based on LangGraph

## 星数曲线

```mermaid
xychart-beta
    title "yokingma/deepresearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f07ab9567043` · [字段定义](../../DATASET.md)*
