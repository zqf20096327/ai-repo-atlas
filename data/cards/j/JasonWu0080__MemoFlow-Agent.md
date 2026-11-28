# JasonWu0080/MemoFlow-Agent

⭐ 3 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/JasonWu0080/MemoFlow-Agent) · 组织维护 · 中文 README

**面向开发者的轻量 Python AI agent 框架：模型驱动工具调用与持久化执行**

从 MemoFlow 应用中抽出的独立 agent 内核包，提供单一 agent 循环：每轮由模型决定回答、调用工具或向用户提问，决策依赖 provider 原生 tool-calling 协议。权限、预算与运行状态由代码而非模型决定；工具带类型化 JSON schema、风险与副作用元数据；支持人工审批（绑定单次调用与参数哈希）、澄清问答、预算计数、流式事件与基于 PostgreSQL 的可选持久化执行（检查点、租约、崩溃恢复）。Python 3.11+，v0.1.0 alpha，API 可能变动；不含多 agent 编排、内置 RAG 或浏览器/shell 工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 agent 循环，决策仅依赖 provider 原生 tool-calling 协议
- 基于能力的权限策略与一次性、可过期的人工审批机制
- 可选 PostgreSQL 持久化：检查点、租约、崩溃恢复与幂等副作用语义
- OpenAI、Anthropic、DeepSeek 三个 provider，约 50 行可新增 provider

## 适用场景

- 为业务应用构建需要人工审批高风险工具调用的 agent
- 需要崩溃恢复与可回放事件流的长时间运行 agent 任务
- 对工具副作用做至多一次（at-most-once）语义保证的场景

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A lightweight, extensible Python AI agent framework with model-driven tool calling, durable execution,
> L33: - **Providers:** OpenAI, Anthropic and DeepSeek. Adding another takes about 50 lines.
> L93: |`openai:`|`OpenAIProvider`|Chat Completions, streaming, native tools|

## 星数曲线

```mermaid
xychart-beta
    title "JasonWu0080/MemoFlow-Agent 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2213e775a1e7` · [字段定义](../../DATASET.md)*
