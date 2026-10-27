# nirholas/auto-kill-terminal

⭐ 22 · Shell · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/nirholas/auto-kill-terminal) · [官网](https://nirholas.github.io/auto-kill-terminal/) · 个人维护

**给 AI 编码代理的终端管理规则文本，防止僵尸终端**

面向使用 GitHub Codespaces 与 VS Code 的开发者：AI 编码代理（Copilot、Claude Code、Gemini、Cursor、Windsurf、Aider 等）执行命令后会遗留终端会话，在 Codespaces 中造成命令超时与令牌浪费。本仓库提供可复制粘贴的 5 条终端管理规则，要求代理使用 isBackground: true 后台终端并在命令结束后调用 kill_terminal 清理。以 Markdown 文本形式提供，无需安装任何包、扩展或配置，放入对应代理的指令文件即可；环境支持覆盖 Codespaces 与本地/远程/WSL 的 VS Code。

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

- 5 条可复制的终端管理规则（isBackground: true + kill_terminal）
- 为 Copilot/Claude Code/Gemini/Cursor/Windsurf/Aider 分别给出指令文件写法
- 提供单行/两行版规则用于内联提示
- 无需安装包或扩展，纯文本规则

## 适用场景

- 修复 Codespaces 中代理命令超时或终端无响应
- 让 AI 代理执行命令后自动清理终端会话
- 为多代理项目统一终端管理规范（AGENTS.md）

## 场景标签

 · 领域:开发工具/AI 代理配置

## 证据(README 行号)

> L28: AI coding agents (GitHub Copilot, Claude Code, Gemini, Cursor, etc.) spawn terminal sessions every time they run a 
> L164: No. This is just copy-paste text that goes into your agent instruction files. No packages, no extensions, no confi
> L199: Coding agents and LLM tooling can read this repo directly: AGENTS.md, llms.txt, llms-full.txt. Point an agent at `

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/auto-kill-terminal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6b32010f94d2` · [字段定义](../../DATASET.md)*
