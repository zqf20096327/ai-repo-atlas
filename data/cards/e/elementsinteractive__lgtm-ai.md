# elementsinteractive/lgtm-ai

⭐ 25 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/elementsinteractive/lgtm-ai) · [官网](https://www.elements.nl) · 组织维护

**用 LLM 生成代码审查与审查指南的 CLI 工具**

面向开发者的 AI 代码审查工具：读取 GitHub/GitLab 的 Pull/Merge Request（或本地变更），交给多个 AI agent 生成带评分（LGTM 到 Abandon 五档）与分类内联评论（正确性/质量/测试/安全）的审查报告，或生成给人工审查者的指南；可用 --publish 发布为 PR 评论。模型完全可配置，支持 OpenAI、Gemini、Claude、Mistral、DeepSeek 及任何 OpenAI 兼容的本地模型（如 Ollama）。以 pip 包与 Docker 镜像分发，可作为 MCP server 供 Claude Desktop、VS Code Copilot 使用，并提供 GitLab CI 步骤与 GitHub Action 集成；DeepSeek 目前仅支持官方 API 地址，可关联 GitHub/GitLab/JIRA issue 作为审查上下文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 PR 生成分档评分与四类内联评论（含三级严重度）的代码审查
- 支持 OpenAI/Gemini/Claude/Mistral/DeepSeek 及 OpenAI 兼容本地模型
- 可作为 MCP server 供 Claude Desktop、VS Code Copilot 等工具调用
- 可关联 GitHub/GitLab/JIRA issue 内容作为审查上下文

## 适用场景

- 在 CI 流水线中自动生成 PR 代码审查评论
- 为人工审查者生成上下文相关的 reviewer guide
- 在不发送 PR 的情况下审查本地 git 变更
- 通过 MCP 在编辑器内按需触发代码审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: lgtm-ai is your AI-powered code review companion. It generates code reviews using your favorite LLMs and helps huma
> L96: lgtm reads the given pull request and feeds it to several AI agents to generate a code review or a reviewer guide. 

## 星数曲线

```mermaid
xychart-beta
    title "elementsinteractive/lgtm-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d7c9d3c2d836` · [字段定义](../../DATASET.md)*
