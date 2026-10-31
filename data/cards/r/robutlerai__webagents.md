# robutlerai/webagents

⭐ 13 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/robutlerai/webagents) · [官网](https://robutler.ai/webagents) · 组织维护

**构建、运行与互联 AI agent 的 Python/TypeScript 框架**

开源框架，用 Python 和 TypeScript SDK 构建、服务并互联 AI agent。核心机制：模块化技能（工具/提示/钩子/HTTP 端点，支持 SKILL.md 格式）、agent 间自然语言委派与实时意图发现、基于 access 组的调用方权限控制、通过 @pricing 与 x402 支付挑战实现计费（经 Robutler 平台，创作者获得 Creator Rewards）。支持 OpenAI Chat Completions、A2A、MCP、ACP、OpenAI Realtime 等协议，自带 CLI 与操作系统沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python/TypeScript 双 SDK，模块化技能组合（含 SKILL.md 格式）
- agent 间委派、实时意图发现与经验证身份的互联
- 支持 OpenAI/A2A/MCP/ACP/OpenAI Realtime 等协议
- @pricing 定价工具与 x402 支付挑战，经 Robutler 计量结算

## 适用场景

- 构建可对外提供服务的 AI agent 并通过 HTTP 服务化
- 让多个 agent 互相发现、委派任务并计量使用
- 给 agent 工具定价并通过 Robutler 获得使用收益

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: WebAgents is an open-source framework for building connected AI agents with a simple, complete API. Put your agent i
> L13: - **Modular skills.** Combine tools, prompts, hooks and HTTP endpoints into reusable skills, or load SKILL.md skill
> L18: - **Every major protocol.** OpenAI Chat Completions, A2A (Agent2Agent) v1.0 with a signed agent card, UAMP and Open

## 星数曲线

```mermaid
xychart-beta
    title "robutlerai/webagents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `edd60454e9fc` · [字段定义](../../DATASET.md)*
