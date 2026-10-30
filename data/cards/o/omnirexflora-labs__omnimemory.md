# omnirexflora-labs/omnimemory

⭐ 16 · Python · MIT · 推送 2025-12-01 · [GitHub](https://github.com/omnirexflora-labs/omnimemory) · 组织维护

**为 AI agent 提供自演化记忆层的框架（SDK/REST/CLI）**

面向 AI agent 开发者的记忆管理框架：通过双 Agent 合成引擎（Episodic + Summarizer）解析对话，提取行为模式与叙事，自动检测冲突并执行更新/删除/跳过操作；检索采用复合评分（相关性×[1+新近度+重要性]）。提供 app/user/session 三级多租户隔离，支持 Qdrant、ChromaDB、PostgreSQL(pgvector)、MongoDB 四种后端切换。交付形态为 Python SDK、FastAPI REST 服务与 CLI，含 Prometheus 指标、连接池与异步后台合成。需 LLM API key 与外部向量库，add_memory 要求批量消息（默认 10 条）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双 Agent 合成（Episodic + Summarizer）解析对话并提取行为模式
- 自演化记忆：冲突时自动 UPDATE/DELETE/SKIP
- 复合评分检索：Relevance × (1 + Recency + Importance)
- 三级多租户隔离（app/user/session），4 种向量库后端可切换

## 适用场景

- 为客服 agent 构建跨会话的用户偏好记忆
- SaaS 多租户场景下为各应用隔离存储 agent 记忆
- agent 需要基于历史记忆回答用户问题的检索问答
- 上下文窗口满时压缩对话并保留摘要

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: It doesn't just "store" messages. It employs a **Dual-Agent Synthesis** engine to interpret conversations, extract 
> L29: ### 1. Dual-Agent Synthesis
> L177: The `AgentMemorySDK` provides a complete "query memory + generate answer" loop. It retrieves relevant memories and

## 星数曲线

```mermaid
xychart-beta
    title "omnirexflora-labs/omnimemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `024e004540d9` · [字段定义](../../DATASET.md)*
