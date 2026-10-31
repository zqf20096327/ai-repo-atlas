# polka-codes/polka-codes

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/polka-codes/polka-codes) · [官网](https://polka.codes) · 组织维护

**TypeScript 多 agent AI 编程助手框架，面向开发者任务规划与代码生成**

基于 TypeScript 与 Bun 的 AI 编程助手框架，以 CLI（polka）提供任务规划（plan）、代码生成（code）、自动修复失败测试（fix）、AI 代码审查（review）、commit/PR 生成、检查点保存与恢复等命令。采用多 agent 协作架构（Architect、Coder 等），支持 Anthropic Claude、Google Vertex、DeepSeek、OpenAI、OpenRouter、Ollama 等多种 AI 提供方，支持 MCP 消费与暴露，可运行 MCP server 将工作流暴露给 Claude Code，并提供 GitHub Actions 集成与 GitHub App runner。运行需要 Bun≥1.0.0 与 ripgrep；项目处于活跃开发期，API 可能演进；TypeScript 自定义脚本目前进程内全权限运行，权限声明仅为预留。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- plan/code/fix/review/commit/pr 等 CLI 命令覆盖开发工作流
- 多 agent 协作架构（Architect、Coder 等专职 agent）
- 支持 6 类 AI 提供方与 MCP 双向集成（消费外部工具、暴露工作流）
- 检查点保存与恢复、GitHub Actions 集成、自定义 TypeScript/shell 脚本

## 适用场景

- 用自然语言让 AI 规划并实现功能、修复失败测试
- 对 PR 或本地改动做 AI 代码审查并自动应用修复
- 通过 MCP 把 Polka 工作流接入 Claude Code 等 agent 客户端
- 在 GitHub Actions 中通过 runner 执行 agent 任务

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L13: Polka Codes is a powerful TypeScript-based AI coding assistant framework that helps developers with task planning, 
> L30: - 🤖 **Multiple AI Providers**: Anthropic Claude, Google Vertex, DeepSeek, OpenAI, OpenRouter, Ollama

## 星数曲线

```mermaid
xychart-beta
    title "polka-codes/polka-codes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `05fd4350325b` · [字段定义](../../DATASET.md)*
