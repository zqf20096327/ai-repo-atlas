# bb-boy680/open-zread

⭐ 45 · TypeScript · MIT · 推送 2026-07-16 · [GitHub](https://github.com/bb-boy680/open-zread) · [官网](https://www.npmjs.com/package/@open-zread/cli) · 个人维护 · 中文 README

**一条命令把代码库生成带图表 Wiki 的 AI 文档工具**

面向开发者的 CLI/TUI 工具：用 LLM 与多 agent 并行读取代码库，生成含 Mermaid 图的 Markdown Wiki。机制上基于 web-tree-sitter 做 14 种语言的 AST 解析，构建三层 Repo Map 控制上下文规模；符号级增量缓存支持 diff 感知的 Wiki 同步，仅重新生成变更页面。自带 32 工具的进程内 Agent SDK、MCP 支持，19 个一线 LLM 提供商加 LiteLLM 动态发现，代码仅在本地运行。npm 全局安装，需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条命令流程：npm 安装后 TUI 配置即生成 Wiki/ 目录
- tree-sitter AST 解析支持 14 种语言
- 符号级增量缓存与 diff 感知 Wiki 同步（new/updated/unchanged/archived）
- 并行页面 agent（p-limit 并发调度）+ 32 工具 Agent SDK，可独立使用

## 适用场景

- 给开源项目自动生成与代码同步的架构 Wiki
- 新人入职快速了解陌生代码库
- 通过 CI 定时重跑保持内部平台/SDK 文档与代码同步
- 收购尽调时快速生成陌生代码库的架构概览

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5:  Turn any codebase into a high-quality Wiki — in a single command.
> L46: - **In-process Agent SDK** — 32 built-in tools (Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, Agent, Ta
> L74: 1. Add an LLM API key (75+ providers supported — OpenAI, Anthropic, DeepSeek, and more).

## 星数曲线

```mermaid
xychart-beta
    title "bb-boy680/open-zread 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-28 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `102a9f931543` · [字段定义](../../DATASET.md)*
