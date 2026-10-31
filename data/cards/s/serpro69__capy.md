# serpro69/capy

⭐ 13 · Go · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/serpro69/capy) · 个人维护

**本地 MCP 服务器：帮编程代理处理大输出、免撑爆上下文**

以 Go 二进制分发的本地 MCP 服务器，面向 Claude Code 与 Codex CLI 编程代理。核心机制：在子进程中执行命令/处理大文件与网页，仅返回摘要或检索结果；索引项目文档并在会话间检索；以加密会话保险库归档、搜索、恢复代理对话。提供 11 个 MCP 工具，支持 JS/TS/Python/Shell/Go/Rust 等多语言执行（依赖本机运行时）。数据库加密为强制项，无遥测/账号/托管服务。限制：Codex 集成仅在 Linux 0.162.1 验证过，捕获执行支持 Linux 与 Apple Silicon（CGO），归档原文保留敏感信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 子进程执行大输出命令/文件/网页，仅返回摘要或检索结果
- 加密会话保险库：归档、搜索、恢复 Claude Code 与 Codex 对话
- 11 个 MCP 工具，含执行捕获、知识索引、检索与统计
- 强制数据库加密，无遥测、账号或托管服务

## 适用场景

- 让编程代理分析大日志/大文件而不占满上下文窗口
- 跨会话保存项目文档并按需检索相关段落
- 归档并事后搜索、恢复编程代理的历史会话

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: capy helps coding agents work with large outputs without filling their context window. It is a local MCP server with
> L11: - **Extract what matters.** Process logs, API responses, web pages, and large files in subprocesses; return summari

## 星数曲线

```mermaid
xychart-beta
    title "serpro69/capy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c8d24693f952` · [字段定义](../../DATASET.md)*
