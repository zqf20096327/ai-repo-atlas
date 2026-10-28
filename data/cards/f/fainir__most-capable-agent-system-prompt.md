# fainir/most-capable-agent-system-prompt

⭐ 878 · MIT · 推送 2026-10-27 · [GitHub](https://github.com/fainir/most-capable-agent-system-prompt) · 个人维护

**让编程 Agent 自建自我改进 Agent 系统的系统提示词**

一段约 2,950 行的纯文本系统提示词（MIT 许可），用户粘贴给 Claude Code、Codex、Cursor 等编程 Agent，指示其立即在工作区搭建一套持久化、自我改进的 Agent 系统：文件式项目操作系统、任务图、验证流程、分层记忆、eval 与模型路由等。支持包裹现有 Agent 的 harness-wrapper 模式和基于 Agent SDK 从零构建的 native runtime 模式，可通过首条消息、系统提示词或 AGENTS.md 方式注入。限制：依赖具备文件读写与命令执行能力的强 Agent 模型，建议在受控环境中运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件纯文本提示词，约 2,950 行 / 约 23,000 tokens
- 指示 Agent 搭建任务图、文件式记忆、验证与自我改进循环
- 支持 harness-wrapper 与 native runtime 两种构建模式
- 兼容任意能读写文件并执行命令的编程 Agent

## 适用场景

- 让 Claude Code/Codex/Cursor 在空目录中自建长期任务系统
- 为多月的软件工程或研究项目搭建持久化 Agent 工作流
- 通过追加自定义约束块定制构建行为

## 场景标签

`Agent 框架` `提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: A copy-paste system prompt for people who use coding agents like Claude Code, Codex, or Cursor: paste it in, and you
> L7: Left alone, most agent sessions forget everything between runs, call work done without checking it, and stall once a


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `89f38826ada0` · [字段定义](../../DATASET.md)*
