# warp-context/rightStage

⭐ 339 · Shell · MIT · 推送 2026-09-07 · [GitHub](https://github.com/warp-context/rightStage) · [官网](https://github.com/warp-context/rightStage) · 个人维护 · 中文 README

**跨终端窗口同步 AI 上下文的三个 shell 脚本工具**

由 progress.md、ai_inject、ai_progress、ai_done 组成的纯 shell 方案：项目内维护一份 .ai/progress.md 任务清单，ai_inject 自动从 git 提交记录推导任务状态并拼装 100 行以内的上下文块，供复制粘贴给任意 AI 工具（Warp AI、Claude、ChatGPT、Cursor 等）；无守护进程、无服务器、无配置。面向在多终端窗口工作并频繁向 AI 提供上下文的开发者，支持 macOS/Linux/Windows Git Bash，curl 脚本一键安装。另有 Rust 移植被提议为 Warp 内置功能（处于 issue 阶段）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- progress.md 作为唯一状态源，多窗口读取同一文件天然同步
- ai_inject 自动拼装 <100 行上下文块并可复制到剪贴板
- 任务状态从 git commit 消息自动推导，无需手动维护
- 无守护进程、无服务器、无配置，仅三个 shell 脚本

## 适用场景

- 换终端窗口后快速恢复当前任务上下文
- 把项目状态一键拼装并粘贴给 Claude/ChatGPT/Cursor 等 AI 工具
- 通过带编号的 git commit 自动推进任务状态

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L9: **aiflow** keeps your AI context in sync across every terminal window. Drop a `progress.md` in your project — any wi
> L73: Generates the minimal context block to paste into your AI.

## 星数曲线

```mermaid
xychart-beta
    title "warp-context/rightStage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 338 --> 340
    line [339, 339]
```

2026-10-18 339 → 2026-10-22 339（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2962e2b6c630` · [字段定义](../../DATASET.md)*
