# Mdx2025/BrainX-The-First-Brain-for-OpenClaw

⭐ 32 · JavaScript · 推送 2026-09-01 · [GitHub](https://github.com/Mdx2025/BrainX-The-First-Brain-for-OpenClaw) · 个人维护

**OpenClaw AI 代理的持久记忆层：向量存储与语义检索**

面向 OpenClaw 代理的持久记忆系统，由 CLI 记忆引擎与可选的运行时插件两部分组成。基于 PostgreSQL 与 pgvector 存储向量记忆，使用 OpenAI embeddings 实现语义检索；提供自动学习管线（捕获、分类、去重、评分、合并）、跨代理学习、PII 清洗、验证状态等治理机制，以及 wiki digest、工作记忆、JIT 召回、工具建议等运行时上下文能力。安装需要 Node.js 20+、PostgreSQL 14+、pgvector 与 OpenAI API key，通过 git clone 与 npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PostgreSQL + pgvector 持久向量存储与语义检索
- 自动学习管线：捕获、分类、去重、评分、合并、晋升
- PII 清洗、验证状态、跨代理召回门控等治理机制
- OpenClaw 运行时插件：wiki digest、工作记忆、JIT 召回、工具建议

## 适用场景

- 让多个 OpenClaw 代理共享一层跨会话持久记忆
- 将对话、决策与教训沉淀为可语义检索的知识
- 在运行时为代理注入相关上下文与风险提示

## 场景标签

`Agent 记忆` `多智能体` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L9: **BrainX V6 is persistent AI agent memory for OpenClaw.** It gives OpenClaw agents long-term memory, semantic search
> L27: - **BrainX skill and CLI**: memory storage, search, injection, doctor, lifecycle, knowledge sync, backups, migratio
> L30: The CLI is the durable memory engine. The plugin is the runtime adapter.

## 星数曲线

```mermaid
xychart-beta
    title "Mdx2025/BrainX-The-First-Brain-for-OpenClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `630bdf02fade` · [字段定义](../../DATASET.md)*
