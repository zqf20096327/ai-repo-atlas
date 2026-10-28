# AgriciDaniel/ace-claude-code

⭐ 27 · PowerShell · MIT · 推送 2026-04-10 · [GitHub](https://github.com/AgriciDaniel/ace-claude-code) · [官网](https://agricidaniel.com) · 个人维护

**Claude Code 的多 agent 编排层：并行执行与会话持久化**

运行于 Claude Code 之上的编排配置项目：由 3 个 Team Lead（Alpha/Beta/Gamma）并行执行任务，各 Team Lead 可继续生成子 agent；通过文件区（Zone）归属避免 agent 间文件冲突，每任务自动生成一次 git 提交，状态持久化以支持会话间恢复。用户以自然语言描述需求即可路由，也可使用 /ace: 前缀的斜杠命令管理项目生命周期、阶段计划、进度与会话。安装方式为 git clone 仓库或复制 .ace 目录与 CLAUDE.md 到项目根。要求已安装 Claude Code CLI、Git 与 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 个 Team Lead 并行执行，可生成不限数量的子 agent
- 每任务一次原子 git 提交，带可追溯性
- 会话持久化，支持暂停/恢复与任务级续接
- 自然语言路由触发工作流，辅以 /ace: 斜杠命令集

## 适用场景

- 在 Claude Code 中用多 agent 并行推进开发任务
- 大型项目按阶段（roadmap→phase→plan）组织构建
- 跨会话保存进度并在之后恢复继续开发

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L14: Ace is an orchestration layer for Claude Code that enables:
> L188: - Claude Code CLI

## 星数曲线

```mermaid
xychart-beta
    title "AgriciDaniel/ace-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6fe164a21cda` · [字段定义](../../DATASET.md)*
