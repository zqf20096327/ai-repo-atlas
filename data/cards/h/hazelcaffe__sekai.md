# hazelcaffe/sekai

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/hazelcaffe/sekai) · 个人维护

**自托管多 AI agent 团队服务器：为个人与小组提供可管理记忆的群聊机器人**

自托管的开源聊天机器人平台：每台机器人有名称、人格与职位，维护自己的记忆与笔记，支持定时例程、群聊协作与操作前审批。模型可来自任意 OpenAI 兼容网关或 API 提供商，也可把已订阅的编码 agent 作为机器人模型。机器人可经 Slack、Discord、Signal、邮件、语音等渠道触达用户，并支持把编码任务分派给 Claude Code/Codex/OpenCode worker。基于 Bun 与 Postgres/pgvector，提供 Docker 部署与源码运行两种方式，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每机器人可独立配置模型、思考级别或 planner/council/fallback 组合策略
- 可视化记忆：下一轮读取的指令、记忆、笔记与历史可查看
- 编码 agent 式分级审批（只读/每次询问/审阅模型检查）与活动日志
- 50+ MCP 应用一键登录，Firecrawl Local 本地抓取为 Markdown

## 适用场景

- 为个人或小团队搭建自托管的多人 AI 助手服务
- 让多个机器人分派编码任务并实时监督、审批
- 机器人经 Slack/Discord/Signal/邮件/语音多渠道触达用户

## 场景标签

`多智能体` `聊天机器人` `AI 助手` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Your own team of AI agents, on your own server, for you and the people you invite.
> L14: Each bot has a name, a face, a job and a personality. It keeps its own memory and notes, runs routines on a schedul
> L16: OpenAI-compatible gateway or API provider (OpenAI, Anthropic, Gemini, OpenRouter, Ollama, LM Studio…), or use agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `aeadde8919be` · [字段定义](../../DATASET.md)*
