# marc2332/term

⭐ 20 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/marc2332/term) · [官网](https://term.mespin.me/) · 个人维护

**用 Rust 与 Freya 构建的个人向终端模拟器**

基于 Freya 框架与 Rust 开发的桌面终端模拟器 marcterm，功能包括多标签页、面板水平/垂直分屏与拖拽调整、可折叠侧边栏、运行时字号调节；支持列出 Git worktrees 并显示 live diff 统计（围绕作者自己的 marcgit 工作流设计）。安装途径为 Debian/Ubuntu 的 .deb 包或 cargo install，配置从 ~/.config/marcterm.toml 读取。README 声明该模拟器围绕作者本人的用法设计，在其他环境下可能出现意外行为。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多标签页与面板水平/垂直分屏、拖拽调整大小
- Git worktree 列表与 live diff 统计
- 提供 .deb 安装包与 cargo install 两种安装方式
- 通过 ~/.config/marcterm.toml 配置启动 shell 等选项

## 适用场景

- 需要一个支持分屏与多标签的 Linux 桌面终端
- 在多 Git worktree 工作流中查看各 worktree 的 diff 状态
- 通过配置文件自定义终端启动 shell

## 场景标签

 · 领域:桌面/开发者工具

## 证据(README 行号)

> L5:  Terminal emulator built with Freya and Rust 🦀
> L35: - 🌿 **Git worktrees** — every worktree is listed under its project with live diff stats, mostly designed around how

## 星数曲线

```mermaid
xychart-beta
    title "marc2332/term 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `0b01074f210f` · [字段定义](../../DATASET.md)*
