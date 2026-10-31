# IEZhu/Agents

⭐ 14 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/IEZhu/Agents) · [官网](https://agents-core.ai) · 个人维护

**为 AI 编码客户端提供专家角色、工作流与项目记忆的本地 MCP 服务器**

运行在本地的一个 MCP 服务器，服务于 Claude Code、Codex、Cursor、Claude Desktop、Antigravity 等 MCP 客户端：按任务路由专家人格（含技能与共享规则）、提供称为 cognitive implants 的推理模式、由模型自身工具执行的 Markdown 工作流（PR 审查、文档刷新等）、有边界且结果经验证的委派子代理，以及按仓库的描述与交互历史记忆。核心服务器无需外部 API key，安装需 Python 3.11+ 并下载约 1.1 GB 本地嵌入模型；macOS/Linux 提供一键安装脚本，Windows 通过初始化脚本，另有 Claude Code 插件形态（仅作启动器，不装 Python 环境）。文件编辑与 shell 命令仍由宿主客户端负责。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按任务路由专家人格（审查者、架构师等）并跨轮次保持
- Markdown 工作流由当前模型用自身工具执行（PR 审查、文档刷新等）
- 有界委派子代理：紧凑角色、验收标准与结构化结果契约及验证
- 按仓库的项目记忆：仓库描述与可检索的交互历史

## 适用场景

- 让我的编码助手在实现、审查、架构等任务中切换专家角色
- 把 PR 审查、文档刷新等流程固化为可重复工作流
- 在多个 MCP 客户端间共享同一套人格、规则与项目记忆

## 场景标签

`提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Agents-Core is one local MCP server for Claude Code, Codex, Cursor, Claude Desktop, Antigravity and other MCP client
> L30: |🔌|One server for every client|A shared local service on macOS and Windows, managed instruction files, and your oth
> L56: The core server needs no external API key. Setup requires Python 3.11+ and downloads a local embedding model (about

## 星数曲线

```mermaid
xychart-beta
    title "IEZhu/Agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a780e399b993` · [字段定义](../../DATASET.md)*
