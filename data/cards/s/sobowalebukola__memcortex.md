# sobowalebukola/memcortex

⭐ 21 · Go · MIT · 推送 2026-09-10 · [GitHub](https://github.com/sobowalebukola/memcortex) · [官网](https://www.memcortex.ai) · 个人维护

**为 LLM 应用提供持久长期记忆的 Memory-RAG 中间层**

Memcortex 是一个 Go 编写的概念验证（PoC）项目，为对话 agent 与 LLM 应用提供持久化长期记忆：用 nomic-embed-text 嵌入模型（经 Ollama）将文本转向量，存入 Weaviate 的 Memory_idx 类，检索 top-K 相关记忆并注入 prompt，新记忆可异步持久化。以 API 服务器 + 内存中间件形式提供，通过 /chat 端点（X-User-ID 头区分用户）使用，部署依赖 Docker Compose 与 Go 1.20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- nomic-embed-text 嵌入 + Weaviate 向量存储与检索
- 中间件自动将 top-K 相关记忆注入 prompt
- 新记忆异步持久化，跨会话保留
- 按 X-User-ID 隔离的 /chat API

## 适用场景

- 让聊天机器人或 agent 跨会话记住用户细节
- 为个性化应用构建记忆层
- 突破上下文窗口限制，无限期召回历史交互

## 场景标签

 · 领域:LLM 基础设施/记忆层

## 证据(README 行号)

> L7: Memcortex is a Proof of Concept (PoC) designed to equip conversational agents and LLM applications with persistent, 
> L24: Memcortex stores user/application memories as both text and vectors in Weaviate and exposes a memory manager + midd
> L29: 4. Injects retrieved memories into the prompt before it reaches the LLM.

## 星数曲线

```mermaid
xychart-beta
    title "sobowalebukola/memcortex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `59f9095a84bb` · [字段定义](../../DATASET.md)*
