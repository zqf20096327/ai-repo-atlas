# AgriciDaniel/claude-code-essentials-vs-code

⭐ 65 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/AgriciDaniel/claude-code-essentials-vs-code) · [官网](https://agricidaniel.com) · 个人维护

**Claude Code 与 VS Code 扩展的选择性安装脚本助手**

一个用 PowerShell/Bash 编写的可选式安装包装脚本：默认不安装任何内容，用户在预览确认后再执行，负责安装 Claude Code CLI（缺失时走 Anthropic 官方 HTTPS 安装器）和指定的 VS Code 扩展。扩展 ID 需符合 publisher.extension 格式，已存在的组件会被跳过，安装后有版本与列表校验，无自动回滚。跨 Windows/macOS/Linux/WSL，不安装 Node、Git、VS Code 等运行时，也不修改 shell 配置或 ~/.claude。附带 Python 测试脚本，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认零安装、预览后需显式 -Apply/--apply 才执行
- 缺失 CLI 时调用 Anthropic 原生 HTTPS 安装器（默认 stable 通道）
- 扩展 ID 严格校验为 publisher.extension，已有组件跳过不覆盖
- 安装后校验扩展列表与 CLI 版本，失败即非零退出并输出诊断

## 适用场景

- 按需安装 Claude Code CLI 与其 VS Code 扩展
- 审查脚本来源后可控地完成 Windows 环境配置
- 为不存在的 CLI 指定安装版本或通道

## 场景标签

 · 领域:开发工具/安装脚本

## 证据(README 行号)

> L3: A small, opt-in setup helper for Claude Code and selected VS Code extensions.
> L36: change or channel change is attempted. A missing CLI uses Anthropic's native

## 星数曲线

```mermaid
xychart-beta
    title "AgriciDaniel/claude-code-essentials-vs-code 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-30 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e3a5cad7c25` · [字段定义](../../DATASET.md)*
