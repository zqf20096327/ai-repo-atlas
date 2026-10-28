# AbhinavPabbaraju/nexus-deep-research-agent

⭐ 25 · TypeScript · 推送 2026-04-30 · [GitHub](https://github.com/AbhinavPabbaraju/nexus-deep-research-agent) · [官网](https://nexus-deep-research-agent.vercel.app) · 个人维护

**多阶段深度研究 agent：规划-执行-评估循环产出研究报告**

基于 Next.js 15 的深度研究 agent 应用，采用 Planner → Executor → Evaluator 架构：Planner 生成 JSON 计划，Evaluator 依据置信度决定提前完成（DONE）、调整计划（PIVOT）、扩展工具（EXPAND）或在多出错时切换 LLM 供应商（FALLBACK）。支持 Anthropic、OpenAI、Gemini、NVIDIA NIM 四家供应商及降级链；RAG 部分通过 Supabase pgvector 存储文档分块，用 OpenAI 嵌入与 LLM 重排序。提供 SSE 流式进度、四档研究深度与 PDF/TXT 上传，部署目标为 Vercel（需 Node.js 运行时）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Evaluator 决策字段驱动 DONE/PIVOT/EXPAND/FALLBACK 循环
- 多供应商适配与出错时的供应商降级链
- pgvector RAG：文档分块入库、检索、LLM 重排序
- 所有 LLM 输出经 Zod 校验并触发重试

## 适用场景

- 对复杂问题执行多步自动化研究并追踪每步进度
- 上传 PDF/TXT 后基于自有文档做检索增强问答
- 按 Quick/Standard/Deep/Exhaustive 四档控制研究深度与耗时

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A production-grade, truly agentic research system built on a **Planner → Executor → Evaluator → Loop** architecture.
> L12: [PLANNER] — Produces a JSON plan: intent, tool sequence, max steps, target confidence

## 星数曲线

```mermaid
xychart-beta
    title "AbhinavPabbaraju/nexus-deep-research-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0adbe422cd2e` · [字段定义](../../DATASET.md)*
