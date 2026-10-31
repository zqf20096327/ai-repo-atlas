# AwalTerminal/Awal-terminal

⭐ 34 · Swift · MIT · 推送 2026-10-21 · [GitHub](https://github.com/AwalTerminal/Awal-terminal) · [官网](https://awalterminal.github.io/Awal-terminal/) · 组织维护

**面向 AI 编码代理的 macOS 原生终端模拟器**

用 Swift 与 Rust 从零构建的 macOS 终端：Metal GPU 渲染、120fps、万行回滚缓冲。面向使用 Claude Code、Gemini CLI、Codex CLI 等 AI 编码代理的开发者，提供 LLM 配置一键切换、AI 侧栏（token/成本/上下文跟踪）、Mission Control 跨窗口代理监控、AI 组件管理与注入、设备端语音输入、会话录制导出 GIF 等。通过 Homebrew Cask 或 GitHub Releases 安装，也可用 Rust/Swift 工具链从源码构建；应用尚未通过 Apple 公证，首次启动需手动放行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Metal GPU 渲染 120fps，万行回滚缓冲
- LLM Profiles 一键切换 Claude/Gemini/Codex/纯 shell
- AI 侧栏与 Mission Control 实时跟踪 token、成本与代理状态
- AI 组件管理：自动检测技术栈并注入 skills/rules/MCP servers/hooks

## 适用场景

- 在终端中运行和监控多个 AI 编码代理会话
- 跟踪各标签页 AI 代理的 token 用量与花费
- 按项目技术栈自动注入 AI 组件与规则
- 用语音输入和会话录制辅助 AI 结对开发

## 场景标签

 · 领域:开发工具/终端

## 证据(README 行号)

> L14:  The LLM-native terminal emulator for macOS.
> L22: A native macOS terminal built from scratch with Swift and Rust, designed specifically for working with AI coding ag

## 星数曲线

```mermaid
xychart-beta
    title "AwalTerminal/Awal-terminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a142013bfa27` · [字段定义](../../DATASET.md)*
