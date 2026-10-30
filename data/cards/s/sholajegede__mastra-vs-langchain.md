# sholajegede/mastra-vs-langchain

⭐ 18 · TypeScript · MIT · 推送 2026-06-06 · [GitHub](https://github.com/sholajegede/mastra-vs-langchain) · [官网](https://mastra-vs-langchain.vercel.app) · 个人维护

**并排复刻同一 AI agent 管线，实测对比 Mastra 与 LangChain**

用 TypeScript 在 Mastra 与 LangChain/LangGraph 中各实现同一条五步研究与综合 agent 管线，可任选主题并行运行并全量埋点：记录每步的 Tavily 查询与相关性、发往 Claude 的完整 prompt 与响应、token 数、耗时，并由 G-Eval critic 从三个维度给最终报告打分。提供 Next.js 实时仪表盘与 CLI，运行历史存入 Convex。README 附有框架机制对照表与实测数据（速度、token、质量）。面向评估选型 AI agent 框架的开发者，需自备 Anthropic 与 Tavily API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一五步管线在 Mastra 与 LangChain 双实现并行运行
- 每步全量埋点：prompt、响应、token、耗时与 G-Eval 三维度评分
- Next.js 实时仪表盘，历史运行存 Convex 并带分类过滤
- CLI 亦可单独运行任一管线

## 适用场景

- 对比评估 Mastra 与 LangChain 的 token 消耗与执行速度
- 研究两种框架在编排、循环与状态传递上的实现差异
- 以任意主题实时观察两条 agent 管线的执行过程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L22: The same five-step research and synthesis pipeline, built twice — once in Mastra, once in LangChain/LangGraph — run
> L24: Every step is fully instrumented: the Tavily search query and all five results with relevance scores, the exact pro
> L85: ## What the data shows

## 星数曲线

```mermaid
xychart-beta
    title "sholajegede/mastra-vs-langchain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `12c112b5c5d9` · [字段定义](../../DATASET.md)*
