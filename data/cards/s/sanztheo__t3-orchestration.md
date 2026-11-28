# sanztheo/t3-orchestration

⭐ 3 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sanztheo/t3-orchestration) · [官网](https://github.com/sanztheo/t3-orchestration#readme) · 个人维护

**为 Claude Code 提供多 agent 编排：协调者+工作者+定时记忆**

一个 Claude Code 插件+mod+skills 组合，把 T3 Code 变成多 agent 工作区：协调者线程按主题开启工作者线程，工作者在回答结束时通过 Stop 事件向协调者自动发信号，协调者只在需要用户决策时打断。附带定时记忆线程（默认每 10 分钟）读取线程写入 SQLite 溯源笔记与知识页，支持多 Claude 账号的用量检查与调度。仅支持 Claude Code（Codex 等只有手动汇报协议），信号为 best effort、无重试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协调者/工作者模式，工作者结束回合自动通知，无轮询无循环
- 基于 T3 原生线程元数据的角色识别，不触碰手动线程
- 定时记忆线程：SQLite 溯源笔记、supersedes 修正、知识页
- 多 Claude 账号用量检查与调度，无 API key、无遥测

## 适用场景

- 在 T3 Code 中用一条对话并行推进多个编码任务
- 让多个 Claude 账号的周用量被充分使用
- 为项目维护带来源的长期记忆知识页

## 场景标签

`多智能体` `Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Run a whole project from one chat.** t3-orchestration turns T3 Code
> L93: A free, open-source Claude Code plugin that adds a coordinator/worker multi-agent workflow and an
> L126: - **Claude Code only** (see the FAQ).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `69ade4a340b2` · [字段定义](../../DATASET.md)*
