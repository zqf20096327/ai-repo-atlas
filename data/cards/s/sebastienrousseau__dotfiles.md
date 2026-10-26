# sebastienrousseau/dotfiles

⭐ 82 · Shell · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/sebastienrousseau/dotfiles) · [官网](https://doc.dotfiles.io/) · 个人维护

**面向开发者的跨平台声明式 dotfiles 工作站控制平面**

基于 chezmoi 的 dotfiles 管理框架，以 Bash 编写的 dot 命令行调度器为核心，覆盖 macOS/Linux/WSL/Windows(PowerShell 7.5+)。功能包括配置生命周期管理、壁纸驱动主题、加密机密、SSH fleet 批量应用、模块注册表与 SLSA 证明的发布。AI 相关部分：dot-ai-tui（Bubble Tea 界面，安装/运行/计费 Claude、Codex、Copilot 等 AI CLI）、只读 MCP 审计服务器、agent 上下文存根管理与 A2A 互操作卡。安装方式含校验脚本、Homebrew/Scoop/AUR/npm/Nix 及源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dot-ai-tui 单屏安装/运行/计费多家 AI CLI（Claude、Codex、Copilot、Aider 等）
- dot-mcp 只读 stdio MCP 服务器（JSON-RPC 2.0，4 工具 5 资源）做工作站策略审计
- 发布携带 SLSA 构建证明与 SHA256 校验安装器
- 支持 SSH fleet 应用与 Docker/Podman 沙箱预览

## 适用场景

- 用 chezmoi 声明式管理多台开发机的 shell/git/工具配置
- 在一个 TUI 里统一安装和运行多个 AI CLI 并计量用量
- 通过 MCP 允许名单在 agent 接触前审计 MCP 服务器
- 为 Claude Code / Cursor 等工具生成并校验 agent 上下文存根

## 场景标签

 · 领域:开发者工具/工作区配置

## 证据(README 行号)

> L226: |**`dot`** (`bin/dot` + `lib/dot`)|Bash dispatcher and shared library — lifecycle, diagnostics, themes, secrets, f
> L228: |**`dot-ai-tui`** (`defaults/dot_local/share/dot-ai-tui`)|Go Bubble Tea cockpit behind `dot ai`|Install, run, chat

## 星数曲线

```mermaid
xychart-beta
    title "sebastienrousseau/dotfiles 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-26 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `b42cbcfd09c8` · [字段定义](../../DATASET.md)*
