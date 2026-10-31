# geekjourneyx/trending-skills

⭐ 67 · Python · 推送 2026-01-24 · [GitHub](https://github.com/geekjourneyx/trending-skills) · [官网](https://skills.sh/) · 个人维护 · 中文 README

**每日抓取 skills.sh 排行榜并用 AI 分析的趋势邮件报告工具**

自动化技能趋势追踪系统：用 Playwright 抓取 skills.sh/trending 的 Top 100 排行榜与技能详情，调用 Claude API（默认经智谱代理接入）生成摘要与分类，计算排名变化、新晋/掉榜与暴涨检测，结果存入 SQLite，并通过 Resend 发送 HTML 邮件报告。可本地运行，也可 Fork 后用 GitHub Actions 每日 UTC 02:00 定时执行。需要自备 Claude API Key 与 Resend API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Playwright 动态渲染抓取 skills.sh Top 100 排行榜与技能详情
- Claude AI 自动总结、分类并提取技能解决的问题
- 排名变化、新晋/掉榜、暴涨检测等趋势计算
- GitHub Actions 定时任务 + Resend HTML 邮件推送

## 适用场景

- 每天通过邮件了解 skills.sh 技能排行榜变化
- 追踪新兴技能的排名与安装量趋势
- 用 AI 摘要快速判断技能的用途与适用场景

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L12: **Skills Trending Daily** 是一个自动化技能趋势追踪系统。它每天从 skills.sh/trending 获取最新的技能排行榜，使用 Claude AI 对热门技能进行智能分析和分类，计算排名变化趋势，并通
> L29: |**AI 分析**|Claude AI 自动总结、分类、提取价值|

## 星数曲线

```mermaid
xychart-beta
    title "geekjourneyx/trending-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-31 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0d399afa263d` · [字段定义](../../DATASET.md)*
