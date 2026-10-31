# gethelio/helio

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/gethelio/helio) · [官网](https://helio.so) · 组织维护

**MCP 代理治理层：拦截审批 AI 工具调用并管控预算与审计**

Helio 是部署在 AI agent 与 MCP 工具服务器之间的代理：每个工具调用先经其策略引擎判定（ALLOW/APPROVE/DENY），支持前置条件要求、跨工具累计花费预算、限流、审批路由（Slack/仪表盘）与全量审计。策略不在模型上下文中，代理持有会话身份、预算与证据状态。接入只需把 MCP 客户端指向 Helio，不改 agent 代码；可选 Python SDK 补充证据标注。默认以同一用户运行的本地安装存在安全边界，需独立用户或容器部署收窄。通过 npx 安装，自带仪表盘。

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

- 声明式 YAML 策略引擎（按工具名/参数/环境/累计状态匹配，热重载）
- 跨工具跨服务器的统一花费预算与持久化账本
-  Slack 与仪表盘的人审审批流程
- 每条审计记录携带生效配置哈希，策略变更可追溯

## 适用场景

- 对 agent 的生产环境工具调用做拦截与人工审批
- 给付费 API 工具设每日花费上限并留存账本
- 统一治理多个 MCP 服务器并集中审计所有调用

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: Helio is an MCP proxy that sits between your AI agents and the tools they use. Every tool call passes through Helio
> L50:  MCP clients send tool calls through Helio — which applies its policy engine, evidence grounding, approval workflow
> L54: 1. **Proxy only**: Point your MCP client at Helio instead of your MCP server. Zero code changes. Immediate governan

## 星数曲线

```mermaid
xychart-beta
    title "gethelio/helio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `af4dd275d959` · [字段定义](../../DATASET.md)*
