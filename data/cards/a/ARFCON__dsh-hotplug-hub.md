# ARFCON/dsh-hotplug-hub

⭐ 28 · JavaScript · MIT · 推送 2026-08-30 · [GitHub](https://github.com/ARFCON/dsh-hotplug-hub) · 组织维护 · 中文 README

**DeepSeek Harness 的热插拔插件/技能/MCP 桌面管理器**

面向 dsh（DeepSeek Harness）用户的桌面插件管理器（WebView2 + C# WinForms），核心概念是 hotpack：带版本的可移植插件集合，可导入、激活、停用、移除而不改动宿主，统一安装到 ~/.dsh/profiles/web。功能覆盖插件与 Skill（SKILL.md）管理、MCP 服务器（STDIO/streamable-http）管理、按项目的全局记忆、GitHub 插件市场、由多家 LLM 驱动的对话式 hotpack 装配，以及启动时 Node/pnpm/profile 自检自愈。提供 Windows/Linux/macOS 安装包与便携包，也可源码安装。

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

- hotpack 热插拔机制：插件激活/停用/移除不改动宿主，profile 原子写入
- 管理 SKILL.md 技能与 STDIO/streamable-http 两类 MCP 服务器
- AI 装配员：多家 LLM（DeepSeek/OpenRouter/商汤/智谱等）驱动的对话式 hotpack 生成
- 启动自检自愈：自动检查并修复 Node/pnpm/profile/插件环境

## 适用场景

- 为 dsh 桌面端安装、停用和管理插件与技能
- 为 AI agent 配置并管理 MCP 服务器
- 通过对话让 AI 装配员生成 hotpack 配置包

## 场景标签

 · 领域:AI agent 工具链/插件管理

## 证据(README 行号)

> L12: **DSH-Hotplug-Hub** is the plugin manager for **Dseam World** — a Windows desktop application (WebView2 + C# WinFor
> L16: A hot-plug package manager for DeepSeek Harness (dsh). It introduces the concept of a **hotpack** — a versioned, po
> L35: - **MCP management** — add / remove / disable `STDIO` and `streamable-http` MCP servers, written uniformly into the

## 星数曲线

```mermaid
xychart-beta
    title "ARFCON/dsh-hotplug-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c6537df56adb` · [字段定义](../../DATASET.md)*
