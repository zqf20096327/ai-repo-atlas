# cognesy/instructor-php

⭐ 328 · PHP · MIT · 推送 2026-10-14 · [GitHub](https://github.com/cognesy/instructor-php) · [官网](https://instructorphp.com) · 组织维护

**PHP 的 LLM 结构化输出、统一推理 API 与 Agent SDK 组件库**

面向 PHP 开发者的 monorepo，含四类组件：Instructor 从文本/图像/聊天序列中抽取经过验证的类型化 PHP 对象，支持 JSON/JsonSchema/Tools/MdJson 等多种输出模式、校验失败自动重试；Polyglot 提供统一推理层，通过一套 API 调用 20+ LLM 提供商，并含异步批处理（Early Access）、嵌入与类型化决策 API；Retrieval 提供向量存储与 RAG 证据上下文；Agent SDK 用于构建工具调用型 agent。另有 Laravel 与 Symfony 一方集成包。经 Composer 安装，框架无关。受 Python 版 Instructor 启发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 结构化输出 + 校验 + 自动重试（利用校验错误供模型自我修正）
- Polyglot 统一 API 支持 20+ 提供商（OpenAI/Anthropic/Gemini/Ollama/OpenRouter 等）
- Agent SDK 支持自定义工具、子 agent、生命周期钩子与事件观测
- 可从 PHP 驱动外部编码 agent（Codex、Claude Code、OpenCode）

## 适用场景

- 在 PHP 项目中让 LLM 返回可验证的类型化数据
- 同一套代码在多个 LLM 提供商之间切换
- 构建带工具调用的 agent 与 RAG 检索流程

## 场景标签

`Agent 框架` `RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: - **Instructor for PHP** - structured data extraction in PHP - powered by LLMs, designed for simplicity, transparenc
> L6: - **Polyglot for PHP** - unified inference, asynchronous batch inference (Early Access), embeddings, and typed decis
> L228: Instructor ecosystem uses Polyglot as an unified inference API layer supporting 20+ LLM providers.

## 星数曲线

```mermaid
xychart-beta
    title "cognesy/instructor-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 327 --> 329
    line [328, 328]
```

2026-10-18 328 → 2026-10-26 328（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `bfc587153e3d` · [字段定义](../../DATASET.md)*
