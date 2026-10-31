# daizhongming/YiQiao

⭐ 13 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/daizhongming/YiQiao) · 个人维护 · 中文 README

**面向 AI 助手/Agent 的自托管记忆服务**

自部署的 Agent 记忆服务：以 Docker Compose 一套交付 REST API、运维 Dashboard、语义与图记忆（PostgreSQL+pgvector，可选 Neo4j）、聊天历史导入导出、用量控制与 Webhook。集成方用项目级 API Key 认证，另有 MCP Streamable HTTP 端点与 Python 包（同步/异步入口）。浏览器首次运行向导配置 LLM 与嵌入模型 provider（含自定义 OpenAI 兼容 base URL）。限制：默认单机 Compose，非高可用集群；记忆抽取与语义搜索需配置可用的 LLM/嵌入模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker Compose 单套部署 REST API、Dashboard、MCP 端点与数据库
- 语义（pgvector）+ 图（可选 Neo4j）双记忆存储
- 项目级 API Key、角色访问、用量限制与请求日志
- pip 安装的 Python 同步/异步客户端（Memory/AsyncMemory）

## 适用场景

- 为我的 AI 助手或编码 Agent 提供持久化记忆
- 私有化运营支持上下文与研究记忆，掌控存储与模型关系
- 导入聊天历史并做语义搜索与图探索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: YiQiao is a self-hosted memory service for AI assistants and agents. It combines
> L126: - Project-scoped memory add, search, update, delete, history, and feedback APIs.
> L131: - Browser-based provider configuration for bundled LLM and embedding adapters,

## 星数曲线

```mermaid
xychart-beta
    title "daizhongming/YiQiao 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8bf4d8ea8b57` · [字段定义](../../DATASET.md)*
