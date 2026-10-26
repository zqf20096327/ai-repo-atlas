# MitulShah1/openai-agents-go

⭐ 45 · Go · MIT · 推送 2026-10-19 · [GitHub](https://github.com/MitulShah1/openai-agents-go) · [官网](https://mitulshah1.github.io/openai-agents-go/) · 个人维护

**非官方 Go 版 OpenAI Agents SDK：构建多 agent 工作流**

社区维护的 Go 语言 SDK，用于基于 OpenAI API 构建多 agent 工作流，功能覆盖 agent handoff、Go 函数工具调用（含审批与并行执行）、结构化 JSON 输出、流式响应、OpenTelemetry 追踪。内置 9+ 安全护栏：PII 检测掩码、内容审核、限流、提示注入检测等。会话持久化支持内存/文件/SQLite/PostgreSQL/Redis 后端。核心库除 OpenAI Go SDK 外零依赖，需 Go 1.24+。与官方 SDK 无隶属关系。

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

- agent handoff 与多 agent 编排（双向转移、条件启用）
- 9+ 安全护栏：PII 检测（10+ 类型）、审核、限流、提示注入检测
- 会话持久化多后端（内存/文件/SQLite/PostgreSQL/Redis）
- 工具审批 human-in-the-loop 与并行工具执行

## 适用场景

- 用 Go 构建调用 OpenAI API 的多 agent 应用
- 为生产 agent 应用加 PII 掩码与内容审核护栏
- 跨请求保持对话上下文并可换用数据库会话后端

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: > **Community Project**: This is an **unofficial** community-maintained Go SDK for building AI agents with OpenAI's
> L33: - **Multi-Agent Workflows**: Seamless agent handoffs and composition

## 星数曲线

```mermaid
xychart-beta
    title "MitulShah1/openai-agents-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9cb9ab1ae7d5` · [字段定义](../../DATASET.md)*
