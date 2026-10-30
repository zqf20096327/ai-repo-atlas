# MerlinStacks/overseek

⭐ 29 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/MerlinStacks/overseek) · 组织维护

**WooCommerce 自托管运营仪表盘：订单、库存、分析与客服一体**

面向 WooCommerce 商店团队的自托管运营平台：通过 WordPress 插件将店铺数据同步到自有的 PostgreSQL 后端，在统一界面管理订单、库存与供应链、发货、客服收件箱、邮件营销、分析与增长等模块。技术栈为 React 19 + Fastify 5 + Prisma，含 Socket.IO 实时更新与移动 PWA。AI 为局部功能：收件箱 AI 草稿协助与可选 AI manager（经 OpenRouter 接入）；部分模块（邮件、发货、批发目录等）为账户功能门控。以 Docker Compose 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WooCommerce 订单、放弃购物车、库存与供应链统一同步管理
- 客服收件箱含 AI 草稿协助与实时聊天
- 邮件营销流程、分群与投放日志
- Docker Compose 部署，首个注册用户成为超级管理员

## 适用场景

- 把 WooCommerce 店铺的订单、库存、客服集中到一个私有仪表盘
- 摆脱分散的 SaaS 面板，自托管掌控商业数据
- 在收件箱中用 AI 起草客服回复并做邮件营销自动化

## 场景标签

 · 领域:电商运营/商业智能

## 证据(README 行号)

> L24: OverSeek is a self-hosted operations hub for WooCommerce stores. It syncs store data into your own PostgreSQL-backe
> L34: - **Inbox:** customer conversations, live chat, email-style replies, canned responses, AI draft assistance, unread 
> L37: - **Growth:** paid ads, reviews, SEO keywords, SEO content tools, product feeds, and optional AI manager features.

## 星数曲线

```mermaid
xychart-beta
    title "MerlinStacks/overseek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `52a79141e000` · [字段定义](../../DATASET.md)*
