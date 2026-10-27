# dialexity/dialectical-framework

⭐ 22 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/dialexity/dialectical-framework) · [官网](https://dialexity.com) · 组织维护

**面向 LLM 的辩证推理框架：张力图谱驱动综合判断**

Python 库形式的 AI 推理框架：对每个论题生成对立论题，展开 T+/T-/A+/A- 四方面，映射正反两极的过度之处与互补之处，并经生成规则校验后驱动出综合结论。推理以语义图形式持久化在 Memgraph 或 Neo4j 图数据库中，可跨会话累积查询。提供三个对话式 agent（Analyst/Explorer/Advisor）作为宿主应用的接入入口，需 Python 3.11+ 与 LLM 提供商（OpenAI/Anthropic/Bedrock），LLM 调用依赖外部 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 论题-反题-四方面结构化，规则校验后的综合推导
- 推理持久化为语义图（Memgraph/Neo4j），可查询可视化
- 三个 agent 入口：Analyst/Explorer/Advisor（含只读 sealed 配置）
- pip 安装为 Python 库，含控制台示例与 notebook

## 适用场景

- 为决策支持类应用接入权衡双方立场的推理引擎
- 构建对立场对立议题做调解或伦理建模的应用
- 需要跨会话累积已验证推理结构的领域知识图

## 场景标签

 · 领域:AI 推理/决策支持

## 证据(README 行号)

> L84: Wherever the answer is a tension rather than a fact, this drops in as the reasoning engine: decision support that w
> L92: ```python

## 星数曲线

```mermaid
xychart-beta
    title "dialexity/dialectical-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `22e43145363a` · [字段定义](../../DATASET.md)*
