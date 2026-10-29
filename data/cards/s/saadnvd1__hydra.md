# saadnvd1/hydra

⭐ 21 · Go · MIT · 推送 2026-04-21 · [GitHub](https://github.com/saadnvd1/hydra) · 个人维护

**AI 编程 CLI 的统一包装器：限流时自动切换并传递上下文**

用 Go 编写的终端工具，将 Claude Code、Codex、OpenCode、Pi 等 AI 编程 CLI 以完整交互式 TUI 方式启动。通过监控终端输出识别限流/配额错误，触发切换时向所有运行中会话发送 SIGUSR1，提供按键式 provider 选择器；切换时把对话历史（解析 Claude Code 的 JSONL 会话文件）、git diff 与最近 5 条提交复制到剪贴板，粘贴到新 CLI 继续。默认回退链可在 config.yaml 配置，支持任意可交互运行的 CLI 作为 provider。需 Unix 终端（macOS/Linux/WSL）与至少一个 AI 编程 CLI，Linux 需 xclip 或 xsel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监控终端输出识别限流并触发 provider 切换
- 切换时提取对话历史 + git diff + 最近提交到剪贴板
- hydra switch 向所有运行中会话发送 SIGUSR1（限流按账户生效）
- 可通过配置接入任意交互式 CLI 作为 provider

## 适用场景

- AI 编程 CLI 频繁触发使用上限时自动切换到备用工具
- 在多个 AI 编程 CLI 之间保留上下文无缝切换
- 多会话并行开发中统一触发 provider 切换

## 场景标签

 · 领域:开发者工具/AI 编程

## 证据(README 行号)

> L3: Unified wrapper for AI coding CLIs. Run Claude Code, Codex, OpenCode, or Pi as a full interactive TUI. When one hits
> L60: 1. `hydra` spawns your AI coding CLI in a PTY — full interactive TUI, identical to running it directly
> L66: 4. On switch: conversation context (history + git diff + recent commits) is extracted and copied to clipboard

## 星数曲线

```mermaid
xychart-beta
    title "saadnvd1/hydra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7b93aaf4e92f` · [字段定义](../../DATASET.md)*
