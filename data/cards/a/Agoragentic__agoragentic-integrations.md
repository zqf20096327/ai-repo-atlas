# Agoragentic/agoragentic-integrations

⭐ 41 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Agoragentic/agoragentic-integrations) · [官网](https://agoragentic.com/integrations/) · 组织维护

**已部署 AI agent 的治理与证据层：策略边界、审批与回执**

Triptych OS (Agent OS) 的开源集成与治理入口：为已有 agent/框架（LangGraph、CrewAI、OpenAI Agents 等）叠加策略决策、审批记录、生命周期证据与本地回执，不要求重写现有编排。提供 Harness Core、Micro ECF/ECF Core、Node/Python SDK、MCP/ACP 协议源码、Agent OS CLI 等多条路径，本地路径无需账户或外部模型提供商；Claude Code 有打包的 PreToolUse 强制钩子，多数其他框架仅为映射示例。托管 Router/Interchange 提供可选的 agent 商务与付费路由，本地开源层不依赖它。面向已有 agent 产品、需要回答“agent 被授权做了什么、证据何在”的开发者与平台团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 112 个集成面的机器可读目录 integrations.json，并区分集成能力级别
- 本地 no-spend 路径：npx init/validate/run 生成策略与回执工件，无需账户或外部提供商
- Claude Code 提供 PreToolUse allow/ask/deny 打包钩子实现强制执行
- 回执分类体系明确各回执类别的证明边界（本地/宿主观察/托管执行/结算）

## 适用场景

- 给现有 agent 框架加策略边界与审批记录而不重写
- 保存 agent 动作的可审计证据与本地回执
- 通过 Interchange 连接跨组织的买卖 agent 与市场
- 治理 agent 可访问的源码与上下文边界（ECF）

## 场景标签

 · 领域:AI agent 基础设施/治理

## 证据(README 行号)

> L7: **Agoragentic is Triptych OS (Agent OS) for deployed agents and swarms. This repository is its open integration, gov
> L91: Keep the existing framework or runtime. Start with Harness Core for policy decisions, approvals, lifecycle evidence
> L94: LangGraph       ─┐


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `14854412dd7b` · [字段定义](../../DATASET.md)*
