# newlc/ai-code-reviewer

⭐ 19 · TypeScript · MIT · 推送 2025-12-07 · [GitHub](https://github.com/newlc/ai-code-reviewer) · 个人维护

**AI 自动审查 Pull Request 的 GitHub Action**

以 GitHub Action 形式运行的自动化代码审查工具：在 Pull Request 上分析代码变更，输出总体摘要评论与针对具体行的行内评论，查找潜在 bug 与安全问题并给出改进建议。支持 OpenAI、Anthropic（Claude）、Grok、Gemini 及本地 Ollama 等多种 AI 提供方，可自定义提示词、忽略模式与关注领域，评论语言支持英/俄/西/中/日等八种，可选在发现严重问题时使 Action 失败以阻止合并。至少需配置一个 AI 提供方（API key 或 Ollama URL）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 OpenAI / Anthropic / Grok / Gemini / 本地 Ollama 多提供方
- 总体摘要 + 行内评论两种输出形式
- fail-on-critical 可在发现严重问题时阻止 PR
- 自定义配置文件：审查模式、语言、忽略模式等

## 适用场景

- 在 Pull Request 流程中自动获得 AI 代码审查评论
- 用本地 Ollama 模型做不外发代码的审查
- 按严重问题自动阻止有风险的 PR 合并

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: **AI Code Reviewer** is a GitHub Action that automatically reviews your pull requests using AI. It analyzes code cha
> L12: - **Multiple AI Providers**: OpenAI, Anthropic (Claude), Grok, Gemini, Ollama

## 星数曲线

```mermaid
xychart-beta
    title "newlc/ai-code-reviewer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `22035b55fd7e` · [字段定义](../../DATASET.md)*
