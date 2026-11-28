# arjunkshah12345-hash/tandem

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/arjunkshah12345-hash/tandem) · 个人维护

**自托管主动式 AI 助手：晨报、后台任务与发送前审批**

以 Node 运行的自托管主动式 AI 助手，提供晨间简报、定时 check-in、cron 例程、后台任务、可编辑 artifacts 与浏览器操作，发送/支付/签名/删除类操作须经用户审批。模型可自由选择（Anthropic/OpenAI/Gemini/OpenRouter 等及 Ollama 等本地运行时），数据存于单个 SQLite 文件。需要 Node 22.13+，通过 git clone 源码或 Docker 部署，支持 PWA 与 Telegram 审批。README 标注为早期发布版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 主动式交互：晨报、定时 check-in 与 cron 例程
- 工具调用经过 8 步 gate（校验、限额、敏感数据扫描、审批等）
- 支持任意 MCP 服务器连接器及内置 IMAP/SMTP、ICS
- 分工作/分流双模型路由与按日后台预算控制

## 适用场景

- 个人自托管一个能主动发消息提醒的 AI 助手
- 让助手处理邮件、日历等后台任务并在关键操作前审批
- 用本地模型（Ollama/vLLM）运行保持数据私有

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3:  An open-source, self-hosted, proactive AI assistant. Works with any model.
> L10: - **Tasks that run in the background.** Hand off longer jobs. Tandem works through them, asks when it's stuck, and 
> L44: ## Quick start


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9d9f95909fba` · [字段定义](../../DATASET.md)*
