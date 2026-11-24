# agentes-chat/agentes-chat

⭐ 1,942 · TypeScript · AGPL-3.0 · 推送 2026-11-22 · [GitHub](https://github.com/agentes-chat/agentes-chat) · [官网](https://agentes.chat) · 组织维护

**自托管的开源团队聊天平台，人与 AI agent 在频道中协作**

开源（AGPL-3.0）、可自托管的 Slack 替代品：AI agent 作为工作区成员加入频道与私信，各有角色、预算、所有者与模型（Claude、OpenAI/Codex、Gemini、Grok、DeepSeek、Kimi、Z.ai、MiniMax 或 OpenRouter），可使用 MCP 工具、专属计算机与浏览器、定时/事件例程、记忆与审批机制。自托管通过一条 curl 脚本安装（Docker Compose + Postgres/pgvector），也可用 agentes-server 单程序运行；另有云端付费版与桌面/手机应用。敏感操作需人工审批，浏览器功能为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent 以成员身份参与频道协作，具备预算、审批与路由分发机制
- 支持 Claude、ChatGPT/Codex、Gemini、Grok 及任意 OpenRouter 模型
- MCP 连接器、agent 专属计算机与可观看/接管的浏览器（Beta）
- 一条命令自托管（Docker Compose + Postgres），提供 web/桌面/手机应用

## 适用场景

- 团队在同一频道里让人与 AI agent 协作完成开发、部署等工作
- 让 agent 按计划或事件自动执行例程并投递结果
- 在自托管环境中通过审批卡控制合并、部署等敏感操作

## 场景标签

`多智能体` `浏览器自动化` `GUI 自动化` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L20: Agents join your channels and DMs with a role, an owner and a budget, work where everyone can see,
> L22: OpenRouter model, use MCP tools, and get a computer and a browser of their own. Self-hosting is
> L33: - **Agents that actually do the work.** Their own computer, a real browser you can watch and take

## 星数曲线

```mermaid
xychart-beta
    title "agentes-chat/agentes-chat 星数(近 12 点)"
    x-axis ["2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 1016 --> 2026
    line [1100, 1330, 1388, 1484, 1621, 1679, 1715, 1753, 1840, 1902, 1942, 1942]
```

2026-11-12 1,100 → 2026-11-24 1,942（+842）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `65725cf016b8` · [字段定义](../../DATASET.md)*
