# brunocapelao/miniAutoGen

⭐ 29 · Python · MIT · 推送 2026-05-17 · [GitHub](https://github.com/brunocapelao/miniAutoGen) · 个人维护

**构建多智能体系统的 Python 微内核编排库**

Python 微内核库，用于编排流水线与异步多智能体协调：提供类型化契约（Pydantic/Protocol）、PipelineRunner 运行时、5 个专用 store（InMemory/SQLAlchemy 后端）、11 个横切策略（budget/retry/timeout/semantic_cache 等）、72 类事件观测。支持 5 种协调模式（Workflow、Deliberation、Agentic loop、Team、Composite）。通过 AgentAPIDriver 接入 OpenAI 兼容端点（Gemini CLI gateway、LiteLLM、vLLM、Ollama），附带 16 命令 CLI、Web Console 与 Docker 部署。全异步基于 AnyIO，README 为葡萄牙语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种多智能体协调模式（Workflow/Deliberation/Agentic loop/Team/Composite）
- 11 个横切策略与 72 类事件的可观测性
- AgentAPIDriver 统一接入 OpenAI 兼容端点（Ollama/vLLM/LiteLLM/Gemini CLI gateway）
- 16 命令 CLI、Web Console dashboard 与 docker-compose 部署

## 适用场景

- 编排多智能体工作流与团队协作流水线
- 通过 Web Console 实时观察与控制 agent 运行
- 在可替换的 LLM 后端之上构建多智能体应用

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Biblioteca Python de microkernel para orquestração de pipelines e coordenação multi-agente assíncrona.
> L16: O MiniAutoGen fornece contratos tipados, runtimes de coordenação e policies transversais para construir sistemas mu
> L84: - `AgentAPIDriver` -- driver HTTP para endpoints OpenAI-compatible (Gemini CLI gateway, LiteLLM, vLLM, Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "brunocapelao/miniAutoGen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `68492d137b57` · [字段定义](../../DATASET.md)*
