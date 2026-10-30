# saeedkolivand/claude-usage-mac

⭐ 15 · Swift · 推送 2026-10-21 · [GitHub](https://github.com/saeedkolivand/claude-usage-mac) · [官网](https://claude-usage-mac.iamsaeed.dev/) · 个人维护

**macOS 菜单栏与桌面小组件：显示 Claude Code 用量与费用**

Swift 编写的原生 macOS 应用，在菜单栏和桌面小组件中显示 Claude Code 的 5 小时/周限额百分比、token 计数与估算费用。数据来自本机两个来源：Anthropic OAuth usage 接口与 ~/.claude/projects 下的转录 JSONL，不发数据到外部。支持多配置文件（多账号）、阈值通知、CSV/JSON 导出、Claude Code statusline 安装及多种小组件样式。README 声明项目尚未在真实 Mac 硬件上运行过（在 Windows 上开发，仅通过编译与快照审查）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取 Anthropic usage 接口与本机 JSONL 转录，本地处理不发数据
- 菜单栏 + 小/中/大/项目级四类桌面小组件，多种样式
- 多账号 profile 支持，会话限额触顶时自动切换显示
- 可安装 Claude Code statusline 并支持 CSV/JSON 导出

## 适用场景

- 在菜单栏实时盯住 Claude Code 的 5 小时与每周限额
- 用桌面小组件分别监控不同账号或项目的 token 与费用
- 费用达到阈值时收到通知，导出每日用量做记录

## 场景标签

 · 领域:开发者工具/LLM 用量监控

## 证据(README 行号)

> L11: Claude Code usage in the macOS menu bar and as a desktop widget — session and
> L100: |`api.anthropic.com/api/oauth/usage`, using the OAuth token Claude Code already stored|5-hour and 7-day limit util
> L244:   UsageCore/     data layer, no UI — shared by the app, the widget, and the CLI

## 星数曲线

```mermaid
xychart-beta
    title "saeedkolivand/claude-usage-mac 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c90e26719a28` · [字段定义](../../DATASET.md)*
