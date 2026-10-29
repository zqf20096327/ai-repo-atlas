# krishnakanthb13/ai_cli_manager

⭐ 44 · Batchfile · NOASSERTION · 推送 2026-10-17 · [GitHub](https://github.com/krishnakanthb13/ai_cli_manager) · 个人维护

**统一安装、管理与启动 28 种 AI 编程 CLI 的命令行工具**

面向开发者的命令行工具，用 Batch（Windows）与 Shell（Linux/macOS）脚本提供 28 种 AI 编程助手 CLI（Claude、Copilot、Codex、Qwen Code 等）的统一安装、版本检查与启动入口。功能包括启动前验证 CLI 是否已安装、自动检测并安装 Node.js/Python/Git 等依赖、向 Windows 资源管理器右键菜单添加两级级联菜单（规避每菜单 16 项的注册表限制），以及 Beast Mode：在 Windows Terminal 或 tmux 中以 2x2 网格同时运行 4 个 AI CLI。另提供注册表备份与日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 28 种 AI 编程 CLI 的安装、版本检查与统一启动
- Beast Mode 在 Windows Terminal/tmux 中以 2x2 网格同时运行 4 个 CLI
- 自动检测并安装 Node.js/Python/Git/curl 等依赖
- Windows 右键两级级联菜单集成与注册表备份/清理

## 适用场景

- 在一台机器上批量安装和更新多个 AI 编程助手 CLI
- 通过右键菜单在任意文件夹快速启动指定的 AI 编程助手
- 同时开 4 个 AI CLI 对照使用完成同一项目任务

## 场景标签

 · 领域:开发者工具/AI CLI 管理

## 证据(README 行号)

> L10: **AI CLI Manager (v1.2.50)** is a powerful command-line utility designed to simplify the installation, management, 
> L13: * **Unified Launcher**: Launch any supported AI CLI (Gemini, Claude, Copilot, etc.) with a single keystroke.

## 星数曲线

```mermaid
xychart-beta
    title "krishnakanthb13/ai_cli_manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2a8942d41452` · [字段定义](../../DATASET.md)*
