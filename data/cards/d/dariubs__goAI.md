# dariubs/goAI

⭐ 40 · Go · 推送 2026-01-05 · [GitHub](https://github.com/dariubs/goAI) · 个人维护

**Go 开发者的多 LLM 提供商统一调用库**

用 Go 标准库实现的 LLM 客户端库：一个 client 一个 Chat 方法，统一接入 OpenAI、Anthropic、Google、xAI、Mistral、Perplexity、Ollama 共 7 家提供商。通过 Options 模式配置 API key、endpoint、超时（默认 60s）、max tokens（默认 500）与 temperature（默认 0.7）。提供带 provider 上下文的类型化错误（如 ErrNoAPIKey、ErrProviderNotFound）与 context 取消处理。零第三方依赖，仅用标准库；新提供商通过实现内部 Provider 接口并在 init() 中自注册接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 接入 7 家 LLM 提供商（含本地 Ollama）
- 零第三方依赖，仅标准库
- 类型化错误与哨兵错误（ErrNoAPIKey 等）
- 通过 init() 自注册扩展新提供商

## 适用场景

- Go 项目中切换或并用多家 LLM 提供商
- 通过 Ollama endpoint 调用本地模型
- 在统一错误处理下构建多提供商调用逻辑

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A simple, modern, and reliable Go library for interacting with multiple LLM providers
> L9: - **7 Providers** - OpenAI, Anthropic, Google, xAI, Mistral, Perplexity, Ollama
> L203: To add a new LLM provider:

## 星数曲线

```mermaid
xychart-beta
    title "dariubs/goAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-29 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cecff02c1788` · [字段定义](../../DATASET.md)*
