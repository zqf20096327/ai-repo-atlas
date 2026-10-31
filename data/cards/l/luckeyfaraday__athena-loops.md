# luckeyfaraday/athena-loops

⭐ 60 · Python · MIT · 推送 2026-07-08 · [GitHub](https://github.com/luckeyfaraday/athena-loops) · 个人维护

**后端无关的 Python AI agent 编排循环框架，供开发者构建确定性任务循环**

agentloop 是一个轻量级 Python 多 agent 编排框架，将 orchestrator→worker→reviewer 模式实现为确定性代码骨架：目标分解为子任务、分发到 worker 子 agent、聚合后经审查门循环直至满足成功标准。通过单一 Agent 接口驱动任意 LLM 后端（Anthropic Claude、Claude Code、Codex、opencode、aider、xAI Grok），并以 MCP 服务器与 CLI 两种形式暴露，供 Claude Code、Cursor 等 MCP-aware agent 调用。控制流写在代码中、模型判断放在可替换的提示词里；支持隔离 worktree、每轮迭代检查点提交、verify_commands 确定性校验与分离式后台运行。安装方式为 pip install -e 源码安装，无运行级系统依赖（MockAgent 零依赖）。

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

- orchestrator→worker→reviewer 确定性循环，单一 Agent 接口驱动多后端
- 同时以 MCP 服务器（orchestrate/status/tail/result 等工具）与 CLI 形式提供
- 隔离 git worktree 运行，每轮迭代自动检查点提交，部分工作不丢失
- verify_commands 在每轮 worker 迭代后运行真实命令并将失败反馈进下一轮

## 适用场景

- 用循环代替手写提示词驱动 Claude Code/Codex/aider 等 coding agent 完成任务
- 让 MCP-aware agent（Claude Code、Cursor 等）通过 MCP 工具调用编排循环
- 在隔离 worktree 中自动分解、执行、审查并验证代码任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **agentloop** is a lightweight Python framework for multi-agent orchestration. It
> L10: loop drives any LLM backend — Anthropic Claude, Claude Code, Codex, opencode, or
> L160: **Outward — a coding agent *calls* the loop.** An MCP server exposes the loop as a

## 星数曲线

```mermaid
xychart-beta
    title "luckeyfaraday/athena-loops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-31 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ca9cb1abe4f8` · [字段定义](../../DATASET.md)*
