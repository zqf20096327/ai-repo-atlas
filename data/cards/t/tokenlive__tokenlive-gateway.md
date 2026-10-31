# tokenlive/tokenlive-gateway

⭐ 14 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/tokenlive/tokenlive-gateway) · [官网](https://www.tokenlive.net) · 组织维护 · 中文 README

**面向企业 LLM 生态的 Go 语言 API 网关，提供流量治理与计费**

用 Go 实现的 LLM API 网关，采用 Gin 外壳 + Engine 管道架构。暴露 OpenAI 兼容统一 API（Chat/Embeddings/Images），内置 OpenAI、Anthropic 等上游厂商接入与模型名改写、加权路由。提供双层熔断、8 种负载均衡、四级策略覆盖、SSE 流量拦截计费与差量退款、Redis 补偿队列；支持 No-Redis 模式（本地/HTTP 配置源 + 内存状态存储）。适配 Claude Code、Codex 等 agent 工具的跨协议翻译。部署途径含源码编译、Homebrew（macOS）与 tokenlive-deploy 统一部署项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容统一 API，内置 OpenAI/Anthropic 多厂商接入与加权路由
- 双层熔断、8 种负载均衡算法与智能重试（指数抖动退避）
- SSE 拦截计费：预分配配额 + 按实际 token 差量退款
- Claude Code / Codex 等 agent 工具的跨协议透明翻译

## 适用场景

- 高并发生产环境下统一接入与管理多家 LLM 上游
- 对多租户按 user+model 维度做限流、鉴权与计费
- 让 Claude Code、Codex 等工具经网关调用第三方模型
- 无 Redis 环境下以内存模式部署网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: TokenLive is a high-performance and extensible LLM API gateway implemented in Go, drawing inspiration from the Gin 
> L25: TokenLive is tailored for large-scale language model ecosystems and high-concurrency production environments, offer
> L28:  - **Full OpenAI Compatibility**: Exposes a unified API that is fully compatible with OpenAI standards (Chat, Embed

## 星数曲线

```mermaid
xychart-beta
    title "tokenlive/tokenlive-gateway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [15, 14, 14]
```

2026-10-18 15 → 2026-10-31 14（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9a62e6a3f172` · [字段定义](../../DATASET.md)*
