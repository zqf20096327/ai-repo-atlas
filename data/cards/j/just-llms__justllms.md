# just-llms/justllms

⭐ 42 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/just-llms/justllms) · [官网](https://www.just-llms.com/) · 组织维护

**多供应商 LLM 统一接口的 Python 编排库**

面向开发者的 Python 库，用单一 API 接入 OpenAI、Anthropic、Google、Azure、xAI、DeepSeek、Ollama 等多家 LLM 供应商。提供一次定义跨供应商通用的工具调用、可配置的静态与失败驱动故障转移链（非流式非工具请求适用）、自动成本追踪与预算上限、基于精确匹配的响应缓存（内存/SQLite 双后端），以及交互式 CLI 并行对比多模型延迟、token 与费用。Ollama 本地部署无需 API key，可经 /api/tags 自动发现已装模型。限制：流式与工具调用请求不参与故障转移与缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套 API 覆盖 7+ 供应商，含 Ollama 本地模型自动发现
- 故障驱动的失败转移链与逐次尝试记录
- 自动成本追踪与预算上限（dict/YAML 配置）
- 内存/SQLite 双后端响应缓存与交互式多模型对比 CLI（justllms sxs）

## 适用场景

- 统一封装多家 LLM 供应商，避免学习各 SDK 差异
- 生产环境配置自动故障转移与预算控制
- 并行对比多个模型的延迟、token 消耗与费用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A production-ready Python library for multi-provider LLM management with a unified API.
> L11: Managing multiple LLM providers is complex. You need to handle different APIs, manage authentication, implement too
> L13: - **Unified Interface**: One API for all providers (OpenAI, Anthropic, Google, Azure, xAI, DeepSeek, Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "just-llms/justllms 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 41 --> 44
    line [43, 42, 42]
```

2026-10-18 43 → 2026-10-26 42（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `65205f3c241c` · [字段定义](../../DATASET.md)*
