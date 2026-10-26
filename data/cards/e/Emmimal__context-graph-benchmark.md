# Emmimal/context-graph-benchmark

⭐ 31 · Python · MIT · 推送 2026-06-27 · [GitHub](https://github.com/Emmimal/context-graph-benchmark) · [官网](https://towardsdatascience.com/vector-rag-isnt-enough-i-built-a-context-graph-layer-for-multi-agent-memory/) · 个人维护

**多智能体 LLM 记忆架构的纯 Python 基准：上下文图 vs 向量 RAG**

对三种记忆架构（Raw History Dump、Vector-Only RAG、Context Graph）做对比基准测试：事实以 (subject, predicate, object) 三元组存入 NetworkX MultiDiGraph，通过图遍历检索，全程零 LLM 调用、完全确定性可复现。覆盖五个脚本化多智能体场景与 18 个评分查询，用确定性子串匹配打分；内建事实覆盖机制与 join 查询两跳遍历。面向需要评估记忆架构选型的多智能体系统开发者。限制：TF-IDF 而非神经嵌入、别名表代替实体链接、两条查询故意不修复。

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

- 三种记忆架构在五个场景、18 个评分查询上的对比（零 LLM 调用，确定性可复现）
- 事实以三元组存入 NetworkX MultiDiGraph，图遍历检索含 join 两跳查询
- 内建事实覆盖（supersession）机制，避免陈旧事实
- 六个回归测试锁定头条数字与结构性结论

## 适用场景

- 多智能体流水线中评估记忆架构选型
- 了解对话长度增长时各记忆架构的 token 成本扩展性
- 审查 Neo4j 导出格式的 Cypher 语句生成

## 场景标签

`模型评测` `知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: This project benchmarks three memory architectures on that exact problem and measures where the ceiling is for each 
> L40: Three memory architectures, each implemented in pure Python with no LLM calls anywhere:
> L49: A benchmark harness runs all three against five scripted multi-agent scenarios and grades answers by deterministic 

## 星数曲线

```mermaid
xychart-beta
    title "Emmimal/context-graph-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `89522e8d5199` · [字段定义](../../DATASET.md)*
