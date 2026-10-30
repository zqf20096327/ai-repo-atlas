# drewnekota/cetus

⭐ 149 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/drewnekota/cetus) · [官网](https://cetus.run) · 个人维护 · 中文 README

**macOS 桌面客户端：统一管理与审阅多个编码 agent 运行时**

面向使用多个编码 agent 的用户的 macOS 桌面应用：在同一窗口中运行和管理 Claude Code、Codex、DeepSeek Harness、OpenCode、Grok Build、Kimi CLI 或内置运行时，复用已安装 CLI 的登录与模型配置。提供权限提示卡片、会话看板（进行中/待审阅/完成）、每会话 git worktree 并行、定时任务（at/every/cron/daily）、双 ⌘ 键快捷启动器、屏幕上下文 OCR、会议转录与听写。内置运行时支持 30+ 模型供应商。仅支持 Apple Silicon，提供 Tauri 与 SwiftUI 两个 DMG 构建，自声明早期版本。

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

- 同一窗口管理 Claude Code/Codex/DeepSeek Harness 等多个 agent 运行时，复用已有 CLI 登录
- 权限提示与计划以卡片呈现，会话按进行中/待审阅/完成看板组织
- 每会话独立 git worktree，支持多 agent 并行编辑同一仓库
- 内置运行时支持 30+ 模型供应商（Anthropic/OpenAI/Bedrock/Ollama 等）

## 适用场景

- 同时使用多个编码 agent 时统一处理权限提示与提问
- 把提示设为定时任务并在同一看板审阅结果
- 用全局快捷键带屏幕上下文随时唤起 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  Cetus is a desktop client for reviewing and managing the work of every agent you run — Claude Code, Codex, DeepSeek
> L36: - **Every runtime in one window.** Use the CLI you already have installed and signed in to. Cetus reuses its login,
> L77: - **30+ model providers** for the built-in runtime, including Anthropic, OpenAI, Google, Bedrock, Ollama, LM Studio

## 星数曲线

```mermaid
xychart-beta
    title "drewnekota/cetus 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 147 --> 150
    line [148, 149, 149]
```

2026-10-18 148 → 2026-10-30 149（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1c29e1b3e6fd` · [字段定义](../../DATASET.md)*
