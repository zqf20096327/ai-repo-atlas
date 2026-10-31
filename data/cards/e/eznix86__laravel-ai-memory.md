# eznix86/laravel-ai-memory

⭐ 31 · PHP · MIT · 推送 2026-10-26 · [GitHub](https://github.com/eznix86/laravel-ai-memory) · [官网](https://packagist.org/packages/eznix86/laravel-ai-memory) · 个人维护

**给 Laravel AI SDK 的 agent 记忆扩展：存储、检索与注入上下文**

Laravel AI SDK 的 agentic 记忆扩展包：通过 AgentMemory Facade 存储/召回记忆，用 StoreMemory/RecallMemory 工具让 agent 自行决定存取，WithMemory 中间件在每次 prompt 前检索相关记忆并前置注入。机制上内容经 toEmbeddings() 转为向量存入 PostgreSQL pgvector，召回时按余弦相似度取候选并 rerank，支持相似度阈值、召回条数等配置。要求 PHP 8.4+、Laravel 12+ 与向量兼容数据库，提供 Pest + TestContainers 集成测试与 AgentMemory::fake() 测试替身。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- StoreMemory/RecallMemory agent 工具让模型自行决定存取记忆
- WithMemory 中间件自动检索并前置注入相关记忆
- pgvector 余弦相似度检索 + rerank 重排
- AgentMemory::fake() 提供确定性 embeddings 的测试替身

## 适用场景

- 让我的 Laravel agent 记住用户偏好与历史决策
- 多 agent/工具协作时持久化共享事实避免重复上下文
- 按相似度检索记忆作为 prompt 上下文注入

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Agentic memory for Laravel AI SDK. It keeps your agent in context.
> L11: - laravel AI SDK
> L56: use Eznix86\AI\Memory\Tools\RecallMemory;
> L58: use Laravel\Ai\Contracts\Agent;

## 星数曲线

```mermaid
xychart-beta
    title "eznix86/laravel-ai-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `497906e37c0d` · [字段定义](../../DATASET.md)*
