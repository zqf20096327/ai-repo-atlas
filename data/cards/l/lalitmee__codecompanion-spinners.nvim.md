# lalitmee/codecompanion-spinners.nvim

⭐ 24 · Lua · MIT · 推送 2026-06-23 · [GitHub](https://github.com/lalitmee/codecompanion-spinners.nvim) · 个人维护

**为 codecompanion.nvim 提供 AI 活动状态旋转指示器的 Neovim 扩展**

作为 codecompanion.nvim 的扩展安装于其 extensions 表中，功能是以旋转指示器和通知展示 AI 的实时活动状态（如 Thinking、Running Tools、Awaiting Review）。提供 8 种样式：cursor-relative 浮窗（默认）、fidget、snacks、noice、lualine、heirline、native 原生浮窗与 none；其中 lualine/heirline/fidget/snacks 样式需相应插件已安装，native 仅用 Neovim 内置功能。通过插件管理器（如 lazy.nvim）安装，需先装主插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 种可切换的 spinner 样式（浮窗/通知/状态栏/禁用）
- 指示器随 AI 状态动态变化（Thinking/Running Tools/Awaiting Review 等）
- 以 codecompanion.nvim 扩展形式构建，图标、消息、高亮组可配置
- native 样式仅依赖 Neovim 内置功能

## 适用场景

- 在 Neovim 中获得 codecompanion AI 活动的实时视觉反馈
- 将 AI 状态显示集成到 lualine/heirline 状态栏或 fidget/snacks 通知
- 按个人工作流定制 spinner 图标与行为

## 场景标签

 · 领域:开发工具/编辑器插件

## 证据(README 行号)

> L7: *A companion extension for `codecompanion.nvim` that provides beautiful, configurable status spinners and notificati
> L22: Install with your favorite plugin manager. This plugin is a `codecompanion.nvim` extension and should be configured
> L26: > ⚠️ **Note:** This is an extension for `codecompanion.nvim`. Make sure you have the main plugin installed first.

## 星数曲线

```mermaid
xychart-beta
    title "lalitmee/codecompanion-spinners.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `98654b43aee3` · [字段定义](../../DATASET.md)*
