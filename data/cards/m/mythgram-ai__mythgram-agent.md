# mythgram-ai/mythgram-agent

⭐ 23 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/mythgram-ai/mythgram-agent) · [官网](https://mythgram-ai.github.io/mythgram-agent/) · 组织维护

**可自托管的通用个人 AI agent 工作台：聊天、工具执行与自动化**

Mythgram Agent 是一个本地运行的通用 AI 助手与执行型 agent 工作区：TypeScript/Express 后端承载 agent 运行时、调度器与 SQLite 持久化，React/Vite 前端提供浏览器控制台。支持 ReAct 式流式工具调用、文件读写与 shell 执行、网页搜索抓取、多 agent 团队、持久记忆与知识库、MCP/Composio 集成、定时任务与 Telegram/Discord/Slack 消息通道。模型可接托管服务商、本地模型服务器或自定义 OpenAI 兼容端点。限制：后端无认证层，需在可信环境运行；根目录 Dockerfile 为失效脚手架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 式流式 agent 聊天，支持停止/恢复与事件历史持久化
- 工作区工具：文件读写编辑、shell 执行、搜索、网页抓取、检查点
- 多 agent 团队与协调者 agent、可复用技能/提示词库
- 持久记忆与知识库、后台记忆 agent、上下文自动摘要与滑窗截断
- MCP 服务器与 Composio 应用连接器、定时任务与消息通道

## 适用场景

- 在自己的机器上运行一个能编辑文件、执行命令的个人 AI agent 工作台
- 让 agent 通过 Telegram/Discord/Slack 处理消息或按计划自动执行任务
- 接入自选的托管或本地模型，自主配置 agent 与团队

## 场景标签

`AI 助手` `多智能体` `提示工程` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: Mythgram AI is a general-purpose AI assistant and action-taking agent workspace—not just a coding chatbot. It can he
> L5: The browser-based console, **frontend-main**, brings chat and workspace management together: configure agents and mo
> L11: - **Streaming agent chat:** ReAct-style tool use, live reasoning/output events, stop and resume behavior, and persi

## 星数曲线

```mermaid
xychart-beta
    title "mythgram-ai/mythgram-agent 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-26 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `60a6683d8b8b` · [字段定义](../../DATASET.md)*
