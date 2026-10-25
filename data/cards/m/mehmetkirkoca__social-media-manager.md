# mehmetkirkoca/social-media-manager

⭐ 101 · JavaScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/mehmetkirkoca/social-media-manager) · 个人维护

**自托管多平台社媒管理面板：聚合信息流、跨平台发帖与定时**

本地优先的自托管社媒管理平台：将 Twitter/X、Mastodon、Bluesky、LinkedIn、Instagram、Reddit、YouTube 的信息流聚合到统一面板，支持跨平台同时发布、按平台/标签过滤、BullMQ 定时发帖。架构上以微服务组织，每个平台一个独立服务，经 RabbitMQ 通信，Node.js/Fastify 做 API 网关，MongoDB/Redis 存储，Docker Compose 一键启动。AI 为其中功能：本地运行的 T5 模型做语法纠正与平台化内容改写。需自行配置各平台 API 凭据。

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

- 聚合 7 个平台信息流到统一面板
- 一次编写、多平台同时发布
- BullMQ 定时发帖队列
- T5 模型本地运行，提供语法纠正与平台化内容改写

## 适用场景

- 在一个面板里查看我所有社媒账号的信息流
- 一次写作同时发布到多个平台
- 提前排期定时发布社媒内容

## 场景标签

`AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A self-hosted, local-first social media management platform. Aggregate feeds from all your platforms, compose and cr
> L11: - **AI Assistance** — Grammar correction and platform-specific content adaptation (T5 model, runs locally)

## 星数曲线

```mermaid
xychart-beta
    title "mehmetkirkoca/social-media-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-25 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `208fc5621f54` · [字段定义](../../DATASET.md)*
