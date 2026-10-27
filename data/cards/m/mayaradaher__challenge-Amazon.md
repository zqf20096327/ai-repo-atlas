# mayaradaher/challenge-Amazon

⭐ 30 · Jupyter Notebook · MIT · 推送 2026-01-24 · [GitHub](https://github.com/mayaradaher/challenge-Amazon) · [官网](https://amazonchallenge-122629525979.southamerica-east1.run.app) · 个人维护

**分析亚马逊购物数据并用 Gemini 生成个性化图书推荐的应用**

基于 Plotly Dash 的亚马逊购物分析应用，处理超过 300 MB 的购买数据库，经数据清洗后转为 Parquet 格式以提升加载效率。应用分三个页面：2018-2022 年购买总览（含年度交互筛选）、用户人口统计分析（性别、年龄、教育、家庭收入、州分布）、以及 AI 图书推荐页——由 Gemini 语言模型分析用户画像与图书购买历史生成个性化推荐。使用 Python、Plotly Dash、CSS 与 Google Cloud Platform 构建，曾获 Plotly App Challenge 2024 奖项。README 未给出本地安装或运行说明，仅提供在线访问入口。

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

- Gemini 语言模型基于用户画像与购买历史生成图书推荐
- 300 MB+ 购买数据库转为 Parquet 格式以优化加载
- 三页面结构：购买总览、用户人口统计、AI 图书推荐

## 适用场景

- 浏览并按年度筛选亚马逊购买趋势
- 查看购买用户的人口统计分布
- 获取基于个人购买历史的个性化图书推荐

## 场景标签

`推荐系统` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6:  The app, designed to analyze Amazon purchases, handles a database exceeding 300 MB. To optimize performance, extens
> L28: - **AI Book Recommendation**: Recognizing the importance of books as the primary product sold, a dedicated page for

## 星数曲线

```mermaid
xychart-beta
    title "mayaradaher/challenge-Amazon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8f0f9872bb81` · [字段定义](../../DATASET.md)*
