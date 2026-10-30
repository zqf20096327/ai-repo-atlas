# sidclawhq/platform

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/sidclawhq/platform) · [官网](https://sidclaw.com) · 组织维护

**AI agent 治理层：拦截工具调用，按策略审批并留痕**

面向已部署 AI agent 的组织提供审批与问责平台：拦截 agent 的每次工具调用，经策略引擎判定 allow/approval_required/deny，高风险动作以带上下文的卡片交人工审批，全程记录哈希链审计轨迹。提供 TypeScript/Python SDK、MCP 治理代理与 Claude Code Hooks 零代码接入，集成 LangChain、OpenAI Agents、CrewAI 等 18+ 框架，审批可通过 Slack/Teams/Telegram 完成。许可分层：SDK 为 Apache-2.0，平台（API/Dashboard）为 FSL 1.1，年收入低于 CHF 1M 的组织免费，2028 年转为 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 策略引擎三态判定：allow / approval_required / deny
- 带完整性哈希链的防篡改审计轨迹与 SIEM 导出
- MCP Governance Proxy 包装任意 MCP server，零代码接入
- 18+ 框架集成（LangChain、OpenAI Agents、CrewAI、Claude Agent SDK 等）

## 适用场景

- 生产环境 AI agent 执行高风险操作前需人工审批
- 金融/医疗等行业满足人工监督与审计合规要求
- 在 Slack/Teams 中直接批准或拒绝 agent 的动作

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L17: Your agents call tools without oversight. SidClaw intercepts every tool call, checks it against your policies, and 
> L198: SidClaw sits at the **tool-call layer**: the moment an agent decides to act in the real world.
> L210: |LangChain|`@sidclaw/sdk/langchain`|`sidclaw.middleware.langchain`|

## 星数曲线

```mermaid
xychart-beta
    title "sidclawhq/platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `265ead3e2835` · [字段定义](../../DATASET.md)*
