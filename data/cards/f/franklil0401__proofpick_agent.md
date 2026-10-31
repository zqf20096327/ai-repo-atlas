# franklil0401/proofpick_agent

⭐ 16 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/franklil0401/proofpick_agent) · [官网](https://franklil0401.github.io/proofpick_agent/) · 个人维护 · 中文 README

**显示器选购演示：带确定性约束复核的 Agentic RAG 决策 Agent**

基于 Youtu-RAG（FastAPI/WebUI/知识库基础设施以 Git subtree 复用）的作品集级 MVP：有界 ReAct 规划器自主调用 Text2SQL、向量检索+Reranker 的 KB Search 与 Evidence Check 三类工具，配合短期会话与长期偏好 Memory 支持连续追问；最终由 SQL/代码实现的 Constraint Checker 独立复核预算、尺寸、接口等硬约束，LLM 不能覆盖结果。演示为脱敏结果回放，非实时模型调用；当前仅覆盖 12 个显示器型号，未接入实时价格。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 有界 ReAct 编排 Text2SQL / KB Search / Evidence Check 三类工具
- SQL/代码实现的确定性 Constraint Checker，LLM 不可覆盖推荐资格
- 短期会话条件与长期偏好 Memory，支持连续追问
- 冻结评测：增强组 92/120（76.67%），违规推荐 0/43

## 适用场景

- 作为 Agentic RAG + 约束复核架构的作品集演示复现
- 了解 ReAct 规划、Text2SQL 与确定性安全门的组合实现
- 在受限商品域内体验带证据核验的选购推荐

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: 基于 Agentic RAG 的消费决策 Agent：自主调用 Text2SQL、知识库检索和证据核验工具，并使用确定性安全门阻止违反硬条件的推荐。`SmartBuy` 是当前的显示器选购演示场景。
> L22: ## 为什么它是 Agent
> L40: 5. Constraint Checker 用 SQL/代码独立复核全部硬约束；失败、未知或冲突候选不能进入推荐集合。

## 星数曲线

```mermaid
xychart-beta
    title "franklil0401/proofpick_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8e5f340738a9` · [字段定义](../../DATASET.md)*
