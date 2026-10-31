# bagusardin25/DevRadar

⭐ 15 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/bagusardin25/DevRadar) · [官网](https://dev-radar-rho.vercel.app) · 个人维护

**开源黑客松与 AI 免费额度聚合目录，带多级核验**

聚合 Devpost/Devfolio/MLH/lablab.ai 等公开渠道的黑客松活动与 AI 免费额度/优惠信息，尽可能对照官方页面核验并标注状态（verified_active 等）。架构为 React/Vite 前端 + FastAPI + PostgreSQL，Celery worker 执行定时采集与提交初审，人工审核队列控制发布。AI 用于从官方页提取结构化字段与提交初审，可在无 LLM key 的 seed demo 模式下运行。面向开发者与自托管运营者，MIT 许可。

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

- 多来源定时采集（Devpost/Devfolio/MLH/lablab.ai）进人工审核队列
- 分级核验状态与来源层级标注，无需终端用户登录或 API key
- 无 key 的 seed demo 模式可本地完整运行
- Docker Compose 部署基础设施，API 另提供容器镜像构建

## 适用场景

- 查找线上黑客松与 AI 免费额度/优惠
- 自托管一套带审核队列的机会聚合目录
- 作为贡献者参与数据源与管线开发

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L10: DevRadar aggregates **hackathons / challenges** and **AI free tiers / credits / promos**, then tries to **verify** 
> L164: |**Seed demo**|None (Docker + generated secrets only)|Local try-out, OSS contributors, demos|
> L165: |**Ingestion + LLM**|`LLM_API_KEY` (OpenAI-compatible)|Extract structured fields from official pages|

## 星数曲线

```mermaid
xychart-beta
    title "bagusardin25/DevRadar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `339362682017` · [字段定义](../../DATASET.md)*
