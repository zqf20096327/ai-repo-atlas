# pieces-app/cli-agent

⭐ 113 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/pieces-app/cli-agent) · [官网](https://docs.pieces.app/products/cli) · 组织维护

**与 PiecesOS 交互的命令行客户端，管理资产与对话**

Pieces 官方的 Python 命令行工具，用于连接本地运行的 PiecesOS：提供资产（materials/Pieces Drive）管理、对话（conversation）交互、应用操作等功能，通过 `pieces` 主命令加子命令使用，支持 run 循环模式。运行前提是系统已安装并启动 PiecesOS。安装途径包括 pip、brew、conda，支持 bash/zsh/fish/PowerShell 自动补全；开发构建使用 poetry，测试使用 pytest。

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

- 通过子命令访问 PiecesOS 的资产管理与对话等功能
- 支持 pip / brew / conda 三种安装方式
- bash/zsh/fish/PowerShell 自动补全
- run 子命令提供循环式交互模式

## 适用场景

- 在终端中管理 Pieces Drive 中的素材
- 通过 CLI 与 PiecesOS 对话功能交互
- 在脚本或终端工作流中操作 PiecesOS 功能

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3:  This is a comprehensive command-line interface (CLI) tool designed to interact seamlessly with PiecesOS. It provide
> L11: Make sure you have **PiecesOS** installed in order to run the Pieces CLI tool.

## 星数曲线

```mermaid
xychart-beta
    title "pieces-app/cli-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-25 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `545124518065` · [字段定义](../../DATASET.md)*
