# danilokhury/Synabun

⭐ 70 · JavaScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/danilokhury/Synabun) · [官网](https://synabun.ai) · 个人维护

**自托管持久记忆 MCP 服务器与 AI 编码工作台**

开源的本地优先持久记忆层与自托管 AI 工作区：以 MCP 服务器（stdio）形式为 Claude Code、Codex、OpenCode、Cursor 等提供 remember/recall 等记忆工具，数据存于单个本地 SQLite 文件，无账号无云服务。附带本地 Web 界面 Neural Interface（端口 3344），提供 3D 记忆地图、多编码 agent 并排面板、任务模板与定时自动化、浏览器工具及 WhatsApp 接入。语义检索依赖本地运行 embedding 模型，需 Node.js 22.19+；不含模型访问，各编码工具使用用户自己的账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器提供 remember/recall/reflect/forget 等记忆工具，任意 MCP 客户端可用
- 记忆存储于本地单个 SQLite 文件，embedding 模型本地运行
- Neural Interface 提供 3D 记忆地图与 Claude Code/Codex/OpenCode 并排面板
- SynaBun Assistant 可规划任务并分派给 worker，支持任务模板与定时运行

## 适用场景

- 让 Claude Code/Codex 等编码工具跨会话、跨项目共享记忆
- 在本地界面查看、搜索、编辑各 agent 记住了什么
- 在一个工作台并排运行多个编码 agent 并共用记忆
- 把重复任务保存为模板按计划自动执行

## 场景标签

`Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L16: **SynaBun is an open-source, self-hosted AI workspace and persistent memory MCP server: SynaBun Assistant coordinat
> L86: - **An MCP server.** It gives your AI tool the memory tools: `remember`, `recall`, `reflect`, `forget`, `restore` a
> L33: It connects to Claude Code, Codex CLI, Gemini CLI and OpenCode with one switch each, and to Cursor, Windsurf or any

## 星数曲线

```mermaid
xychart-beta
    title "danilokhury/Synabun 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-26 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7b24f4073523` · [字段定义](../../DATASET.md)*
