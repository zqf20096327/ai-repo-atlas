# robcholz/vibebox

⭐ 191 · Rust · MIT · 推送 2026-02-18 · [GitHub](https://github.com/robcholz/vibebox) · [官网](https://vibebox.robcholz.com/) · 个人维护 · 中文 README

**Apple Silicon 上的微型 VM 沙箱：安全运行编码 agent**

基于 Apple Virtualization Framework 的 per-project micro-VM 沙箱 CLI，用 Rust 编写，面向 macOS（Apple Silicon）用户运行编码 agent。机制：单条 `vibebox` 命令进入当前仓库对应的 Debian Linux 虚拟机，warm re-entry 通常 <5 秒（作者 M3）；通过 vibebox.toml 显式挂载白名单（默认仅仓库可写，.git 用 tmpfs 遮蔽）实现隔离；支持多实例会话管理与缓存复用。首次运行需下载 Debian 基础镜像；首次登录自动安装 mise 及 uv/node/codex/claude-code 等工具（best-effort）。限制：仅支持 macOS Apple Silicon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Apple Virtualization Framework 的 per-project Linux micro-VM 隔离边界
- warm re-entry 通常 <5s，单命令进入当前仓库沙箱
- vibebox.toml 显式挂载白名单，默认 repo-first、其余 opt-in
- 多实例会话管理（复用、多终端、清理）与项目级 .vibebox 状态目录

## 适用场景

- 让编码 agent 在隔离 VM 中执行任意命令而不接触宿主机
- 日常开发中以单命令快速进入/复用 per-repo 沙箱
- 按项目配置 CPU/RAM/磁盘与挂载路径的本地开发环境

## 场景标签

 · 领域:开发工具/虚拟化沙箱

## 证据(README 行号)

> L22: **VibeBox is a per-project micro-VM sandbox for running coding agents on macOS (Apple Virtualization Framework).**
> L57: I use coding agents daily, and I wanted to give them a real shell without handing them my host machine.
> L25: **Who it’s for:** macOS users running coding agents who want real isolation without giving up a fast daily workflow

## 星数曲线

```mermaid
xychart-beta
    title "robcholz/vibebox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 187 --> 191
    line [188, 190, 190]
```

2026-10-18 188 → 2026-10-22 190（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cd7dccb652b4` · [字段定义](../../DATASET.md)*
