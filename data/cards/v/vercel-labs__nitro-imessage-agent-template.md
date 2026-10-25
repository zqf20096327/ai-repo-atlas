# vercel-labs/nitro-imessage-agent-template

⭐ 57 · TypeScript · Apache-2.0 · 推送 2026-05-21 · [GitHub](https://github.com/vercel-labs/nitro-imessage-agent-template) · [官网](https://nitro-imessage-agent.vercel.app) · 组织维护

**可部署的 iMessage AI agent 模板：短信进、可重试的 LLM+工具回复出**

基于 Nitro v3 + Vercel 平台组件的 iMessage agent 工程模板：用户向 Sendblue 号码发 iMessage，webhook 触发 Chat SDK 分发，由 Vercel Workflow 以可重试的 "use step" 单元编排 LLM 回复与回帖两步，经 Vercel AI SDK/AI Gateway 调用模型（改一个常量即可切换 Gemini/Claude/GPT/Grok 等），evlog 记录 token 用量、工具耗时与成本估算。开发需 Node 20+、Sendblue 账号与 ngrok 隧道，生产部署到 Vercel 或其他 Node 主机。

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

- generateReply 与 postReply 两步独立可重试，LLM 错误与发送失败互不影响
- 改一个 MODEL 常量即可切换 AI Gateway 支持的模型
- 工具调用（zod schema + execute）自动成为可重试可观测的 workflow step
- evlog 宽事件记录 token、工具耗时、成本，支持 Axiom/OTLP/Sentry 等多种 drain

## 适用场景

- 搭建通过 iMessage 对话的 AI 助手并部署到生产环境
- 学习 Vercel Workflow 持久编排与 Chat SDK 的组合用法
- 为 iMessage agent 接入自定义工具与可观测性后端

## 场景标签

`AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: - Vercel Workflow — durable orchestration with retryable `"use step"` units
> L28: 1. **`generateReply` step** — calls `generateText` against the Vercel AI Gateway. Tools registered in server/tools/

## 星数曲线

```mermaid
xychart-beta
    title "vercel-labs/nitro-imessage-agent-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8a687d2ddb12` · [字段定义](../../DATASET.md)*
