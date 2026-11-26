# theselfruleorg/polyrob

⭐ 13 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/theselfruleorg/polyrob) · [官网](https://polyrob.dev) · 组织维护

**自托管自主 AI agent：在其机器上持续追求目标并学习**

自托管的自主 AI agent：用户以自然语言下达任务或常驻目标，agent 自行规划步骤，调用工具（web、文件、代码、shell、邮件、MCP 服务器），从错误中恢复并汇报结果。交互面包括终端、Web 控制台、REST API 及 Telegram 等聊天应用。agent 循环与 LLM 层为原生代码实现（不依赖第三方 agent 框架），记忆与状态存于本地 SQLite；带目标板、定时任务、步骤/花费上限、审批队列、子 agent 最小权限与 shell 命令分级等安全机制。钱包与加密功能为可选模块且代码未经独立审计。MIT 许可。

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

- 常驻目标板与定时任务（cron/间隔语法），跨会话记忆与自写技能（编辑需隔离审查）
- 内置工具：web_fetch、Playwright、shell、git/GitHub、MCP 客户端与子 agent
- 多聊天面接入：Telegram、邮件、WhatsApp、Discord、Slack、Feishu/Lark、DingTalk 等
- 安全机制：不可信输入框定、步骤/花费上限、审批卡、最小权限子 agent、shell 命令分级

## 适用场景

- 在自己服务器上运行一个持续在消息间隙干活的个人 agent
- 让 agent 执行定时任务并自动跟进未完成工作
- 通过 Telegram/邮件等聊天应用远程指挥家中/服务器上的 agent

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13: POLYROB is an AI agent you run yourself. Give it a task or a standing goal in plain language: it
> L14: plans the steps, uses tools (web, files, code, a shell, mail, MCP servers), recovers from its own
> L19: their own box. The agent loop and the LLM layer are native code (no third-party agent framework),


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1cd5bbbf18db` · [字段定义](../../DATASET.md)*
