# spencermarx/orc

⭐ 27 · Shell · 推送 2026-06-21 · [GitHub](https://github.com/spencermarx/orc) · 个人维护

**把一个提示分派为多 AI 编码代理团队的编排框架**

基于本地 Agentic CLI（Claude Code、OpenCode、Codex、Gemini CLI）之上的轻量编排层：以 tmux 为运行环境，将用户提示分解为 goal 与 bead 工作项，为每个工程师代理分配隔离 git worktree，经计划、分解、派发、构建、两级评审、交付（推分支/建 PR）的固定生命周期执行。支持根/项目/goal 三层 orchestrator 层级与多项目协调，各阶段用 TOML 自然语言配置，无守护进程。需预装 Beads(bd)、tmux、git、bash 3.2+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- goal→bead 两级分解，每个工程师在隔离 git worktree 中并行工作
- Investigate→Plan→…→Deliver 可配置生命周期，含两级评审与交付钩子
- 支持 Claude Code / OpenCode / Codex / Gemini CLI，auto 检测已装 CLI
- 基于 tmux 的 TUI：命令面板、窗口树、面包屑与斜杠命令协调

## 适用场景

- 让多个编码代理并行完成一个功能的不同子任务
- 在隔离工作区中运行代理避免合并冲突
- 跨多个本地项目统一分派与监控 AI 代理工作

## 场景标签

`编码 Agent` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Turn one prompt into a team of AI agents that plan, build, review, and ship.
> L75: |Agent CLI|Your AI coding agents — `auto` detects what's installed|Claude Code, OpenCode, Codex, or Gemini CLI|
> L147: Investigate -> Plan -> Decompose -> Dispatch -> Setup -> Build -> Review -> Deliver

## 星数曲线

```mermaid
xychart-beta
    title "spencermarx/orc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-31 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d664fc955b81` · [字段定义](../../DATASET.md)*
