# agent-sh/computer-use-linux

⭐ 952 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/agent-sh/computer-use-linux) · 组织维护

**为 Linux 桌面上的 AI agent 提供本地桌面控制（MCP/CLI）**

Rust 编写的 MCP 服务器与 CLI，为 AI agent 提供本地 Linux 桌面的结构化控制：AT-SPI 无障碍树读取、受限截图、感知合成器的窗口定位、Wayland/X11 输入合成与单次往返的操作后验证。支持 GNOME、KDE Plasma、Hyprland、niri、COSMIC、i3、Sway、labwc 等 wlroots 合成器及 X11/EWMH。提供 npm 包、crates.io crate 与源码安装，预编译 x86_64/aarch64 二进制需 glibc 2.28+。该 crate 由 Codex Desktop 的 Linux 发行版抽取而来，本仓库为其上游。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Wayland 原生输入路径：/dev/uinput 或 freedesktop portal RemoteDesktop
- 感知合成器的窗口定位，支持多后端按序尝试并报告结果
- 语义选择器优先的点击/操作，AT-SPI element_index 定位
- doctor 命令输出结构化 JSON 就绪报告

## 适用场景

- 让 Claude Code 等 MCP 宿主通过 MCP 操作 Linux 桌面
- 自动化桌面应用测试与 UI 操作
- 在隔离工作区中运行 agent 桌面任务

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L15: `computer-use-linux` gives AI agents real, structured control of a local Linux desktop: semantic AT-SPI accessibili
> L47: `computer-use-linux` is a Rust MCP server and CLI for Linux desktop control. It ships three binaries: the main `com

## 星数曲线

```mermaid
xychart-beta
    title "agent-sh/computer-use-linux 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 713 --> 973
    line [734, 739, 743, 748, 757, 767, 772, 780, 784, 734, 830, 844, 849, 863, 871, 881, 889, 895, 899, 903, 907, 912, 916, 920, 928, 946, 952]
```

2026-10-25 734 → 2026-11-27 952（+218）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `8a8e6c45ccf3` · [字段定义](../../DATASET.md)*
