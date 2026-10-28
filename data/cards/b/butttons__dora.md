# butttons/dora

⭐ 109 · TypeScript · MIT · 推送 2026-03-10 · [GitHub](https://github.com/butttons/dora) · [官网](https://dora-cli.dev) · 个人维护

**把 SCIP 索引转为 SQLite 供 AI agent 查询代码库的 CLI**

面向 AI agent 与开发者的命令行工具：将 SCIP 索引（由 scip-typescript 等索引器生成）解析并载入 SQLite，提供符号查找、引用追踪、依赖/反向依赖、循环依赖、耦合度与复杂度等毫秒级查询，替代 grep/find 式多步探索。另有 Tree-sitter 层（TypeScript/JavaScript）直接解析源码提取函数签名、圈复杂度与代码异味；输出默认采用面向 LLM token 优化的 TOON 编码，并可启动 MCP server 供 Claude Code 等 agent 接入。安装方式为下载二进制或经 Bun 的 npm 包，需自行安装对应语言的 SCIP 索引器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SCIP 索引转 SQLite，符号/引用/依赖查询毫秒级返回
- Tree-sitter 层提取函数签名、圈复杂度、代码异味（TS/JS）
- 默认输出 TOON 编码，优化 LLM token 用量
- 内置 MCP server（stdio），支持 Claude Code/OpenCode/Cursor/Windsurf 集成

## 适用场景

- 让 AI agent 结构化理解大型代码库，减少读文件与 grep 的 token 消耗
- 分析文件依赖关系、循环依赖与耦合热点
- 通过 MCP 或 CLI 查询符号引用与定义位置

## 场景标签

 · 领域:开发工具/代码智能

## 证据(README 行号)

> L3: A CLI that turns a SCIP index into a queryable SQLite database. Gives AI agents structured answers about your codeba
> L139: For agent-specific setup (hooks, skills, AGENTS.md snippets) for Claude Code, OpenCode, Cursor, and Windsurf:
> L122: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "butttons/dora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-28 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fbe6f58ee816` · [字段定义](../../DATASET.md)*
