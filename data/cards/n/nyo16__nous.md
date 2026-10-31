# nyo16/nous

⭐ 14 · Elixir · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/nyo16/nous) · 个人维护

**Elixir 的 AI agent 框架：一个字符串切换 13 家 LLM 供应商**

面向 BEAM/Elixir 生态的 AI agent 框架。以 `provider:model` 单一字符串接入 13 个 LLM 供应商（OpenAI、Anthropic、Gemini、Ollama、vLLM、LlamaCpp 等及任意 OpenAI 兼容端点）。Agent 作为 OTP 受监督进程运行，具备崩溃恢复、流式背压与传输层错误的自动回退链。内置工具调用、结构化输出（Ecto schema）、技能、插件、混合记忆、DAG 工作流、知识库与评测等功能。要求 Elixir 1.18+ 与 OTP 27+，通过 mix 依赖安装；Bash 工具与 command 钩子需可选依赖 net_runner，否则拒绝执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个 `provider:model` 字符串切换 13 个 LLM 供应商及自定义 OpenAI 兼容端点
- Agent 以 OTP 受监督进程运行，含崩溃恢复与流式拉取背压
- 传输层错误自动触发 fallback 链切换备用模型
- 内置工具调用、结构化输出（Ecto）、21 个技能、混合记忆、DAG 工作流与 LiveView 集成

## 适用场景

- 在 Elixir/Phoenix 应用中构建带工具调用的 AI agent
- 通过统一接口在云 API 与本地运行时（Ollama/LM Studio/vLLM）间切换
- 构建需要审批、守卫与监督恢复的多 agent 工作流

## 场景标签

`Agent 框架` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: AI agent framework for Elixir with multi-provider LLM support.
> L16: A production-grade AI agent framework for the BEAM. Three things you get:
> L18: - **One string, 13 providers.** Swap OpenAI for Anthropic, Gemini, Vertex AI,

## 星数曲线

```mermaid
xychart-beta
    title "nyo16/nous 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5740fbcdcf88` · [字段定义](../../DATASET.md)*
