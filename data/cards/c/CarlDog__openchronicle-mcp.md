# CarlDog/openchronicle-mcp

⭐ 16 · Python · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/CarlDog/openchronicle-mcp) · 个人维护

**面向 LLM agent 的持久记忆数据库，REST+MCP 双通道服务**

SQLite 持久化存储，供 LLM agent 跨会话保存决策、里程碑与被否方案，通过全文+语义混合检索（RRF 融合）取回；记忆按项目命名空间隔离。支持 git 仓库 onboarding：克隆、按相关性聚类提交并生成摘要供记忆摄入。单个 ASGI 进程同时提供 HTTP REST 与 MCP streamable-HTTP 两种传输。嵌入服务不可用时降级为 FTS5-only 检索。产品本身不含 LLM、单用户、非云端同步；可选用 age 加密备份至 rclone 远端。提供 pip 源码安装与 Docker 容器两种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全文+语义混合检索（Reciprocal Rank Fusion）
- 单 ASGI 进程同时服务 REST（/api/v1/*）与 MCP（/mcp）
- 嵌入服务故障时降级为 FTS5-only 并通过 health 端点暴露状态
- Git onboarding：聚类提交并生成可摄入记忆的摘要

## 适用场景

- 让编码 agent 在跨会话后保留项目决策与上下文
- 通过 MCP 注册到 Claude Code 等 agent 客户端做长期记忆
- 在 NAS/本地硬件上自托管记忆服务并加密备份

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: A memory database for LLM agents. Persistent semantic + keyword
> L24: - **One process, two transports.** FastAPI hosts both the REST surface
> L54: - Not a conversation engine. v3 has no LLM. Use Claude Code, Goose,

## 星数曲线

```mermaid
xychart-beta
    title "CarlDog/openchronicle-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `abc416aa0af1` · [字段定义](../../DATASET.md)*
