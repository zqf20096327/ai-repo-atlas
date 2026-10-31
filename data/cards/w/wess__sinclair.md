# wess/sinclair

⭐ 14 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/wess/sinclair) · [官网](https://wess.io/sinclair/) · 个人维护

**面向编码 agent 团队的 GPU 渲染终端（macOS/Linux）**

用 Rust 编写的终端模拟器，GPU 渲染、支持 Sixel/kitty 图形、OSC 8/52、kitty 键盘协议等标准特性，提供标签页、递归分屏、命令面板、22 主题与实时重载的 settings.json。在此之上提供 agent 工作区：每个分窗显示 agent 语义状态（working/blocked/done/idle）、共享 Docker/Podman 沙箱容器、每 agent 一个 git worktree、内置 MCP server 让 agent 操作终端本身，插件为沙箱化 WASM 组件。macOS 经 brew cask 或 dmg 安装，Linux 提供 x86_64/aarch64 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每分窗自报 agent 语义状态并汇总到 Activity 面板，接入 Claude Code 生命周期钩子
- 单一 Docker/Podman 容器作为全队 agent 共享沙箱（无需 VS Code/devcontainer CLI）
- 内置 MCP server：agent 可运行命令、读屏、切换标签、管理 worktree
- GPU 渲染 + 标准完备 VT（Sixel/kitty 图形、OSC 8/52、同步输出）

## 适用场景

- 在一个窗口里并行运行并监督多个编码 agent
- 把项目和 agent 放进同一容器沙箱隔离运行
- 通过 MCP 让 agent 直接操作终端（命令、读屏、worktree）

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L3: **The terminal your agent team lives in.**
> L6: working, blocked, or done — on top of a terminal that stands on its own. GPU-rendered, standards-complete VT, tabs a
> L11: macOS and Linux · Rust · Apache-2.0

## 星数曲线

```mermaid
xychart-beta
    title "wess/sinclair 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ae59bce664ea` · [字段定义](../../DATASET.md)*
