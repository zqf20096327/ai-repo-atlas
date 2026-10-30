# nairiai/nairid

⭐ 25 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/nairiai/nairid) · [官网](https://nairi.ai) · 组织维护

**运行 AI 编码 agent 并接入 Slack/Discord 协作的守护进程**

由 Nairi 平台维护的 agent 守护进程：在本机运行 AI 编码助手（Claude Code、Cursor、Codex、OpenCode 四种，Claude Code 为默认），将其连接到 Nairi 平台，并通过 Slack/Discord 触发。它会自主创建分支、修改代码并发起 PR，依赖 GitHub CLI 与 NAIRI_API_KEY 环境变量，可配置会话最大时长。提供 Homebrew 安装与 Go 源码编译两种方式，支持 macOS/Linux/Windows 的 Intel 与 ARM 原生二进制。文档区分 acceptEdits 安全模式与 bypass 权限模式并给出隔离环境建议。

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

- 支持 Claude Code/Cursor/Codex/OpenCode 四种 AI 编码助手，Claude Code 默认
- 通过 Slack/Discord 触发 agent 自主建分支、改代码、发 PR
- 可配置单次 agent 调用的最大时长（NAIRI_MAX_SESSION_MS）
- 区分 acceptEdits 与 bypass 权限模式并提供安全建议

## 适用场景

- 在团队 Slack/Discord 中远程驱动 AI 编码助手完成编码任务
- 为 AI agent 单独克隆仓库并自动产出 PR 的工作流
- 通过专用 bot 账号让 agent 代表团队提交代码

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: The Nairi daemon - runs your AI coding agents and connects them to the Nairi platform. nairid bridges AI assistants 
> L7: - **Claude Code**: Anthropic's official CLI tool for software engineering (default)
> L10: - **OpenCode**: Open-source AI coding agent with multi-provider model support

## 星数曲线

```mermaid
xychart-beta
    title "nairiai/nairid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1483d59c766c` · [字段定义](../../DATASET.md)*
