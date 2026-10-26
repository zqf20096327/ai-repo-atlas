# zebbern/agent-collab

⭐ 34 · JavaScript · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/zebbern/agent-collab) · 个人维护

**在 Claude Code 内调度 Codex/Cursor 后台干活的插件市场**

一个含三个插件的 Claude Code marketplace：codex 插件（openai/codex-plugin-cc v1.0.6 的非官方 fork，含 Windows 修复）把任务、review、rescue 委托给 OpenAI Codex CLI；cursor 插件驱动 Cursor 的 cursor-agent CLI（Windows 经 WSL 运行）；goal 插件做长程目标分解。共享后台 job 机制：进度感知 status、结果存储、resume 会话交接、所有权验证的 cancel。需 Node.js ≥20 与相应订阅，通过 /plugin 命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个插件分别对接 Codex CLI、cursor-agent CLI 与长程目标分解
- 后台 job：持久化 worker、跨会话 status/result 收取、resume 交接
- codex 插件为 openai/codex-plugin-cc v1.0.6 fork，含 Windows 修复与原子状态写入
- cursor 插件在 Windows 自动经 WSL 运行并翻译工作区路径

## 适用场景

- 在 Claude Code 会话中把修复或调查任务委托给 Codex/Cursor 后台执行
- 关闭会话后回来收取后台任务结果并继续
- 用对抗性 review 命令挑战自己的设计决策

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Delegate work from Claude Code to other AI coding agents.**
> L5: Run Codex and Cursor as background workers inside Claude Code — reviews, tasks, and rescues with tracked jobs, live 
> L29: The codex and cursor plugins share the same job chassis: background jobs with progress-aware `status`, stored `resu

## 星数曲线

```mermaid
xychart-beta
    title "zebbern/agent-collab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b2f5d039cdd7` · [字段定义](../../DATASET.md)*
