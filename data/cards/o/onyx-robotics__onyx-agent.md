# onyx-robotics/onyx-agent

⭐ 69 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/onyx-robotics/onyx-agent) · [官网](https://www.onyxresearch.ai/) · 组织维护

**用大规模 AI agent 团队在你的代码库上自动做改进研究的 CLI 工具**

面向机器人/控制系统等硬件相关代码仓库的自动化研究工具：通过编排多个编码 agent 工作进程，按用户设定的目标、指标与可编辑范围批量运行实验，每个实验是一个带指标和元数据的 git commit，结果可转为 PR。提供 CLI 与 /onyx 技能两种入口，支持 Claude Code、Codex、OpenCode 作为工作 agent 及自定义 harness；支持实验数量/时长上限与工作进程动态扩缩。通过 sandbox.json 配合 bubblewrap/Seatbelt 做操作系统级沙箱隔离。macOS/Linux 原生支持，Windows 仅限 WSL2（需 0.1.20+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 并行实验编排，每个实验为带指标的 git commit，可转为 PR
- 内置 Claude Code / Codex / OpenCode 启动器与自定义 worker 接口
- bubblewrap(Linux)/Seatbelt(macOS) OS 级沙箱与 Landlock 执行路径限制
- 会话可设 --experiments/--max-minutes 上限，并支持 onyx research scale 动态扩缩工作进程

## 适用场景

- 在自己的仓库上让 AI agent 团队批量探索代码改进并生成可审查的 PR
- 对控制系统/机器人代码做自动超参数与控制器方案研究
- 以受限范围与沙箱隔离方式运行多个并行编码 agent 实验

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Use large-scale AI agent teams to rapidly discover code improvements on your hardware systems.
> L28: Onyx includes a CLI, but the intended interface is to use onyx with your coding agent, via the `/onyx` skill includ
> L65: Onyx uses a mix of deterministic CLI/processes with agents to keep research consistent, and results durable across 

## 星数曲线

```mermaid
xychart-beta
    title "onyx-robotics/onyx-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-28 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9688ae1ae273` · [字段定义](../../DATASET.md)*
