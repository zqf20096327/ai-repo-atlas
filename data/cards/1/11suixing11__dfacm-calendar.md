# 11suixing11/dfacm-calendar

⭐ 4 · JavaScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/11suixing11/dfacm-calendar) · [官网](https://dfacm.website/calendar) · 个人维护 · 中文 README

**面向 HydroOJ 站点与参赛者的统一赛事日历**

以 HydroOJ 插件形式提供的赛事聚合日历，将 ICPC、CCPC、Codeforces、AtCoder、AI 竞赛与黑客松收录到同一清单，支持按方向、类型、标签、平台、状态与关键词组合筛选，并提供与筛选条件联动的 ICS/RSS 订阅和公开 JSON 接口。数据来自手工维护的 calendar.json、直接抓取、可选的 CLIST API 以及配套的 FastAPI AI 采集后台；多源结果去重合并，单源失败时保留缓存。需 Node.js 22，生产部署在 Hydro 环境中，AI 采集组件仅作可选后台服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一收录算法赛、AI 竞赛与黑客松，多条件组合筛选
- ICS / RSS 订阅与页面共用同一套筛选条件
- 多源数据自动采集与去重合并，单源失败保留缓存
- 公开 /calendar/data JSON 接口供外部程序读取

## 适用场景

- 给 OJ 站点挂载一份算法与 AI 赛事日历
- 用日历客户端订阅自己筛选出的赛程和报名截止提醒
- 让自己的机器人低频读取公开赛事 JSON 数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: 把算法赛、AI 竞赛和黑客松放进同一份日历。为 HydroOJ 提供公开赛事清单、组合筛选，以及跟随筛选条件的 ICS / RSS 订阅。
> L44: |AI 采集后台|DataFountain、天池、讯飞、Kaggle、DrivenData、Devpost、lablab.ai|可选，Kaggle 需要自己的 token|
> L35: AI 采集组件只需作为后台服务启动。网站的导航、清单和订阅由一个 Hydro 日历插件提供。

## 星数曲线

```mermaid
xychart-beta
    title "11suixing11/dfacm-calendar 星数(近 3 点)"
    x-axis ["2026-11-22", "2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-22 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `7600be8fdb4d` · [字段定义](../../DATASET.md)*
