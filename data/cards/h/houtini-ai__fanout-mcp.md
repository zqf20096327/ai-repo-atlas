# houtini-ai/fanout-mcp

⭐ 13 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/houtini-ai/fanout-mcp) · [官网](https://houtini.com) · 组织维护

**面向 AI 搜索时代的内容查询覆盖缺口分析 MCP 服务器**

一个 MCP 服务器工具：读取指定 URL 的内容，基于 Google 查询扇出专利方法（US 11663201 B2）生成查询变体，评估内容对每条查询的覆盖情况（COVERED/PARTIAL/GAP），给出带原文证据的评估、覆盖分数与改进建议，用于 Generative Engine Optimization（GEO）。提供内容分析、混合分析、关键词分析三种模式，支持 5 种默认变体类型（可扩展至 8 种）与上下文信号（购物/研究意图、时间语境）。需 MCP 兼容客户端（如 Claude Desktop）与 Anthropic API key，通过 npx 运行，无需本地构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Google 扇出专利方法生成 5-8 种类型查询变体（默认 15-25 条）
- 覆盖评估附带原文逐字证据（Self-RAG 校验，声明零幻觉率）
- 输出覆盖分数（0-100）、缺口清单与优先级建议
- 支持购物/研究意图与时间语境的上下文感知变体生成

## 适用场景

- 我想知道自己的文章能回答哪些用户查询、漏掉了哪些
- 针对目标关键词检查内容的关键词变体覆盖情况
- 优化内容以提升在 ChatGPT、Perplexity 等 AI 搜索中的被引用机会

## 场景标签

 · 领域:SEO/AI 搜索内容优化

## 证据(README 行号)

> L81: - Claude Desktop (or any MCP-compatible client)
> L108: claude mcp add -e ANTHROPIC_API_KEY=sk-ant-... -s user fanout -- npx -y @houtini/fanout-mcp@latest

## 星数曲线

```mermaid
xychart-beta
    title "houtini-ai/fanout-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2f764086c3cf` · [字段定义](../../DATASET.md)*
