# LilithGames/a2wave

⭐ 27 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/LilithGames/a2wave) · [官网](https://a2wave.ai) · 组织维护 · 中文 README

**把既有 agent CLI 变成团队共享服务的编排平台**

面向企业内部团队的自托管平台：将 Claude Code、Cursor Agent、OpenAI Codex 等 agent CLI 转换为可共享、可治理的服务。用户用自然语言描述 Agent、绑定模型提供商、附加 Skills 与 MCP 服务器后，发布到飞书、Slack、Discord、Telegram、HTTP API、A2A 或定时触发等渠道。平台负责凭据注入、运行排队、审计、权限与交付，通过 Web 仪表盘管理。明确边界：不含 LLM 推理与沙箱运行时，执行来自底层 CLI；信任模型假定使用者是可信同事，不防御内部恶意 Agent。npm 全局安装后 a2wave setup 生成 docker-compose 部署。

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

- 自然语言描述 Agent，绑定模型提供商并发布到多渠道（飞书/Slack/Discord/Telegram/A2A 等）
- 凭据注入、运行排队、审计、每 Agent 权限与速率限制
- 通过 Skills 与 MCP 服务器（stdio/SSE/HTTP/代理组）组合式扩展
- 内置评测：冻结 provider/model/prompt 快照回放用例集

## 适用场景

- 把团队已在用的 agent CLI 开放给全组同事，经聊天渠道调用
- 为共享 Agent 配置权限、审计与运行队列
- 让 Agent 在真实 Git/Perforce 检出上工作并通过 HTTP API 或定时任务触发

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L21: a2wave turns the agent CLIs you already use — **Claude Code, Cursor Agent, OpenAI
> L26: and MCP servers, publish. a2wave handles credential injection, run queueing, audit
> L29: **a2wave orchestrates; it does not execute.** No bundled LLM inference, no sandbox

## 星数曲线

```mermaid
xychart-beta
    title "LilithGames/a2wave 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6dbc90955e25` · [字段定义](../../DATASET.md)*
