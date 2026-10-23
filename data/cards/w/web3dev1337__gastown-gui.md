# web3dev1337/gastown-gui

⭐ 95 · JavaScript · MIT · 推送 2026-08-31 · [GitHub](https://github.com/web3dev1337/gastown-gui) · 个人维护

**Gas Town 多智能体编排系统的独立 Web 图形界面**

面向 steveyegge/gastown（基于 Claude Code 的多智能体编排系统）的独立配套 Web GUI，最初作为 PR #212 提交后转为独立维护。通过调用 gt/bd CLI 命令实现 Rig 管理、工作项跟踪、任务分派（sling）、PR 查看、代理收件箱与健康检查，WebSocket 提供实时更新，不直接修改 Gas Town 内部状态。npm 安装，兼容 Gas Town v0.2.x+ 与 Node.js 18/20/22；Agent 配置 UI 尚未实现，需用 CLI 完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过官方 gt/bd CLI 子进程执行全部操作，服务器权威设计
- WebSocket 实时广播状态变更
- Rig/工作项/任务分派/PR 跟踪/代理邮件/健康检查的图形化界面
- 提供 Nix/NixOS 模块与服务硬化默认配置

## 适用场景

- 为 Gas Town 编排系统提供浏览器端可视化管理
- 在统一界面中查看各 Rig 的 PR 与代理消息
- 运行 doctor 检查并监控 Gas Town 系统状态

## 场景标签

 · 领域:开发工具/智能体编排

## 证据(README 行号)

> L5: A standalone web GUI for Gas Town - the multi-agent orchestration system for Claude Code.
> L134: All operations execute through the official `gt` and `bd` commands - the GUI never directly modifies Gas Town's in
> L147: 1. **Server-Authoritative** - All operations execute via `gt` and `bd` CLI commands

## 星数曲线

```mermaid
xychart-beta
    title "web3dev1337/gastown-gui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-23 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `83fd4abfc079` · [字段定义](../../DATASET.md)*
