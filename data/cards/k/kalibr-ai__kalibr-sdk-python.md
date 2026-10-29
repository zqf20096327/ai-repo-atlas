# kalibr-ai/kalibr-sdk-python

⭐ 32 · Python · Apache-2.0 · 推送 2026-06-03 · [GitHub](https://github.com/kalibr-ai/kalibr-sdk-python) · [官网](https://kalibr.systems) · 组织维护

**面向开发者：为 agent 管道做模型/执行路径路由与自动修复的 Python SDK**

Kalibr Python SDK 在应用与 LLM 提供商之间提供路由层：按目标（goal）将请求路由到模型+工具+参数组合的执行路径，用 Thompson Sampling 基于真实结果反馈学习路由；提供自愈执行环（元提示生成、结构化评估、LLM judge 失败分类、提示修复或换模型重试），以及 OpenAI/Anthropic/Google/DeepSeek/HuggingFace SDK 的零代码自动插桩与追踪。支持多步 pipeline、Insights API 查询学习结果，并提供 LangChain/CrewAI/OpenAI Agents SDK/LiveKit/Pipecat 集成。开源 SDK 配合托管的 routing intelligence 服务，需要 KALIBR_API_KEY 与租户 ID。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Thompson Sampling 基于真实结果反馈选择模型+工具+参数执行路径
- 自愈执行环：元提示生成、结构化评估、LLM judge 失败分类、修复或换模型重试
- 零代码自动插桩追踪 OpenAI/Anthropic/Google/DeepSeek/HuggingFace 调用（17 种任务类型）
- 提供 LangChain/CrewAI/OpenAI Agents SDK/LiveKit/Pipecat 框架集成

## 适用场景

- 降低 agent 管道的推理成本，把简单请求路由到更便宜的模型
- 模型或工具退化时自动切换到可用路径，保持管道运行
- 对生产 agent 的调用做成本追踪与路由决策审计
- 构建多步 pipeline 并在各步骤应用自动修复

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L3: The self-healing execution harness for agent pipelines. Every model call gets a task-specific meta prompt, automatic
> L13: * **Routes to lower-cost paths automatically** — Simple requests move to cheaper models. Hard requests stay on stro
> L20: * **Framework integrations** — LangChain, CrewAI, OpenAI Agents SDK, LiveKit, Pipecat.

## 星数曲线

```mermaid
xychart-beta
    title "kalibr-ai/kalibr-sdk-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `428828577a05` · [字段定义](../../DATASET.md)*
