# buildlucid/lucid-cms

⭐ 23 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/buildlucid/lucid-cms) · 组织维护

**TypeScript 优先的无头 CMS，面向需要内容建模与发布流程的团队**

面向开发与内容团队的无头 CMS：开发者通过代码定义集合、类型化 API、运行时与数据库适配器（Node.js/Cloudflare Workers，PostgreSQL/SQLite/LibSQL/D1）以及插件体系扩展；内容团队获得媒体管理、修订、工作流、定时发布、本地化与 AI 内容工具（生成图片、生成替代文本、AI 用量追踪，需订阅）。当前处于 alpha 阶段，AI 功能将随 beta 上线，API 可能有破坏性变更。默认启用匿名遥测，可通过配置关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代码定义集合、可复用砖块、自定义字段与本地化
- 双运行时适配：Node.js 与 Cloudflare Workers
- 四种数据库适配器（PostgreSQL/LibSQL/SQLite/D1）
- 20 个官方插件（S3/R2/Redis/Typesense/SEO 等）与 Astro 集成

## 适用场景

- 为 Astro 站点提供结构化内容管理与发布
- 在 Cloudflare Workers 边缘环境运行内容平台
- 团队协作的内容工作流：修订、审批、定时发布

## 场景标签

 · 领域:内容管理系统

## 证据(README 行号)

> L11: Lucid CMS is a TypeScript-first headless CMS for teams that need flexible content modeling, polished editorial work
> L23: - **Use AI where it helps:** generate and edit images, generate alt text, and track AI usage.

## 星数曲线

```mermaid
xychart-beta
    title "buildlucid/lucid-cms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `22c837a17505` · [字段定义](../../DATASET.md)*
