# DomaAI/Codo

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/DomaAI/Codo) · 组织维护

**给已有付费 coding agent 与 API 的开发者：一个终端里接通所有模型**

终端与应用形态的 agent 运行器：在同一个对话中驱动用户已订阅的 Claude Code、Codex、Gemini CLI、ACP agent、任意 OpenAI 兼容 `/v1` API 或本地模型；某一订阅计划达到限额时，携带完整历史、文件与计划自动切换到下一个模型继续同一回合。提供 agent 团队（各自 git 副本、评审、PR）、跨提供方 agent 分组（并行、交叉评审、投票）、马拉松模式与 systemd/launchd 常驻 agent，可经 Telegram、Discord、Slack、邮件等渠道应答。单 Python 文件实现，依赖 Python 3.9+，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 订阅限额到达时同一对话自动切换到下一个计划、API key 或本地模型
- 接入 Claude Code、Codex、Gemini CLI、20+ ACP agent、任意 `/v1` API 与本地模型
- agent 团队各自在独立 git 副本工作，评审通过后 `apply --pr` 开 PR
- 每次编辑有备份，`/undo` 撤销、`/diff` 查看变更

## 适用场景

- 多个 AI 订阅计划之间自动接力，避免在限额处等待
- 让多个 agent 分工协作并在独立分支上完成、评审、合并代码
- 在服务器上常驻 agent，通过 Telegram/Slack/邮件等接收任务
- 同一目标在 Claude、Codex、Gemini 之间并行或对比运行

## 场景标签

`编码 Agent` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6:  Claude Code, Codex, Gemini CLI, any API or a local model in one app and one terminal.
> L66: - **Never stuck on a plan limit.** Claude Code ran out? The turn moves to Codex, Gemini, your API key
> L187: |Models|OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek, Groq, OpenRouter, Ollama, LM Studio, any `/v1` URL, sev


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f5f72371c236` · [字段定义](../../DATASET.md)*
