# EzinsightsInc/EzCoworker

⭐ 26 · Python · NOASSERTION · 推送 2026-03-28 · [GitHub](https://github.com/EzinsightsInc/EzCoworker) · 组织维护

**自托管多用户 AI agent 平台：Docker 隔离运行 Claude Code CLI**

基于 Claude Code CLI 的多用户自托管 AI agent 平台（社区版），由 ezinsights.ai 维护，采用 IBU-1.0 许可证，内部商业用途免费。每个 agent 迮行在独立的 Docker 容器中，数据留在用户自有服务器。支持 6+ LLM 提供商（Ollama 本地、Anthropic、OpenAI、Gemini、Groq、OpenRouter），启动时自动发现 22 个模型，支持 MCP 工具与 LiteLLM。通过 git clone 加 Docker 快速启动，含 Admin 模块与前后端服务。企业版另提供数据智能与 SDLC 自动化套件，需联系销售。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个用户独立 Docker 容器隔离运行 agent
- 6+ LLM 提供商接入，启动时自动发现 22 个模型
- MCP 工具支持与 LiteLLM 网关
- Admin 模块与多渠道集成（Slack/Teams/Discord 等，企业版）

## 适用场景

- 在企业自有服务器上部署多用户 AI agent 工作台
- 结合本地 Ollama 模型实现数据不出内网的 agent 运行
- 通过 Admin 模块查看 agent 运行状态与可观测性

## 场景标签

`模型网关` `多智能体` `编码 Agent` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L7: A powerful self-hosted AI agent platform powered by **Claude Code CLI** — free for internal business use.
> L31: ✓  Any LLM — Ollama local, Anthropic, OpenAI, Gemini, Groq, OpenRouter

## 星数曲线

```mermaid
xychart-beta
    title "EzinsightsInc/EzCoworker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `288f94fd6df7` · [字段定义](../../DATASET.md)*
