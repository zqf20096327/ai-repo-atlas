# thatsme/AlexClaw

⭐ 119 · Elixir · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/thatsme/AlexClaw) · 个人维护

**单用户自托管个人 AI agent：监控信息源并经 Telegram/Discard 对话**

基于 Elixir/OTP 构建的单操作员个人 AI agent，运行在自有基础设施上。监控 RSS、网页、GitHub 仓库与 API，经固定只读查询读 PostgreSQL，存入 pgvector 知识库，按 Cron 调度多步工作流（含条件分支与熔断），通过 Telegram/Discord 网关与唯一所有者对话。核心机制：按推理层级（light/medium/heavy/local）将任务路由到最便宜的可配置 LLM（云端与本地，含 Gemini/Claude/Ollama/LM Studio），凭据存于内置 OpenBao，管理操作需 2FA。支持 MCP 只读服务器、BEAM 多节点集群与运行时动态技能加载。明确单用户、无多租户访问控制；部分旧技能已标记废弃。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按推理层级的多模型 LLM 路由（云端与本地提供商，默认含 Ollama/LM Studio）
- 计划-执行-评估推理循环，可暂停/转向/中止，全程留痕并嵌入 pgvector
- 技能级 OTP 熔断器与死信路由（跳过/停止/回退）
- MCP 服务器暴露知识/工作流（只读、密钥脱敏、操作经审计）

## 适用场景

- 自托管一个只服务自己的信息监控与提醒 agent
- 定时抓取 RSS/网页/GitHub/数据库并按工作流加工后推送到 Telegram/Discord
- 通过聊天让 agent 执行计划-执行-评估式的研究任务

## 场景标签

`工作流自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L5: A personal AI agent for a single user, built on Elixir/OTP.
> L7: AlexClaw monitors sources (RSS feeds, web pages, GitHub repositories, APIs) and reads PostgreSQL databases through f
> L19: - **Multi-Model LLM Router** — Tier-based routing (`light` / `medium` / `heavy` / `local`) with priority-based sele

## 星数曲线

```mermaid
xychart-beta
    title "thatsme/AlexClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 117 --> 120
    line [118, 119, 119]
```

2026-10-18 118 → 2026-10-30 119（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d6413d5422a4` · [字段定义](../../DATASET.md)*
