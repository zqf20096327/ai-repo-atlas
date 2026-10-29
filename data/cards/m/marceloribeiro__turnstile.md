# marceloribeiro/turnstile

⭐ 18 · Go · MIT · 推送 2026-10-13 · [GitHub](https://github.com/marceloribeiro/turnstile) · [官网](https://turnstileguard.com) · 个人维护

**LLM 会话层熔断代理：实时计量并掐断失控会话**

透明流式代理，部署在应用与 LLM 提供商之间：将应用 base URL 指向它即可，无需 SDK 或改代码。实时计量每个会话的 token 与成本，在转发前执行预算上限、循环检测与手动终止，只掐断单个失控会话而不影响全局 API key。支持 OpenAI、Anthropic、Gemini 直连适配，经 OpenRouter 接任意 OpenAI 兼容端点。架构为 Go 数据平面 + FastAPI 控制平面（PostgreSQL/Redis）+ Next.js 仪表盘的三服务 monorepo，API key 与原始 prompt 不持久化，仅上传加盐哈希与数值聚合。本地完整启动需按 API→web→铸造 key→Go 数据平面顺序操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- base URL 替换即接入，无需 SDK 与代码改动
- 预执行强制门：预算上限、循环检测、手动终止单会话
- 原始 prompt 与 API key 不持久化，仅上传哈希聚合
- 三服务 monorepo：Go 数据平面 / FastAPI 控制平面 / Next.js 仪表盘

## 适用场景

- 生产环境 agent 成本失控时只掐断单个会话而非整个应用
- 按模型/组织实时观测 LLM 支出与拦截金额
- 对多租户 LLM 流量做治理与合规观测

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L14: Turnstile is a transparent proxy that sits between your application and your
> L17: every AI session in real time and trips a circuit breaker the instant *one*
> L92: 1. Your app's LLM calls hit the **Go data plane** instead of the provider directly (base-URL swap).

## 星数曲线

```mermaid
xychart-beta
    title "marceloribeiro/turnstile 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `07430582a15f` · [字段定义](../../DATASET.md)*
