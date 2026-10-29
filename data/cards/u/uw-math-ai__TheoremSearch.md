# uw-math-ai/TheoremSearch

⭐ 23 · Jupyter Notebook · 推送 2026-10-03 · [GitHub](https://github.com/uw-math-ai/TheoremSearch) · [官网](https://theoremsearch.com) · 组织维护

**覆盖 900 万数学定理的语义检索 API，供数学家与证明 agent 使用**

面向数学家和数学证明 agent 的定理语义检索系统：索引 arXiv、Stacks Project 等八个来源共约 900 万条定理，支持自然语言查询，报告 4 秒级延迟。以生产 REST API 形式提供，返回带元数据与相似度分数的定理级结果；另提供 MCP 工具端点供 AI agent 以单一 theorem_search 工具调用。README 载有 Hit@10 检索性能对比表，并列出 arXiv 论文与数据集链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引 arXiv、Stacks Project 等八个来源约 900 万条定理
- 自然语言语义查询，报告 4 秒延迟
- 生产 REST API 返回带元数据与相似度分数的结果
- 提供 MCP 工具端点供 AI agent 调用

## 适用场景

- 数学研究中按语义查找定理陈述
- 数学证明 agent 通过 MCP 工具检索相关定理
- 查找包含某定理的原始论文

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: Mathematicians and math prover agents need fast and efficient theorem search.
> L49: TheoremSearch is also available as an MCP tool for AI agents with a single tool `theorem_search`. Endpoint: `https:

## 星数曲线

```mermaid
xychart-beta
    title "uw-math-ai/TheoremSearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `662e54703e9c` · [字段定义](../../DATASET.md)*
