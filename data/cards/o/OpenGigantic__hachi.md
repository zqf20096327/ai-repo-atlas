# OpenGigantic/hachi

⭐ 12 · Python · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/OpenGigantic/hachi) · [官网](https://github.com/OpenGigantic/hachi) · 组织维护

**受治理的个人 AI agent：能力以可审计的 .og 文件运行**

一个 Python 3.11+ 的个人 agent 运行时，将每个能力（含自我学习的技能）封装为类型化、带版本与权限范围的 .og 文件，可 lint 与审计。ReAct 循环在 LLM 调用之间强制执行每会话与每回合的 token/成本上限；shell、路径、URL 与记忆写入在源码层通过 call-time 权限门槛把关。内置 31 个技能、62 个工具，支持 TUI、REST+SSE 网关、React Web UI、多聊天渠道与 OpenAI 兼容接口。状态为 pre-release，需从源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- .og 格式：类型化节点图，带 semver、changelog 与可执行断言
- 每会话与每回合的成本/token 上限在调用间强制执行
- 权限分层（sandbox/guided/unrestricted）与 SSRF 守卫、OS keyring 凭据
- 支持 TUI、FastAPI 网关、Web UI 及 Telegram/Slack/Discord/WhatsApp 渠道

## 适用场景

- 限制个人 agent 的 token 开销与自主行为
- 以可审计文件形式管理 agent 技能库
- 通过本地网关与多渠道接入个人 agent

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L15: Every capability the agent has — or teaches itself — is a typed, versioned, lintable,
> L44: |**Surfaces**|Textual TUI · FastAPI gateway (REST + SSE) · React web UI · Telegram / Slack / Discord / WhatsApp · O
> L45: |**Models**|Anthropic · OpenAI-compatible · OpenRouter · Groq · DeepSeek · Gemini · local Ollama|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `c76c0499fbae` · [字段定义](../../DATASET.md)*
