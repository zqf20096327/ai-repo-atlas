# MerlinStacks/socaliseit

⭐ 31 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/MerlinStacks/socaliseit) · 组织维护

**面向品牌与代理商的自托管社媒运营平台，带 AI 内容生成**

Overseek Socials 是基于 Next.js/React/Prisma/PostgreSQL 的社交媒体运营平台：一次编辑即可发布到 Instagram、TikTok、YouTube 等 7 个平台，提供拖拽式内容日历、跨渠道数据分析与 ROI 追踪（Shopify/WooCommerce 收入归因）、评论/提及/DM 统一互动管理与情感审阅、基于角色的团队协作。AI 部分通过 OpenRouter API 生成文案、改写、alt 文本与标签建议。以 Docker Compose 自托管部署，webapp 与 worker 从源码本地构建，包含 PostgreSQL/Redis/MinIO 服务。

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

- 一次编辑多平台发布（Instagram/TikTok/YouTube/Facebook/Pinterest/Bluesky/Google Business Profile）
- AI 内容引擎：生成文案、改写、alt 文本、标签建议（OpenRouter API）
- Shopify/WooCommerce 电商同步与收入归因分析
- 统一互动收件箱（评论/提及/DM/审阅）与协作者实时 presence

## 适用场景

- 团队在一个工作区统一排期、发布与分析多个社媒账号
- 代理商多品牌工作区隔离管理与协作
- 将社媒发帖与电商收入数据关联追踪 ROI

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L29: - **AI content engine**: Generate captions, rewrite copy, create alt text, suggest tags, and keep output aligned wi
> L85: Update `stack.env` with database values, OAuth provider credentials, and your `OPENROUTER_API_KEY`.

## 星数曲线

```mermaid
xychart-beta
    title "MerlinStacks/socaliseit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fffc10c42b62` · [字段定义](../../DATASET.md)*
