# atlas-php/atlas

⭐ 55 · PHP · MIT · 推送 2026-07-21 · [GitHub](https://github.com/atlas-php/atlas) · [官网](http://atlasphp.org/) · 组织维护

**面向 Laravel 的统一 AI SDK：构建 agent、工具并接入多家模型服务商**

面向 Laravel 11+ 的 PHP AI SDK，提供统一 API 接入 OpenAI、Anthropic、Google、xAI、ElevenLabs、Cohere、Jina 及任意 OpenAI 兼容端点（Ollama、DeepSeek、Groq 等）。SDK 自身运行工具调用循环，包含 agent 框架（子 agent、并行扇出、执行树审计）、10 种模态（文本/图像/音频/视频/实时语音/嵌入/重排/审核等）、可选持久化（对话记忆、执行跟踪、S3/本地媒体资产）与中间件。默认无状态运行、无需数据库。通过 composer 安装，各 provider 模态经真实 API 实测。

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

- 统一 API 接入多家服务商，切换仅需改字符串
- 10 种模态：文本、图像、音频、音乐、视频、实时语音、嵌入、重排、审核等
- agent 框架：子 agent（深度/循环守卫、并行扇出）、执行树审计、四层中间件
- 可选持久化：对话记忆、执行跟踪、媒体资产（S3/本地），默认无状态无需数据库

## 适用场景

- 在 Laravel 应用中构建带工具调用的 AI agent
- 多服务商之间切换模型而不改动业务代码
- 为多轮对话应用增加记忆、执行追踪与重试分支

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L22: **A unified AI SDK for Laravel — agents, tools, and 10 modalities across every major provider.**
> L24: One API for OpenAI, Anthropic, Google, xAI, ElevenLabs, and any OpenAI-compatible endpoint — with no external AI de

## 星数曲线

```mermaid
xychart-beta
    title "atlas-php/atlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-25 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `806faf5d0e54` · [字段定义](../../DATASET.md)*
