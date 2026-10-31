# sourcebridge-ai/sourcebridge

⭐ 14 · Go · AGPL-3.0 · 推送 2026-06-29 · [GitHub](https://github.com/sourcebridge-ai/sourcebridge) · [官网](https://sourcebridge.ai) · 组织维护

**面向团队的代码库理解平台：生成导读、需求追溯与 AI 评审**

SourceBridge 是一个需求感知的代码库理解平台：用 tree-sitter 解析 12 种语言的代码库，由 LLM 生成 cliff notes、学习路径、代码漫游、架构图等"field guide"；支持从 Markdown/CSV 导入需求并自动关联代码生成追溯矩阵，提供 AI 结构化代码评审、变更影响分析与对话式代码探索。同时作为 MCP server 供 AI agent 接入，并提供 VS Code 扩展、CLI 与 GraphQL API。架构为 Go API server + Python gRPC worker + Next.js 前端，数据存 SurrealDB。OSS 版为单租户模式，多用户仓库隔离需企业版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tree-sitter 索引 12 种语言，生成 cliff notes/学习路径/代码漫游/架构图
- 需求导入（Markdown/CSV）与代码双向追溯、变更影响分析
- 作为 MCP server 接入 AI agent，可为 Claude Code 生成技能卡
- 多 LLM 提供商：云端（Anthropic/OpenAI/Gemini/OpenRouter）或本地（Ollama/vLLM/llama.cpp/SGLang/LM Studio）

## 适用场景

- 新加入团队快速理解陌生代码库的整体结构
- 把需求文档与代码关联并生成追溯矩阵
- 在 VS Code 内直接获得 AI 导读与代码问答
- 为 Claude Code 等 AI agent 提供代码库上下文

## 场景标签

`代码审查` `文档问答` · 领域:编码与开发

## 证据(README 行号)

> L17: SourceBridge is a requirement-aware code comprehension platform. Point it at any codebase and it generates field gu
> L40: - **Field Guides** -- Cliff notes, learning paths, code tours, workflow stories, and system explanations at reposit
> L48: - **Multi-Provider LLM** -- Works with cloud APIs (Anthropic, OpenAI, Gemini, OpenRouter) or fully local inference 

## 星数曲线

```mermaid
xychart-beta
    title "sourcebridge-ai/sourcebridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `fd629e70f875` · [字段定义](../../DATASET.md)*
