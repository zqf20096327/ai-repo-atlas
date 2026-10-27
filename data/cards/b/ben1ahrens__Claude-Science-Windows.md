# ben1ahrens/Claude-Science-Windows

⭐ 37 · Shell · MIT · 推送 2026-08-04 · [GitHub](https://github.com/ben1ahrens/Claude-Science-Windows) · 个人维护

**在 Windows 上通过 WSL2 运行 Claude Science 的安装器与任务栏启动器**

面向 Windows 用户的非官方社区封装：将 Anthropic 仅官方支持 macOS/Linux 的 Claude Science 安装进 WSL2 发行版，并创建可固定到任务栏的开始菜单快捷方式，点击后唤醒 WSL、启动守护进程、在默认浏览器打开单次登录链接。安装器为 PowerShell 脚本，可在发行版内安装 bubblewrap/socat/curl 并运行官方安装程序，支持 -DryRun 预览与指定发行版等选项。使用需 Claude 付费账户，WSL2 发行版共享网络命名空间，同时仅一个发行版可运行守护进程（占用 localhost:8765）。

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

- PowerShell 一键安装 Claude Science 到 WSL2 并创建开始菜单快捷方式
- 启动器仅为指向 wsl.exe 的快捷方式，无自定义二进制
- 安装脚本支持 -DryRun 预览与 -Distro/-CreateNew 等选项
- 提供 claude-science status/logs/stop 等守护进程管理命令

## 适用场景

- 在 Windows 上以桌面应用方式使用 Claude Science
- 不敲 wsl 命令、一键从任务栏启动并自动打开浏览器登录
- 在多个 WSL 发行版中预览和管理 Claude Science 守护进程

## 场景标签

 · 领域:科研工具/系统封装

## 证据(README 行号)

> L7: *Anthropic ships Claude Science for macOS and Linux only. This gives Windows users a first-class
> L35: project installs Claude Science *inside* a WSL distribution and gives you a **pinnable Windows
> L44: > binaries**. It downloads and runs the *official* Claude Science installer inside your WSL distro.

## 星数曲线

```mermaid
xychart-beta
    title "ben1ahrens/Claude-Science-Windows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `31862f661e0e` · [字段定义](../../DATASET.md)*
