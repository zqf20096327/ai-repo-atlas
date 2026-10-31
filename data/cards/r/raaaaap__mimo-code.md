# raaaaap/mimo-code

⭐ 14 · TypeScript · MIT · 推送 2026-06-01 · [GitHub](https://github.com/raaaaap/mimo-code) · 个人维护 · 中文 README

**终端 AI 编程 agent：MiMo 大模型驱动的 CLI 结对编程工具**

基于 TypeScript 与 Ink（React for CLI）构建的终端 AI 编程助手，由小米 MiMo 大模型驱动，也支持 OpenAI 与 Anthropic API。提供交互式 REPL，通过自然语言对话写代码、执行命令、搜索文件与管理任务：内置 33 个工具（Bash/PowerShell/文件读写/Grep/MCP 调用/子 agent 等）、48 个斜杠命令、计划模式、5 种权限模式、会话持久化与成本追踪。经 git clone + npm install 源码安装，需 Node.js ≥ 18 与 API key。

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

- 33 个内置工具，含 Bash/PowerShell/MCP/子 agent 派生与 git worktree 隔离
- 多 Provider 支持：MiMo（OpenAI/Anthropic 协议）、OpenAI 兼容端点、Anthropic
- 计划模式、5 种权限模式与并发安全工具编排（只读并行、破坏性串行）
- 会话持久化、成本追踪、多语言 UI（zh-CN/en/ja）与插件系统

## 适用场景

- 在终端通过自然语言让 AI 编写和修改代码
- 让 agent 执行命令、搜索文件并管理开发任务
- 接入 MCP 服务器扩展 agent 能力

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14:  A terminal AI coding agent powered by MiMo LLM
> L21: Mimo Code is a terminal-based AI coding assistant powered by the MiMo large language model. Built with TypeScript a
> L246: Tool calls → Execute via ToolRegistry → Append results → Loop

## 星数曲线

```mermaid
xychart-beta
    title "raaaaap/mimo-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b7c57e3316e7` · [字段定义](../../DATASET.md)*
