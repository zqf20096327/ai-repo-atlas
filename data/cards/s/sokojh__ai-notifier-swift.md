# sokojh/ai-notifier-swift

⭐ 14 · Swift · MIT · 推送 2026-01-21 · [GitHub](https://github.com/sokojh/ai-notifier-swift) · 个人维护 · 中文 README

**macOS 原生通知工具：AI 编程 CLI 完成响应时提醒用户**

用 Swift 编写的 macOS 原生通知应用，通过配置 Claude Code、Gemini CLI、Codex CLI、OpenCode 的 hook，在 AI 响应完成或请求权限时弹出系统通知（UNUserNotificationCenter API，兼容 Big Sur 至 Sequoia/Tahoe）。支持点击通知跳转对应终端/IDE 会话、从通知直接批准或拒绝权限请求（仅 iTerm2 与 Terminal.app），可选 ntfy 推送到移动端。提供 DMG、一键安装脚本与源码构建三种安装方式，附 8 种界面语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测并配置 4 种 AI CLI（Claude Code/Gemini CLI/Codex CLI/OpenCode）的 hook
- 点击通知跳转到终端会话（iTerm2/Terminal.app 精确到标签页）
- 通知内直接批准/拒绝权限请求（iTerm2 与 Terminal.app）
- 可选 ntfy 移动端推送，支持自建服务器与 Bearer/Basic 认证

## 适用场景

- 运行 AI 编程 CLI 时收到响应完成提醒，无需盯终端
- 在通知上直接处理权限弹窗，减少窗口切换
- 离开电脑时通过 ntfy 在手机上接收 AI 任务通知

## 场景标签

 · 领域:开发者工具/macOS 应用

## 证据(README 行号)

> L11: Native macOS notification app for AI coding assistants (Claude Code, Gemini CLI, Codex CLI, OpenCode)
> L248: CLI response complete → Hook executed → ai-notifier called →

## 星数曲线

```mermaid
xychart-beta
    title "sokojh/ai-notifier-swift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9986482916b1` · [字段定义](../../DATASET.md)*
