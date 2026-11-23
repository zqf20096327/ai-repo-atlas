# win4r/runwright

⭐ 6 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/win4r/runwright) · 个人维护 · 中文 README

**给 LLM agent 提供持久运行、审批与花费上限的自托管运行时**

自托管的 agent 运行时平台，在模型循环之外补充四类机制：持久化运行（每步写入 SQLite 日志，崩溃后从最后完成步骤恢复）、控制（工具 allow/ask/deny 策略、人工审批、花费/调用/轮次上限）、学习（运行后提交笔记与技能，经评分版本化后供下次运行使用）、类型化工作流（确定性文档替代开放式循环）。附带 HTTP API、CLI、TypeScript 客户端、Web 控制台、cron 与签名 webhook 触发器。数据存于单个 SQLite 文件，无运行时依赖，需 Node.js 22.18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 持久化运行：进程中断后从最后完成步骤恢复，已完成步骤不重复执行
- 工具策略与人工审批：allow/ask/deny、待办列表、花费上限暂停机制
- 检查式学习：运行后提案经代码检查与评分，版本化后供后续运行使用
- 类型化工作流：支持决策阈值、分支、有界循环与子工作流

## 适用场景

- 需要 agent 运行可在崩溃后恢复、不丢进度的自托管部署
- 运行中需要人工审批关键工具调用的团队流程
- 按花费上限控制 agent 运行成本的场景
- 将可重复任务写成确定性工作流而非开放式循环

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L8: Runwright is a self-hostable platform that wraps LLM agents with the parts an agent loop does not give you on its
> L10: interface (Anthropic Messages, any OpenAI-compatible Chat Completions server, or a deterministic offline
> L178: - **One store, one journal per run.** Agents, revisions, runs, commands, pendings, usage, learning items, triggers


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `a4890c4f992b` · [字段定义](../../DATASET.md)*
