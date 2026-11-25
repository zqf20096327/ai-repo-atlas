# theBGuy/GitDesktop

⭐ 252 · TypeScript · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/theBGuy/GitDesktop) · [官网](https://gitdesktop.app) · 个人维护

**键盘优先的 AI Git 桌面客户端，AI 可选可关闭**

基于 Tauri 2 + React 19 的开源（Apache-2.0）Git 桌面客户端，覆盖 Windows/macOS/Linux。核心是 Git 操作与 PR 全流程：staging、diff、交互式 rebase、跨 GitHub/GitLab/Bitbucket 的 PR 评审与 CI、离线本地 PR、GitHub Actions 管理面板、分支清理与恢复。所有 GitHub 访问经由 gh CLI，token 不落盘。AI 功能（提交信息生成、评审、CI 调试、代理任务）由用户自选提供商（含本地模型），且可通过开关整体隐藏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 GitHub/GitLab/Bitbucket 的 PR/MR、CI、issue 统一管理
- 离线本地 PR 与 GitHub Actions 管理面板
- AI 提交信息/评审/CI 调试，提供商可选含本地模型，可整体关闭
- 交互式 rebase、merge prediction、丢失 stash 恢复等 git 深度工具

## 适用场景

- 在桌面端完成 PR 评审、评论、批准与合并而不开浏览器
- 把任务交给 Claude Code/Codex 等编码代理并审阅其改动
- 一键清理与恢复大量过期分支
- 隐私敏感环境下关闭全部 AI 界面使用纯 Git 客户端

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5:  An AI-native, keyboard-first Git desktop client
> L20: AI runs through commits, reviews, and CI debugging, with the provider you
> L21: choose (local models included). It's also optional: one switch hides every AI

## 星数曲线

```mermaid
xychart-beta
    title "theBGuy/GitDesktop 星数(近 12 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-25"]
    y-axis "stars" 236 --> 253
    line [237, 238, 239, 240, 242, 238, 247, 248, 249, 251, 252, 252]
```

2026-10-23 237 → 2026-11-25 252（+15）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `40c51b7040c3` · [字段定义](../../DATASET.md)*
