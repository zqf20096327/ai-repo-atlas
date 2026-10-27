# AlameerAshraf/tokentoll

⭐ 78 · Python · 推送 2026-03-09 · [GitHub](https://github.com/AlameerAshraf/tokentoll) · [官网](https://github.com/AlameerAshraf/tokentoll) · 个人维护

**面向 LLM SaaS 的自托管计量计费与开票引擎**

为基于 LLM 的 SaaS 提供计费基础设施：通过 REST 或 SDK 摄入用量事件，以 YAML 定义计价方案（按量/阶梯/批量/固定/预付/免费额度），计算成本、执行配额与预算上限、自动生成月度发票并可同步 Stripe，或完全自托管运行。内置 12 家提供商、100+ 模型的费率表，传入 provider/model 即自动计价，费率 YAML 支持热重载。架构含 FastAPI API、三类 worker、MongoDB 与 Redis，Docker Compose 一键启动，附 React 仪表盘。SDK 未发布到包仓库，需本地构建安装；无 Stripe 时以手动开票模式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件摄入幂等去重，支持批量与多计量（tokens/调用次数/计算时长）
- YAML 定价方案热重载，覆盖按量/阶梯/批量/固定/预付/免费额度六种模型
- 预配置 12 家提供商、100+ 模型费率表，自动计算成本
- Stripe 同步或完全自托管，多租户隔离与 HMAC 签名 Webhook

## 适用场景

- 为我的 LLM SaaS 按客户追踪 token 用量并自动出账
- 执行配额、预算上限与预付额度控制
- 自托管地运行计量与开票，不依赖外部计费 SaaS

## 场景标签

 · 领域:LLM 基础设施/计费

## 证据(README 行号)

> L21: > **The problem:** You're building a SaaS on top of LLMs. You need to track usage per customer, enforce quotas, sup
> L23: > **The solution:** TokenToll gives you a single API to handle all of it. Ingest usage events, define pricing in YA

## 星数曲线

```mermaid
xychart-beta
    title "AlameerAshraf/tokentoll 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 76 --> 79
    line [77, 78, 78]
```

2026-10-18 77 → 2026-10-27 78（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ea4f8651dcba` · [字段定义](../../DATASET.md)*
