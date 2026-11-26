# pizza-bot-app/pizza-bot

⭐ 578 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/pizza-bot-app/pizza-bot) · [官网](https://github.com/pizza-bot-app/pizza-bot/releases) · 组织维护

**给开发者的长时 AI 任务本地收件箱与审批队列**

本地优先的桌面/浏览器/CLI 应用，将长时运行的 agent 任务组织为收件箱模式：完成的工作进入 Unread 队列，需要人工批准的决策进入 Action 队列。运行带有检查点，客户端断开后 api-server 继续执行任务；支持 cron 与 webhook 触发。通过 Settings > Providers 配置多家模型供应商；以 MCP 服务器、Agent Skills 和插件扩展。Apache-2.0 许可，在 Amazon 内部开发后开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 断开后任务继续运行，检查点化且可由 cron/webhook 触发
- 人工审批队列与长期记忆、桌面通知内置
- 支持 11 家模型供应商，含 Amazon Bedrock 与 Ollama
- Electron 桌面、浏览器与 CLI 三种前端共用同一 api-server

## 适用场景

- 启动后台 agent 任务后离开，回来查看已完成结果
- 对关键操作设置人工批准关卡
- 在本地以收件箱方式管理多个并行 agent 会话

## 场景标签

`AI 助手` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An inbox for long-running AI work.
> L45: - **Bring your model provider.** Amazon Bedrock, Anthropic, Google Gemini,
> L97: A running api-server needs access to at least one model provider; HTTP clients


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0bec5acbc2d8` · [字段定义](../../DATASET.md)*
