# kongusen/loom-agent

⭐ 24 · Python · Apache-2.0 · 推送 2026-04-30 · [GitHub](https://github.com/kongusen/loom-agent) · 个人维护 · 中文 README

**可嵌入的 Python Agent SDK：构建有状态 agent 运行时内核**

面向应用开发团队的可嵌入 Agent SDK/运行时内核，提供 Agent+Model+Runtime 组合与子系统：受治理的工具能力路径（files/web/shell/MCP）、Harness 执行策略（单次/生成-评估循环/人工门控）、编排委派、知识注入、cron 调度、会话持久化与长期记忆。支持 OpenAI、Anthropic Claude、Gemini 模型接入，外部事件统一归一化为 RuntimeSignal 处理。README 强调它不是完整托管 agent 平台、网关或技能市场，网关/面板等需自行以适配器组合。pip 安装，需 Python 3.11+，许可为 Apache 2.0 + Commons Clause。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent+Model+Runtime 运行时内核，子系统覆盖工具/记忆/技能/Harness/编排/知识/cron
- 治理式能力路径：Permission → Veto → Rate limit → Execute → Observe
- Harness 支持生成-评估循环、人工门控与自定义候选生成
- 会话持久化（FileSessionStore）与 MemorySource 长期记忆分离

## 适用场景

- 在自己的产品内构建客服 agent 平台（自带网关、路由与质量控制）
- 构建带受治理工具使用与记忆连续性的内部工程 copilot
- 构建响应 cron 与外部信号的自动化工作流 agent
- 构建带检索、引用与策略驱动执行的企业知识 agent

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A Python Agent SDK for stateful runtime execution, context control, safety boundaries, and extensible capabilities
> L16: Loom is an embeddable Agent SDK that helps developers build agent platform capabilities similar to Hermes and OpenC
> L92: |Tool Use|`Capability`, tool registry, `GovernancePolicy`|Exposes Python tools, shell, files, web, MCP, and builtin

## 星数曲线

```mermaid
xychart-beta
    title "kongusen/loom-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `54b155f63cf8` · [字段定义](../../DATASET.md)*
