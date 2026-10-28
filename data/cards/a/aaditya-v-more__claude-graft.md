# aaditya-v-more/claude-graft

⭐ 62 · Swift · MIT · 推送 2026-09-27 · [GitHub](https://github.com/aaditya-v-more/claude-graft) · [官网](https://graft.aadityamore.com/) · 个人维护

**macOS 菜单栏工具：并行运行多个 Claude Desktop 账号并共享聊天记录**

面向 macOS 13+ 的菜单栏应用，用于为 Claude Desktop 创建多个独立账号快捷方式，各自登录、名称与图标，可在 Spotlight/Dock 并行打开。支持在账号间共享 Claude Code 聊天历史、置顶与侧栏排序（双向同步），提供一次性聊天迁移、菜单栏实时用量显示、Start Session 开启五小时窗口等功能。它读取各 profile 的访问令牌但仅发送至 api.anthropic.com，不触碰刷新令牌。不修改 Claude 应用本体；通过 Homebrew cask 或 .dmg 安装，ad-hoc 签名未公证。

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

- 多 Claude Desktop 账号并行运行，各自独立登录与快捷方式
- Claude Code 聊天记录、置顶与侧栏排序跨账号双向同步
- 菜单栏显示各账号实时用量与重置时间
- 读取访问令牌仅发送至 api.anthropic.com，不触碰刷新令牌与登录

## 适用场景

- 我在多个 Claude 账号间切换使用，希望它们同时在线互不干扰
- 我想让多个账号共享同一份 Claude Code 聊天历史和置顶
- 我在菜单栏随时查看各账号的用量与重置时间

## 场景标签

 · 领域:桌面工具/AI 客户端管理

## 证据(README 行号)

> L24: Run multiple Claude Desktop accounts side by side, each with its own login,
> L25: shortcut and optional shared Claude Code history — including pins and sidebar

## 星数曲线

```mermaid
xychart-beta
    title "aaditya-v-more/claude-graft 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-28 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8e05624d5c56` · [字段定义](../../DATASET.md)*
