# ueberdosis/ai-agent-custom-llm-demos

⭐ 20 · JavaScript · MIT · 推送 2025-11-20 · [GitHub](https://github.com/ueberdosis/ai-agent-custom-llm-demos) · [官网](https://tiptap.dev/docs/content-ai/capabilities/agent/custom-llms/overview) · 组织维护

**给开发者的 Tiptap AI Agent 自定义后端接入示例集**

由 Tiptap 团队（ueberdosis）提供的 Next.js 示例工程，演示如何将 Tiptap AI Agent 富文本编辑器扩展接入自定义后端与 AI 模型提供商。含三类示例（基础集成、客户端工具、服务端工具），每类覆盖四种适配器：Vercel AI SDK、OpenAI Responses API、OpenAI Chat Completions API、Anthropic Claude Messages API。依赖 Tiptap 私有 npm 仓库认证与 API key。README 顶部声明 AI Agent 扩展已弃用，应迁移至 AI Toolkit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类示例 × 四种适配器（Vercel AI SDK/OpenAI Responses/OpenAI Chat Completions/Anthropic）
- 演示客户端工具（Replace Tool）与服务端工具（Weather Tool）实现
- 统一三层架构：React+Tiptap 前端 → Next.js Server Actions 后端 → LLM 提供商

## 适用场景

- 为 Tiptap 编辑器接入自有后端和自选 LLM 提供商
- 学习编辑器场景下的工具调用（客户端/服务端）实现模式
- 对比不同 LLM 提供商 API 的适配差异

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: A comprehensive Next.js project showcasing how to integrate the Tiptap AI Agent extension with a custom backend and 
> L45: This repository contains three categories of demos, each with implementations for all four supported adapters:

## 星数曲线

```mermaid
xychart-beta
    title "ueberdosis/ai-agent-custom-llm-demos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5b2d85688272` · [字段定义](../../DATASET.md)*
