# jhd3197/CachiBot

⭐ 21 · Python · MIT · 推送 2026-03-04 · [GitHub](https://github.com/jhd3197/CachiBot) · [官网](https://cachibot.ai) · 个人维护 · 中文 README

**可视化多 agent 平台：构建、部署与审计 AI 机器人**

自托管的 AI agent 平台，含可视化仪表盘：可创建多个带自定义系统提示与逐 bot 模型路由的专用 bot，在协作房间中以 9 种响应模式（并行、链式、辩论等）运行；通过能力开关门控插件系统，提供沙箱 Python 执行（AST 风险评分）、工作区隔离与审计日志。支持 14 家 LLM 提供商接入、7 个消息平台部署适配器、知识库 RAG、语音对话，并暴露 OpenAI 兼容 API。面向需要构建和监控 AI bot 的开发者与团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 bot 协作房间，9 种响应模式（并行/链式/辩论/共识等）
- 沙箱 Python 执行：AST 风险评分 + 导入限制 + 审批流
- 14 家 LLM 提供商支持，含 Ollama/LM Studio 本地模型
- 7 个消息平台适配器（Telegram/Discord/Slack/Teams 等）
- 暴露 OpenAI 兼容 /v1/chat/completions API

## 适用场景

- 构建客服 bot 并部署到 Telegram/Discord 等平台
- 搭建多 bot 协作房间做数据分析或内容生产流水线
- 自托管一个带审批流和审计日志的可控 agent 平台
- 把自有 bot 作为 OpenAI 兼容 API 供 Cursor 等工具调用

## 场景标签

`多智能体` `聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L39: **CachiBot gives you all three.** Build specialized bots, deploy them to any messaging platform, run them in collab
> L119: - **Unlimited Specialized Bots** — Create bots with custom system prompts, per-bot model routing, capability toggl
> L195: CachiBot exposes `/v1/chat/completions` and `/v1/models` endpoints, so external tools like Cursor or VS Code exten

## 星数曲线

```mermaid
xychart-beta
    title "jhd3197/CachiBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5018b212f1ad` · [字段定义](../../DATASET.md)*
