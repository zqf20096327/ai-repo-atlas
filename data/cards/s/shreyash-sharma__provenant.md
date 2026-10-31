# shreyash-sharma/provenant

⭐ 16 · Python · 推送 2026-08-10 · [GitHub](https://github.com/shreyash-sharma/provenant) · [官网](https://www.shreyashsharma.com/writing/provenant) · 个人维护

**给 AI 编程 agent 的本地代码库记忆与检索层（CLI + MCP）**

面向 AI 编程 agent 的本地代码库记忆层，以 CLI 与 MCP server 形式提供。它读取 Git 仓库，用 tree-sitter 解析生成 wiki 页面、符号与依赖图、git 历史考古、死代码检测与风险评分，通过 8 个 MCP 工具向 Claude Code、Cursor、Copilot 等兼容客户端输出带引用的检索上下文。在 SWE-bench Verified 上评估 File Coverage@5 63.8%、上下文体积较原始文件加载降低 60-65 倍。默认本地运行，索引存于 .provenant/，wiki 生成与回答合成需配置一个 LLM provider 的 API key（Anthropic/OpenAI/DeepSeek/Gemini），也可用本地 embedder。另含本地 web dashboard、monorepo 支持与可选 ccusage 用量统计。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter 解析 15+ 语言，生成英文 wiki 页面与符号/依赖图
- 8 个 MCP 工具：检索问答、符号定位、死代码、风险评分、git 考古等
- SWE-bench Verified 评估：File Coverage@5 63.8%，上下文体积降低 60-65 倍
- 低置信度答案触发后台 wiki 修复的自愈检索机制

## 适用场景

- 编程 agent 反复打开大量文件时，改用带引用的聚焦上下文
- 在编辑大型、有历史包袱的仓库前了解风险模块、死代码与依赖结构
- 用 git 历史回答某段代码为何存在
- 跨 Claude Code/Cursor/Cline 等编辑器复用同一代码库记忆层

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L40: Provenant is a Command Line Interface (CLI) and MCP server designed to give AI coding agents a local memory layer f
> L71:  🔌 MCP-native Eight tools for Claude Code, Cursor, Windsurf, Cline, and other MCP-compatible clients.
> L16:  symbol context, git archaeology, dead-code signals, and risk-aware answers through MCP.

## 星数曲线

```mermaid
xychart-beta
    title "shreyash-sharma/provenant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `daf4418d999b` · [字段定义](../../DATASET.md)*
