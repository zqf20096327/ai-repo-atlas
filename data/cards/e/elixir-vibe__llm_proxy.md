# elixir-vibe/llm_proxy

⭐ 27 · Elixir · MIT · 推送 2026-10-22 · [GitHub](https://github.com/elixir-vibe/llm_proxy) · [官网](https://hexdocs.pm/llm_proxy) · 个人维护

**Elixir 自托管 LLM 网关：多供应商路由、降级与预算管控**

以 Elixir/OTP 实现的自托管 LLM 代理网关，定位为 LiteLLM 的替代：在 OpenAI、Anthropic、OpenRouter、OpenAI Codex 及自定义 OpenAI 兼容端点前提供统一 API。应用请求 fast/smart 等别名，由网关集中配置路由目标，支持有序/加权/最低成本/延迟感知等策略、熔断与降级、按 key 的配额与预算限制、凭证池管理及用量成本记录。可嵌入 Elixir 应用（库模式）或作为独立 OTP 服务运行（DuckDB 存储），提供 OpenTelemetry 追踪。需 Elixir 1.17+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商路由：ordered/shuffle/round_robin/weighted/lowest_cost/latency_aware 六种策略
- 按应用/客户/团队发放 key，模型访问、并发、token 与美元预算限制
- 支持 OpenAI Chat Completions/Responses 与 Anthropic Messages 协议
- 库模式嵌入 Phoenix 或独立 OTP 服务运行，OpenTelemetry 追踪

## 适用场景

- 统一多个 LLM 供应商的接入，切换供应商不改客户端代码
- 为多团队/多应用集中管理凭证、配额与支出
- 供应商故障时自动降级与熔断保持服务可用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: A self-hosted, Elixir-native alternative to LiteLLM. Put one API in front of OpenAI, Anthropic, OpenRouter, Kimi Cod
> L29: - **Connect your applications once.** Point any OpenAI-compatible client at LLMProxy, use the Anthropic Messages AP
> L34: - **Self-host without adding a Python control plane.** Run the bundled OTP service as a LiteLLM-style gateway, or e

## 星数曲线

```mermaid
xychart-beta
    title "elixir-vibe/llm_proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `75a96f1b2dbd` · [字段定义](../../DATASET.md)*
