# GantisStorm/essentials-claude-code

⭐ 90 · Unlicense · 推送 2026-02-15 · [GitHub](https://github.com/GantisStorm/essentials-claude-code) · 个人维护

**Claude Code 插件：以循环/蜂群/团队三模式执行带退出准则的任务**

基于 Claude Code 内置 Task System（v2.1.19+）的工作流插件，提供三种执行模式：Loop 顺序执行、Swarm 以队列并行生成子代理（默认 3 并发）、Team 在 tmux 面板中生成完整 Claude Code 实例并采用契约优先协调。计划文件定义退出准则与依赖图，转换器生成 prd.json 或 beads 格式，任务状态持久化于 ~/.claude/tasks/ 并支持跨会话。声明零外部依赖；Team 模式需 tmux 与实验环境变量。通过 /plugin 命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Loop/Swarm/Team 三种执行模式，均强制退出准则（测试通过才算完成）
- 依赖图驱动的任务系统：blockedBy 依赖、ctrl+t 可视化进度、跨会话持久化
- 转换器生成 prd.json（dependsOn）或 beads（epic→task）执行格式
- Team 模式由 lead 定义集成契约（API URL/JSON 形状/状态码）并做契约 diff 与端到端验证

## 适用场景

- 让 AI 编码循环执行直到测试全部通过
- 把独立任务分派给并行子代理以蜂群模式执行
- 前后端等多组件构建中用团队模式对齐接口契约
- 跨会话追踪与恢复任务列表

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Loops, swarms, and teams powered by Claude Code's built-in Task System.**
> L46: Our loop, swarm, and team commands use Claude Code's **built-in Task Management System** (v2.1.19+).

## 星数曲线

```mermaid
xychart-beta
    title "GantisStorm/essentials-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-29 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f653a7c1838c` · [字段定义](../../DATASET.md)*
