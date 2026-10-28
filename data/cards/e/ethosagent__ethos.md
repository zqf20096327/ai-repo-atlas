# ethosagent/ethos

⭐ 22 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ethosagent/ethos) · [官网](https://ethosagent.ai) · 组织维护

**TypeScript AI agent 框架：以人格为单位构建多平台运行的专业 agent 团队**

以 TypeScript 编写的 agent 框架，核心机制是将'人格'作为架构单位：默认内置 engineer/researcher/reviewer/coach/operator 五种人格，同一人格可跨 CLI、Telegram、Discord、Slack、Email 运行，共享记忆与会话。支持多人格团队通过看板、共享话题文件、审计轨迹等可见工件协作。提供 npm 全局安装的 CLI，配置 provider（Anthropic/OpenAI/OpenRouter/Ollama/本地 LLM），可作 MCP server 暴露给 Claude Desktop 等客户端。README 声明十三条安全边界保证并标注代码位置。macOS 桌面应用未签名，原生 Windows 非主要目标，需 WSL2 + Node 24+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种默认人格，同一身份跨 CLI/Telegram/Discord/Slack/Email 运行
- 团队通过看板、共享文件、审计轨迹等可见工件协作
- 可作 MCP server 暴露人格给 Claude Desktop、Cursor 等客户端
- 十三条安全保证清单，每条标注执行位置 file:line

## 适用场景

- 构建有明确职责边界的专业 AI agent 团队
- 在聊天平台长期运行常驻 agent 并保留记忆
- 从 OpenClaw 或 Hermes 迁移记忆、技能与密钥

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: Most AIs try to be good at everything. Ethos gives you a team — each one really good at just one thing.
> L107: |Architecture in 90 seconds|The 12-step `AgentLoop.run()` cycle, the four extension points, what's frozen vs. plug
> L111: |Building on Ethos — Quickstart|Write a tool, add a provider, build a channel adapter, publish a plugin. Ten minut

## 星数曲线

```mermaid
xychart-beta
    title "ethosagent/ethos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ca48c7904a17` · [字段定义](../../DATASET.md)*
