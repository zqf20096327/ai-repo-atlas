# ashishpatel26/omnicache-ai

⭐ 31 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/ashishpatel26/omnicache-ai) · [官网](https://ashishpatel26.github.io/omnicache-ai/) · 个人维护

**AI Agent 管道统一多层缓存库：省 token 降延迟**

面向 AI/Agent 管道开发者的 Python 缓存库，置于 LLM 调用、嵌入、检索查询与 agent 工作流之前，复用相同调用的结果。提供 8 类缓存层（响应/嵌入/检索/会话/语义/自适应语义/流式/Prompt Cache）、9 种存储后端（内存/磁盘/Redis/分层/FAISS/Chroma/Qdrant/Weaviate 等）与 13 个框架适配器（LangChain、LangGraph、AutoGen、CrewAI、Agno、OpenAI/Anthropic SDK 等）。含 TTL 策略、防击穿、多租户命名空间、Prometheus/OTEL 指标。要求 Python ≥ 3.12，pip 安装，MIT 许可。README 中与 GPTCache/LiteLLM/redis-vl 有功能对比表。

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

- 8 类缓存层覆盖 LLM 响应、嵌入、检索、会话、语义（余弦相似度）与流式
- 9 种存储后端：内存/磁盘/Redis/分层 L1+L2/FAISS/Chroma/Qdrant/Weaviate
- 13 个框架适配器：LangChain、LangGraph、AutoGen、CrewAI、Agno、A2A、OpenAI/Anthropic SDK 等
- TTL 策略、Stampede 防击穿、多租户命名空间与 Prometheus/OTEL 指标导出

## 适用场景

- Agent 管道中消除重复 LLM 调用、降低 token 成本与延迟
- LangChain/LangGraph 应用接入缓存（BaseCache/BaseCheckpointSaver 挂载）
- 语义相似问题直接返回缓存答案（余弦阈值匹配）
- 多进程/服务间通过 Redis 或分层后端共享缓存

## 场景标签

 · 领域:AI 基础设施/缓存

## 证据(README 行号)

> L6:  Drop it in front of any LLM call, embedding, retrieval query, or agent workflow
> L114: |Orchestrator|`CacheManager`|Central hub — wires backend, key builder, TTL policy, invalidation|

## 星数曲线

```mermaid
xychart-beta
    title "ashishpatel26/omnicache-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e7013244794f` · [字段定义](../../DATASET.md)*
