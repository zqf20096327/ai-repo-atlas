# 2witstudios/PurePoint

⭐ 27 · Swift · MIT · 推送 2026-10-24 · [GitHub](https://github.com/2witstudios/PurePoint) · [官网](https://PurePoint.dev) · 组织维护

**macOS 上并行管理多个编码 agent 的终端工作区**

面向 macOS 的 agent-first 编码工作区：以终端为命令中心，在隔离的 git worktree 中并行运行 Claude Code、Codex、OpenCode 等编码 agent，实时查看每个 agent 的分屏终端会话与逐文件 diff，可中途接管或终止。附带 `pu` CLI（21 个命令，支持 --json）实现 spawn/status/swarm/定时任务/事件触发等管理，桌面端仅限 macOS，daemon 与 CLI 也可跑在 Linux 服务器，另有 iPhone/iPad 远程查看应用。项目自述为早期活跃开发状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 10 个 agent 流式运行于 10 个隔离 worktree，实时 diff 与可中断接管
- `pu` CLI 提供 21 个命令（spawn/swarm/schedule/trigger/grid 等）并支持 --json
- 可运行 Claude Code、Codex、OpenCode 等不同 agent
- 支持 swarm 多 agent 扇出与定时调度

## 适用场景

- 并行派发多个编码任务并逐个监督改动
- 在一个界面里切换查看各 agent 的终端输出与 diff
- 定时或事件触发方式自动运行 agent 任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L12: Your attention is the bottleneck. Other platforms run headless agents in parallel — you get results, but you can't 
> L17: A terminal at your home directory where you run Claude Code, Codex, or OpenCode — whichever fits the job. Browse yo
> L21: **02 — A terminal built for agents.**

## 星数曲线

```mermaid
xychart-beta
    title "2witstudios/PurePoint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f49db0fc395f` · [字段定义](../../DATASET.md)*
