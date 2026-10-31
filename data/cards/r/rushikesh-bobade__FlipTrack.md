# rushikesh-bobade/FlipTrack

⭐ 27 · TypeScript · MIT · 推送 2026-08-29 · [GitHub](https://github.com/rushikesh-bobade/FlipTrack) · [官网](https://fliptrack-psi.vercel.app) · 个人维护

**面向转售商的开源 SaaS：库存、市价追踪与 AI 洞察**

面向球鞋、收藏品、电子产品等实物转售商的开源 SaaS 平台（MIT）。核心功能包括库存管理（SKU/尺码/成色/实时状态）、通过 API cron 定时爬取二级平台市场价格、销售与费用记录及损益报表。AI 部分基于 Vercel AI SDK 与 Groq（Llama 3）分析库存并给出持有/出售建议。技术栈为 React Router v7 + TypeScript + Prisma + Supabase（PostgreSQL/Auth），本地开发可用 docker-compose 启动 Postgres 容器，需 Node.js v18+、Supabase 账号与 Groq API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 库存全生命周期管理（IN_STOCK/LISTED/SOLD 状态）
- API cron 后台爬取多平台市场价格更新估值
- Groq（Llama 3）生成持有/出售建议的 AI 洞察
- 销售/费用记录与即时 P&L 报表生成

## 适用场景

- 管理我的转售库存并跟踪每件商品状态
- 自动追踪二级市场行情给库存定价
- 记录销售与费用，查看利润与亏损报表
- 让 AI 基于我的库存数据给出出售时机建议

## 场景标签

`数据分析` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10:  An open-source SaaS platform designed for resellers of any physical goods (electronics, vintage clothing, collecti
> L30:  Powered by the Vercel AI SDK and Groq (Llama 3), FlipTrack analyzes your inventory and provides actionable, data-d

## 星数曲线

```mermaid
xychart-beta
    title "rushikesh-bobade/FlipTrack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c905f0fc9900` · [字段定义](../../DATASET.md)*
