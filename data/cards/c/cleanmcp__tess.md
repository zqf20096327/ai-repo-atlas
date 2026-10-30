# cleanmcp/tess

⭐ 15 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/cleanmcp/tess) · 组织维护

**macOS CLI：为多个 AI 编码代理分配独立 git worktree 并统一管理**

面向 macOS 开发者的终端工具：每个任务创建隔离的 git worktree 并在其中派生 AI 编码代理，提供 spawn/status/tell/ship 六条核心命令查看与调度全部会话，ship 完成测试→推送→PR→清理流程。通过 tess wire 向 Claude Code、Cursor、Codex、Gemini、opencode 安装技能并拦截原生 git worktree。另含本地访问 Mac 信息/邮件/日历/通话等 12 个连接器，以及笔记/看板知识库。通过 git clone 加 install.sh 安装。

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

- 每任务独立 git worktree + 独立代理与上下文
- tess ship 一键完成测试→推送→PR→清理
- 向 Claude Code/Cursor/Codex/Gemini/opencode 安装技能并拦截原生 git worktree
- 本地访问 Messages/Mail/Calendar 等 12 个 Mac 连接器，数据不上传

## 适用场景

- 同时跑多个 AI 编码代理任务而不丢失追踪
- 按任务隔离代码变更并在完成后自动建 PR
- 让代理直接查询本机的邮件、日历与消息

## 场景标签

`编码 Agent` `知识库管理` · 领域:编码与开发

## 证据(README 行号)

> L2:  Run 10 AI coding agents without losing track of any of them.
> L3:  Every task gets its own git worktree, its own agent, its own context. One command shows you all of them.
> L16: git clone https://github.com/cleanmcp/tess.git && cd tess && ./install.sh
> L19: Add `~/.local/bin` to your `PATH`, then type `tess`. macOS. Skip any optional step — nothing breaks.

## 星数曲线

```mermaid
xychart-beta
    title "cleanmcp/tess 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3b02db113af3` · [字段定义](../../DATASET.md)*
