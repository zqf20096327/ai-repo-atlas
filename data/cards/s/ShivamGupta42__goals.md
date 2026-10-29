# ShivamGupta42/goals

⭐ 17 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/ShivamGupta42/goals) · 个人维护

**让 AI agent 长时间运行也能按计划完成目标的工作流插件**

面向 Claude Code 与 Codex 的开源插件加 CLI：在 agent 原生 /goal 循环之上增加可持久化的计划、逐步执行证明、决策记录与用户偏好记忆（~/.goals/user/ 下可手编的 Markdown 文件）。步骤须检查实际运行通过才算完成，支持 token 预算与重试上限的停止门（GOALS_ENFORCE），可从 URL/文件导入循环模板并验证。状态以纯文件存于用户仓库，可跨 /clear 与新会话恢复，也可交给其他 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 步骤须检查实际运行通过才算完成，提供执行证明
- 决策记录与用户偏好以可手编的 Markdown 文件形式存储
- opt-in 停止门：阶段重试上限与 token 预算，防止长跑失控
- 从 URL/文件导入循环模板并验证后激活

## 适用场景

- 让 Claude Code 或 Codex 长时间运行完成一个完整目标并保留进度
- 跨会话恢复被打断的 agent 任务计划与决策历史
- 用 token 预算和重试上限约束长跑 agent 的成本

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Goals is an open-source plugin for Claude Code and Codex that helps an AI agent
> L62: Goals runs the **workflow**; your AI assistant (Claude Code, Codex, …) does the **work**.
> L65: Under the hood it's a small **CLI plus a plugin**, working over **plain files in

## 星数曲线

```mermaid
xychart-beta
    title "ShivamGupta42/goals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `793e1cb1c8c3` · [字段定义](../../DATASET.md)*
