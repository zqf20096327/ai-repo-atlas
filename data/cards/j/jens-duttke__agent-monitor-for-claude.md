# jens-duttke/agent-monitor-for-claude

⭐ 21 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/jens-duttke/agent-monitor-for-claude) · 个人维护 · 中文 README

**本地桌面监控器：一眼看清各 Claude Code agent 的运行状态与费用**

面向同时运行多个 Claude Code agent 的开发者的 Windows/Linux 桌面工具。只读、完全离线地读取 ~/.claude/ 会话数据，按项目分组展示每个 agent 的实时状态（working/waiting/permission/finished 等）、按模型估算美元费用、宿主应用、版本与子 agent 数量，并支持一键聚焦宿主窗口、会话内容搜索、背景进程监控。Windows 提供单文件可执行程序，Linux 需从源码运行（依赖 GTK/WebKit）。作者声明项目处于早期阶段。

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

- 按项目分组实时展示所有运行中 Claude Code agent 的状态、估算费用、模型与宿主
- 支持 WSL 会话监控（经 \\wsl.localhost 只读读取）
- 会话 transcript 内容搜索（大小写/整词/正则，结果流式加载）
- Windows 单文件便携可执行程序，零配置零安装

## 适用场景

- 同时跑多个 Claude Code agent 时分辨谁在工作、谁在等我
- 按项目追踪各 agent 的 token 用量与估算费用
- 一键跳转到被权限提示阻塞的 agent 窗口

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A local desktop window that shows every running Claude Code agent at a glance - grouped by project, with each agent'
> L43: - Claude Code (this tool reads the session data it writes under `~/.claude/`)

## 星数曲线

```mermaid
xychart-beta
    title "jens-duttke/agent-monitor-for-claude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `db8292010a0a` · [字段定义](../../DATASET.md)*
