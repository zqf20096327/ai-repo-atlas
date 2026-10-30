# izzoa/polyrouter

⭐ 24 · TypeScript · AGPL-3.0 · 推送 2026-10-09 · [GitHub](https://github.com/izzoa/polyrouter) · [官网](https://polyrouter.app) · 个人维护

**可自托管的 LLM 路由/网关：统一端点、多供应商路由与预算控制**

自托管 LLM 网关，位于 AI agent 与各 LLM 供应商之间：agent 用单一端点与单一密钥接入，polyrouter 按 explicit-first 优先级（显式模型、tier 头、header 规则、auto 智能分层、default 兜底）路由请求到 BYOK 密钥、自定义 OpenAI/Anthropic 兼容端点或本地模型，供应商失败时沿回退链重试，流式开始后不换模型。提供日/周/月预算的原子 Redis 计数阻断、请求时价格快照的成本记录（默认仅存元数据不存正文）、OpenAI 与 Anthropic 协议互译、SolidJS 仪表盘（KPI、请求日志、决策检查器）与告警通知。单容器部署，依赖 PostgreSQL 16 与 Redis，需 Node 24.x 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Anthropic 兼容端点，跨协议请求经专门翻译核心处理
- explicit-first 路由：显式模型优先，auto 分层不可用时静默降级到默认 tier
- 预算强制阻断（Redis 原子计数，跨实例正确）与不可变成本快照记录
- 默认仅存元数据、凭证静态加密、SSRF 防护与租户隔离

## 适用场景

- 多个 AI agent 共用一个端点和密钥接入多家 LLM 供应商
- 为团队或按 agent 设置支出预算并在超限时阻断
- 供应商故障时自动沿回退链切换且流式响应中途不换模型
- 通过仪表盘审查每个请求的路由决策、成本与延迟

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L24: polyrouter sits between your AI agents and your LLM providers. Agents talk to **one**
> L25: endpoint with **one** key; polyrouter routes each request to the right model across your
> L26: providers (BYOK API keys, custom OpenAI/Anthropic-compatible endpoints, local models),

## 星数曲线

```mermaid
xychart-beta
    title "izzoa/polyrouter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ce8cc5f879bc` · [字段定义](../../DATASET.md)*
