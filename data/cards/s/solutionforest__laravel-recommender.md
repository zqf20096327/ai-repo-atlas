# solutionforest/laravel-recommender

⭐ 3 · PHP · MIT · 推送 2026-11-19 · [GitHub](https://github.com/solutionforest/laravel-recommender) · 组织维护

**Laravel 应用的自托管推荐引擎：从已有互动数据生成 for-you 流**

面向 Laravel 开发者的推荐引擎包：读取应用已有的浏览、点赞、购买等互动表，用协同过滤找共同互动的物品（neighbours），结合趋势分与自定义规则生成个性化 Feed，结果缓存后以 JSON 分页或 Blade 卡片输出。评分由调度任务更新，数据存于四个 rec_* 表；提供 bootstrap 一键迁移建流、/recommender 健康仪表盘与 doctor/explain 等 artisan 命令。要求 PHP 8.3+ 与 Laravel 10–13，冷启动或数据稀疏时输出趋势项或空 Feed。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协同过滤（共同互动 neighbours）+ 趋势分 + 自定义规则的混合排序
- recommender:bootstrap 一键迁移、写 Feed、建分并自检表/列/索引
- /recommender 仪表盘与 doctor 命令监控 Feed 健康与慢代码段
- explain 命令按来源拆分每个物品的得分来源

## 适用场景

- 给博客或社区应用加个性化文章 Feed
- 电商应用基于浏览与购买记录推荐商品
- 新物品通过 match 属性匹配进入相关推荐

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L12: Your users view, like, or purchase things. This package reads those events from **your tables**, finds items people
> L30: 1. **Learn from activity:** scheduled commands update trending scores and find items that users interacted with tog

## 星数曲线

```mermaid
xychart-beta
    title "solutionforest/laravel-recommender 星数(近 2 点)"
    x-axis ["2026-11-12", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-12 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a16d7356bec5` · [字段定义](../../DATASET.md)*
