# mongodb-developer/event-venue-operator

⭐ 76 · Python · MIT · 推送 2026-07-16 · [GitHub](https://github.com/mongodb-developer/event-venue-operator) · 组织维护

**基于 MongoDB Atlas 的 agentic 场馆运营演示（三层记忆+混合检索）**

面向探索 agentic 模式的开发者构建在 MongoDB Atlas 上的演示种子项目：以网球赛事雨延场景为叙事，展示长期/短期/共享三层记忆建模、Voyage AI 多模态嵌入与 Atlas Vector Search 混合检索、视觉文档 RAG、按人物画像分段的 agent 决策，以及 LangGraph 五节点执行链（perceive→plan→hitl_gate→act→reflect），LLM 使用 Claude Sonnet。提供确定性舞台 UI、FastAPI 端点与 Langfuse 可选追踪；明确声明非生产平台，CI/错误恢复等不在教程范围内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层记忆（长期/短期/共享）以 Atlas 集合存储与检索
- Voyage 多模态嵌入 + Atlas Vector Search 混合检索与视觉文档 RAG
- LangGraph 链端到端运行（perceive→plan→hitl_gate→act→reflect）
- FastAPI 暴露检索/RAG/嵌入检查等 API 端点，支持可选 Langfuse 追踪

## 适用场景

- 学习在 MongoDB Atlas 上建模 agent 记忆与检索模式
- 跑通 LangGraph agent 端到端执行链并观察各阶段
- 参考人物画像分段的 agent 决策与视觉文档 RAG 实现

## 场景标签

`Agent 记忆` `Agent 框架` `RAG` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agentic event-venue operator demo built on MongoDB Atlas. Showcases three-layer memory (long-term, short-term, share
> L9: A demo seed for practitioners exploring agentic patterns on MongoDB. Shows how to model agent memory, retrieve patte

## 星数曲线

```mermaid
xychart-beta
    title "mongodb-developer/event-venue-operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-26 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `45cb96704924` · [字段定义](../../DATASET.md)*
