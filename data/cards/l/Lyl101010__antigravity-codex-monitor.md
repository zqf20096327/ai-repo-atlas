# Lyl101010/antigravity-codex-monitor

⭐ 9 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Lyl101010/antigravity-codex-monitor) · 个人维护 · 中文 README

**为 Antigravity 提供实时监控 Codex 任务并派单的 MCP App**

面向 Google Antigravity 的原生 MCP Server / MCP App 插件：当 Antigravity（Gemini）把编码、重构、补单测等任务派发给本地 OpenAI Codex CLI（codex exec）时，该插件在 Antigravity 右侧辅助栏弹出监控面板，每 0.8 秒流式展示执行命令、语法高亮 Diff、模型档位与 Token/缓存命中统计。采用纯本地只读轮询，不修改 .asar、不依赖 CDP 注入。内置跨平台派单脚本（PowerShell/Shell）与 codex-worker Skill，支持沙箱隔离、Git worktree 与按 SESSION_ID 续跑。安装需 Python 3.10+ 与 mcp 包，最终用户端无需 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 右侧栏每 0.8s 实时展示 codex exec 的命令、Diff 与 Token 统计
- 遵循 MCP Apps（SEP-1865）规范，不修改客户端、零 CDP 侵入
- 内置跨平台派单脚本与 codex-worker Skill，前端预编译单文件 HTML
- 默认 read-only / workspace-write 沙箱隔离，Git 写任务默认 --worktree

## 适用场景

- 让 Antigravity 统筹规划并把编码任务派发给本地 Codex CLI 执行
- 实时查看后台运行中的 codex exec 命令输出与文件改动
- 以沙箱与 worktree 隔离方式运行 Codex 写任务并按会话续跑

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: 面向 **Google Antigravity** 的原生 **MCP Server / MCP App**（Model Context Protocol）实时协作监控面板与 `codex-worker` 派单套件。
> L14: 当你让 Antigravity（Gemini）统筹规划并把编码、重构、写脚本、补单测等任务派发给本地官方 **OpenAI Codex CLI（`codex exec`）** 执行时，以往 `codex exec` 只能在后台黑盒
> L36: - **一个插件，开箱即用**：内置侧栏监控面板 + 跨平台派单脚本（Windows `run-codex.ps1` / macOS & Linux `run-codex.sh`）+ 内嵌 `codex-worker` Skill


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `60e6d472826c` · [字段定义](../../DATASET.md)*
