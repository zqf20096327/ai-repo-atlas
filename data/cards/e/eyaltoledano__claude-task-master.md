# eyaltoledano/claude-task-master

⭐ 28,243 · JavaScript · NOASSERTION · 推送 2026-04-28 · [GitHub](https://github.com/eyaltoledano/claude-task-master) · [官网](https://tryhamster.com) · 个人维护

**AI 驱动的开发任务管理系统，可接入多款 AI 编辑器**

以 MCP 服务器与 npm CLI 两种形式运行的任务管理系统：解析 PRD 生成任务，支持任务拆分、依赖管理、状态更新、复杂度分析与研究命令，提供 36 个 MCP 工具并可按 all/standard/core/custom 模式选择性加载以控制上下文占用。需配置至少一个 AI 供应商的 API key（或 Claude Code/Codex CLI OAuth），可定义主模型、研究模型与回退模型。采用 MIT + Commons Clause 许可，禁止将其本身作为托管服务出售。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`maintenance` — 距上次 push 172.8 天,年发版 33,56 位贡献者
- 涨星:近 1 天 **+6**(自 20261016 起算)
- 安装:npm 包 `task-master-ai` 月下载 70,539
- 平台:— · 协议:OPENAI-API / MCP

## 能力要点

- MCP 服务器形式接入 Cursor、Windsurf、VS Code、Q CLI 等编辑器
- 36 个 MCP 工具支持 selective tool loading（all/standard/core/custom 四种模式）
- 支持主/研究/回退三类模型配置，多供应商 API key 接入
- npm CLI 提供 init 与任务管理命令

## 适用场景

- 在 AI 编辑器中从 PRD 生成并管理开发任务
- 通过命令行初始化和管理任务依赖
- 配置多模型切换以控制 API 成本

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  Taskmaster : A task management system for AI-driven development, designed to work seamlessly with any AI chat.
> L76: Taskmaster utilizes AI across several commands, and those require a separate API key. You can use a variety of mode
> L226: Task Master's MCP server supports selective tool loading to reduce context window usage. By default, all 36 tools 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `11156f51babd` · [字段定义](../../DATASET.md)*
