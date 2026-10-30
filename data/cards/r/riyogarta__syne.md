# riyogarta/syne

⭐ 15 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/riyogarta/syne) · 个人维护

**自托管的个人 AI Telegram 助手：长期记忆存在你自己的服务器上**

一个自托管的 Telegram 机器人：与用户对话并跨天/周/重启地记住信息。记忆系统由 pgvector 语义检索、实体知识图谱和衰减引擎组成——明确要求记住的事实永久保存，自动捕获的随使用衰减。写入前由本地 Ollama 小模型（qwen3:0.6b，$0 成本）评估是否值得存储。聊天模型接入 Anthropic/Google/OpenAI/Together 等 API 或订阅 OAuth。运行时配置全部存于 PostgreSQL，通过对话修改而非配置文件。需要 Docker 运行 PostgreSQL+pgvector，2GB 内存起步。可选扩展包括文档读写、图像生成、语音、子代理等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 显式事实永久保存，自动捕获记忆随使用衰减并可驱逐
- 三层写入过滤：规则→本地 Ollama 评估器→相似度去重
- pgvector HNSW 语义检索 + 实体关系知识图谱双通道召回
- 配置全部存于 PostgreSQL，通过对话修改，无配置文件

## 适用场景

- 在 Telegram 上养一个记住个人长期信息的 AI 助手
- 把记忆数据完整保存在自己的服务器与数据库里
- 用对话方式修改 AI 的身份、规则与行为配置

## 场景标签

`Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L5: Self-hosted personal AI on Telegram. Runs on your own server, stores everything in your own PostgreSQL. Explicit fac
> L11: A Telegram bot you self-host. You chat with it. It remembers what you tell it to remember, across days, weeks, rest
> L13: - **Persistent long-term memory** — semantic search via pgvector + a small knowledge graph for entity-relation quer

## 星数曲线

```mermaid
xychart-beta
    title "riyogarta/syne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `299d461a630a` · [字段定义](../../DATASET.md)*
