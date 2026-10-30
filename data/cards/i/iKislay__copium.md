# iKislay/copium

⭐ 20 · Python · Apache-2.0 · 推送 2026-09-05 · [GitHub](https://github.com/iKislay/copium) · 个人维护

**面向 AI 编程工具的 LLM 上下文压缩本地代理**

Copium 是部署在 agent 与 AI 提供商之间的本地压缩代理：拦截 Claude/GPT/Gemini/Bedrock 及本地模型的请求，通过 ToolPrefilter、SmartCrusher、会话去重、错误卡片化等组件压缩 token，README 称 65-94% 节省。支持 copium wrap 一键接入 Claude Code、Cursor、Aider、Copilot 等工具，另提供 MCP 代理与服务器模式、Python 库、跨 agent 共享上下文（SQLite 持久化、语义检索）、压缩前数据丢失防护（Claude Code PreCompact 钩子）与质量门（压缩后校验、不达标自动回退）。限制：Google Antigravity 因 OAuth 不暴露代理设置，当前无法拦截。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地代理压缩 65-94% token，支持 Anthropic/OpenAI 兼容、Bedrock、Vertex 端点
- copium wrap/unwrap 一键接入 Claude Code、Cursor、Aider、Copilot、Cline 等工具
- 质量门：压缩后四项校验，不达标自动回退原文；CCR 支持可逆检索
- 跨 agent SharedContext：SQLite 持久化、来源追踪、冲突解决与语义检索

## 适用场景

- 降低 AI 编程助手长会话的 token 消耗与费用
- 防止 agent 自动压缩时丢失推理链与架构决策等关键上下文
- 多 agent 系统间共享、持久化并检索压缩后的上下文
- 压缩 MCP 工具的描述、schema 与响应体积

## 场景标签

 · 领域:LLM 基础设施/上下文工程

## 证据(README 行号)

> L164: Copium sits between your agent and the AI provider and compresses everything before it goes out. It's a local prox
> L145: > 65–94% fewer tokens. Zero quality loss. Drop-in proxy for Claude, GPT, Gemini, Bedrock, and local LLMs.

## 星数曲线

```mermaid
xychart-beta
    title "iKislay/copium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f7461bd8623f` · [字段定义](../../DATASET.md)*
