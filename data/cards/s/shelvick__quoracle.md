# shelvick/quoracle

⭐ 31 · Elixir · AGPL-3.0 · 推送 2026-04-17 · [GitHub](https://github.com/shelvick/quoracle) · [官网](https://github.com/shelvick/quoracle) · 个人维护

**多 LLM 共识驱动的递归多智能体编排平台**

基于 Phoenix LiveView 的 Web 应用，用于构建层级式智能体系统：每个决策由模型池中多个 LLM 投票共识后执行，Agent 可派生子 Agent、通过消息通信、状态持久化到 PostgreSQL，并通过浏览器实时查看。支持 OpenAI/Anthropic/Google/Azure/Groq 及 Ollama/vLLM 等本地模型（经 ReqLLM，兼容 models.dev 所列），API key 以 AES-256-GCM 加密存储。提供 Docker、源码与自包含 release 三种部署方式。README 明确不适用于简单聊天、单模型流程与无人监督的生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个决策由多模型池投票共识后执行，可配置 0-9 轮精炼迭代
- Agent 可递归派生子 Agent，状态持久化到 PostgreSQL，浏览器实时可见
- 支持多种云端提供商及 Ollama/vLLM/LM Studio/LlamaCpp 本地端点
- 配置项覆盖模型角色（嵌入/回答/摘要/图像生成）、能力组与 USD 预算上限

## 适用场景

- 我想让三个不同厂商的 LLM 共同审议再执行复杂任务
- 我想实验多智能体递归编排与共识机制
- 我需要浏览器界面实时观察智能体的决策与状态

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Recursive agent orchestration with multi-LLM consensus.
> L5: Quoracle is a Phoenix LiveView application that lets you build hierarchical agent systems where _every decision_ is 
> L9: **What this is for:** Exploring multi-agent orchestration, experimenting with consensus-driven AI, and running compl

## 星数曲线

```mermaid
xychart-beta
    title "shelvick/quoracle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `57c825e9bd7a` · [字段定义](../../DATASET.md)*
