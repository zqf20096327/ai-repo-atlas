# rafaelpierre/openai-agents-redis

⭐ 16 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/rafaelpierre/openai-agents-redis) · [官网](https://pypi.org/project/openai-agents-redis/) · 个人维护

**用 Redis 做持久层的 OpenAI Agents SDK 会话管理实现**

面向 OpenAI Agents SDK 的 Python 库，提供基于 Redis 的 RedisSession 会话持久化，用于在多次交互间保存对话上下文。安装通过 uv 或 pip，代码示例展示从 agents_redis.session 导入 RedisSession 并配置使用。测试运行需 Docker、uv，OpenAI Agents SDK 与 API Key 为可选项。Roadmap 列出全文搜索、向量/混合搜索、监控面板等未完成项。附 YouTube 演示视频链接。

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

- RedisSession 提供 Redis 持久化会话
- 维护跨交互的对话记忆上下文
- 以 uv/pip 安装的 Python 3.13+ 库

## 适用场景

- 为 OpenAI Agents SDK 应用接入 Redis 会话持久化
- 多轮对话场景中保持 agent 上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: > Native OpenAI Agents SDK session management implementation using Redis as the persistence layer.
> L18: - 🧠 **Intelligent Agents**: Built on OpenAI's powerful Agents SDK

## 星数曲线

```mermaid
xychart-beta
    title "rafaelpierre/openai-agents-redis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7c151b44594a` · [字段定义](../../DATASET.md)*
