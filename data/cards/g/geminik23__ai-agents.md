# geminik23/ai-agents

⭐ 38 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/geminik23/ai-agents) · [官网](https://ai-agents.rs) · 个人维护

**Rust 声明式 AI agent 框架：一份 YAML 定义并运行 agent**

Rust 编写的 AI agent 构建框架，通过单一 YAML 规范定义 agent，常见场景无需编码，另提供 Rust API 嵌入。支持 12 个 LLM 提供商（含 OpenAI/Anthropic/Google/Ollama 等）并带自动回退；内置 30 个工具与 MCP 接入；提供状态机、技能、记忆栈（Redis/SQLite 快照，Redis 存储标注为实验性）、多 agent 编排、HITL 审批与 fail-closed 工具授权。含 CLI/TUI、YAML 场景评测与 Prometheus 等可观测性导出。需 Rust 1.88+，Retrieval/RAG、Python 绑定等仍在规划中未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 YAML 定义 agent，CLI 直接运行，常见场景无需编码
- 12 个 LLM 提供商接入与自动回退，支持自定义 provider trait
- 30 个内置工具 + MCP 服务器接入
- fail-closed 工具授权、HITL 审批与 YAML 场景评测

## 适用场景

- 用一份 YAML 快速定义并运行带工具与状态机的 agent
- 在 Rust 应用中嵌入多 LLM agent 与多 agent 编排
- 对 agent 行为做场景化评测与可观测性追踪

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: A Rust framework for building AI agents from a single YAML specification. No code required for common use cases.
> L24: - **Multi-LLM with fallback** - 12 providers (OpenAI, Anthropic, Google, Ollama, DeepSeek, Groq, Mistral, Cohere, x

## 星数曲线

```mermaid
xychart-beta
    title "geminik23/ai-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `019512e7575e` · [字段定义](../../DATASET.md)*
