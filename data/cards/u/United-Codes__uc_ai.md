# United-Codes/uc_ai

⭐ 49 · PLSQL · LGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/United-Codes/uc_ai) · [官网](https://www.united-codes.com/products/uc-ai/docs) · 组织维护

**Oracle PL/SQL 的 AI 集成框架：数据库内调用 LLM 与函数**

面向 Oracle 开发者的 PL/SQL 框架，用于在数据库内直接调用 OpenAI GPT、Anthropic Claude、Google Gemini、Ollama 等 AI 模型，并提供工具系统支持 AI 通过函数调用（function calling）执行数据库函数。作者定位为不依赖 Oracle 23ai 数据库（当前仅云端提供）即可在自有 Oracle 数据库中接入 LLM。提供安装指南、文档与介绍视频，以 PL/SQL 代码形式调用，文本生成等 API 见官方文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PL/SQL 内直接调用多家 LLM 提供商（OpenAI/Anthropic/Gemini/Ollama 等）
- 结构化工具系统支持 AI 执行数据库函数（function calling）
- 不要求 Oracle 23ai/26ai 数据库版本

## 适用场景

- 在 Oracle 数据库内为业务逻辑添加 AI 文本生成能力
- 让 LLM 通过函数调用直接操作数据库函数
- 无法升级 23ai 的 Oracle 环境中接入 AI 模型

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A comprehensive Oracle PL/SQL framework for integrating AI models (OpenAI GPT, Anthropic Claude, Google Gemini, Olla
> L13: The most important part of AI integration is really just calling an **API** to access Large Language Models (LLMs).

## 星数曲线

```mermaid
xychart-beta
    title "United-Codes/uc_ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `caf65b15349b` · [字段定义](../../DATASET.md)*
