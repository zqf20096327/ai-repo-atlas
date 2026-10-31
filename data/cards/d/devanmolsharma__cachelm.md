# devanmolsharma/cachelm

⭐ 15 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/devanmolsharma/cachelm) · [官网](https://pypi.org/project/cachelm/) · 个人维护

**LLM 应用的语义缓存层：为改述提问复用缓存回答**

面向 LLM 应用的 Python 语义缓存库：拦截 OpenAI 客户端调用，将 prompt 向量化后在向量库中检索相似的历史提问，命中阈值内直接返回缓存回答，未命中则调用 LLM 并把回答存入缓存。向量库可选 ChromaDB/Redis/ClickHouse/Qdrant，向量化器可选 FastEmbed/RedisVL/Text2Vec-Chroma，支持流式 chat completions，并提供 pre_cache_save/post_cache_retrieval 中间件钩子（如 Replacer 将可变字段替换为占位符以提高命中率）。通过 pip extras 按需安装各集成。

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

- 语义缓存：改述/同义提问命中同一缓存回答
- 可插拔向量库（ChromaDB/Redis/ClickHouse/Qdrant）与向量化器
- 支持流式 chat completions
- 中间件钩子（Replacer 占位符替换等）定制缓存行为

## 适用场景

- 高流量 LLM 应用减少重复 API 调用开销
- 实时聊天机器人降低响应延迟
- 含可变字段（用户名/ID）的模板化提问提高缓存命中率

## 场景标签

 · 领域:LLM 基础设施/缓存

## 证据(README 行号)

> L40: `cachelm` intercepts your LLM API calls and adds a smart caching layer.
> L42: 1. **Intercept**: A user sends a prompt through the `cachelm`-enhanced client.

## 星数曲线

```mermaid
xychart-beta
    title "devanmolsharma/cachelm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1f2c91683479` · [字段定义](../../DATASET.md)*
