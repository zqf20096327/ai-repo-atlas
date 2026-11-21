# anton-abyzov/specwithcode

⭐ 5 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/anton-abyzov/specwithcode) · [官网](https://spec-weave.com/code/) · 个人维护

**一个桌面应用统一管理多个编码 Agent 并跨供应商续接任务线程**

Electron 桌面应用与可选本地服务器，把 Claude Code、Codex、Copilot 等编码 Agent 汇集到一个窗口并行运行：协调者将目标拆分为工作线程，各自使用独立的供应商、模型和 git worktree，并以 PR 形式交付。核心机制包括跨供应商的用量限额监控与线程回退续接（保留历史）、多机配对（局域网/SSH/Tailscale）、以及规格与验收证据以文件形式存入 git 仓库。提供 macOS/Windows/Linux 安装包，MIT 许可，需自带已有 Agent 的账号或 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协调者拆分目标为多任务，各 worker 使用独立供应商/模型/git worktree 并报告 PR
- 供应商限额用尽时按项目规则将线程移交另一供应商并保留近期历史
- 多机配对：本地网络、SSH 或 Tailscale 连接 Mac/Windows/Linux 机器
- 规格、验收标准与任务证据以 SpecWeave 增量文件存于 git

## 适用场景

- 同时管理已付费的多个编码 Agent 并行处理任务
- 一个账号达到限额时自动切换到另一供应商续接线程
- 在多台机器上调度编码 Agent 工作线程
- 将任务规格与完成证据版本化保存在代码仓库中

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5:  One desktop app for Claude Code, Codex, Copilot and your other coding agents. Run tasks side by side on your own ma
> L44: You already pay for Claude Code, Codex or Copilot. SpecWithCode is one free, open-source (MIT) window that runs the
> L47: - **Never stuck on a limit.** Every account's usage on one screen. When a provider runs out, a per-project rule mov

## 星数曲线

```mermaid
xychart-beta
    title "anton-abyzov/specwithcode 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-20", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `9651ded1c32b` · [字段定义](../../DATASET.md)*
