# Monan-AI/monan-sdk

⭐ 48 · TypeScript · MIT · 推送 2025-12-21 · [GitHub](https://github.com/Monan-AI/monan-sdk) · 组织维护

**基于 Bun 的 AI Agent 框架：本地推理、向量存储与 API 部署一体**

面向 Bun/TypeScript 开发者的 Agent 构建框架：代码中定义 Agent，由 CLI 负责执行，支持终端交互测试与一键启动 Elysia API 服务器。本地模型通过 Ollama 接入（需先运行 ollama serve），云端通过 OpenRouter 访问 OpenAI/Anthropic 等并默认启用 PII 脱敏。内置 SQLite 向量存储与 Hugging Face 嵌入实现本地 RAG，提供 Zod 类型安全的工具系统、Router 模型路由、HyperAgent 多智能体编排与工作流引擎。声明处于 Alpha 开发阶段，另设 Community（免费）/Enterprise 付费方案，后者含审计日志与 SSO 等治理功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI 管理执行：交互测试与一键部署 Elysia API 服务器
- Ollama 本地模型接入，支持 LoRA/QLoRA 适配器自定义模型
- SQLite 向量存储 + Hugging Face 嵌入的本地 RAG
- Zod 类型安全工具系统与 HyperAgent Plan-Delegate-Synthesize 编排

## 适用场景

- 用 TypeScript 在本地构建并部署 AI Agent API
- 无 GPU 环境下经 OpenRouter 使用云端模型并自动脱敏 PII
- 为本地小模型挂载 LoRA 适配器实现领域专用 Agent
- 多 Agent 路由与工作流编排处理复杂任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Monan** is a framework designed to eliminate the latency and complexity of AI orchestration. Unlike Python-based 
> L31: In Monan, you define your agent in code, but execution (Chat or API) is managed by the CLI. This ensures optimizati

## 星数曲线

```mermaid
xychart-beta
    title "Monan-AI/monan-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2b289c0853d3` · [字段定义](../../DATASET.md)*
