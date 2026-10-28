# Shiv-aurora/context-compass

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-04-08 · [GitHub](https://github.com/Shiv-aurora/context-compass) · 个人维护

**从 git 历史学习代码关系的上下文引擎，服务 Claude Code**

面向 Claude Code 的 CLI 框架与 MCP 服务器：解析符号/调用/导入，从 git 提交会话中学习共编辑耦合（PMI），通过 MCP 向 Claude 提供紧凑的上下文包，减少文件探索的 token 消耗。提供 economy/balanced/quality 三种检索模式，附 eval 命令可在自有仓库复现召回评估。当前处于 beta，仅支持 Claude Code（Cursor/Windsurf 等计划后续支持），要求 Node>=20 与 git 仓库，索引数据存储在项目本地 .context-compass/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 git 历史学习共编辑耦合（PMI）构建行为级代码关系索引
- 通过 MCP 提供紧凑上下文包，三种检索模式调节 token 与召回
- eval 命令支持在 held-out 会话上复现检索质量评估
- 支持 Python/TypeScript/Go/Rust/Java 等 10 种语言

## 适用场景

- 让 Claude Code 在大型仓库中减少盲目文件探索的 token 消耗
- 基于团队历史编辑行为提升代码检索相关性
- 评估不同检索模式下的召回与 token 节省效果

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Context Compass is a CLI framework for Claude Code that pre-computes behavioral code relationships from git history
> L35: Context Compass parses symbols/calls/imports, learns co-edit coupling from git sessions (PMI), and serves compact c
> L96: - `context-compass serve` — Run MCP server over stdio.

## 星数曲线

```mermaid
xychart-beta
    title "Shiv-aurora/context-compass 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `59e658dfc6aa` · [字段定义](../../DATASET.md)*
