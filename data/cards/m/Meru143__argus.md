# Meru143/argus

⭐ 18 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Meru143/argus) · [官网](https://merup.me/argus/) · 个人维护

**本地优先的 AI 代码审查平台：让独立 AI 审查 AI 生成代码**

Rust 编写的本地优先 AI 代码审查工具，面向希望独立审查 AI 代理所写代码的团队。核心机制：结合 tree-sitter+PageRank 结构地图、混合语义搜索、git 历史分析（热点/耦合/巴士因子）与 LLM 审查，使评论基于完整代码库而非仅 diff。提供单一二进制与 11 个子命令，含 MCP server，可接入 Claude Code/Cursor/Windsurf。LLM 支持 Gemini/OpenAI/Anthropic/Ollama 及自定义 base_url；Gemini 免费层提示词可能被 Google 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结构地图+语义搜索+git 历史+LLM 的上下文感知审查
- 11 个 Unix 风格子命令，含 MCP server
- 支持 Gemini/OpenAI/Anthropic/Ollama 与自定义 OpenAI 兼容端点
- 自然语言自定义规则（.argus/rules.md）与反馈训练

## 适用场景

- 让独立 AI 审查 AI 编码代理产生的 diff 或 PR
- 在 GitHub Action 中自动审查 PR 并回贴评论
- 分析代码库结构热点与巴士因子风险

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Argus is a local-first AI code review platform for teams that want an independent reviewer, not a model grading its
> L68: ### `review` — AI Code Review

## 星数曲线

```mermaid
xychart-beta
    title "Meru143/argus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `664ecbf83e91` · [字段定义](../../DATASET.md)*
