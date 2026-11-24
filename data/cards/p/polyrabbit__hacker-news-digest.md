# polyrabbit/hacker-news-digest

⭐ 754 · Python · LGPL-3.0 · 推送 2026-11-22 · [GitHub](https://github.com/polyrabbit/hacker-news-digest) · [官网](http://hackernews.betacat.io/) · 个人维护 · 中文 README

**用 LLM 为 Hacker News 首页新闻生成摘要与配图的阅读站**

一个部署在 GitHub Pages 上的静态站点，周期性抓取 Hacker News 首页文章，用评分算法抽取正文，为每篇文章生成 AI 摘要并配图，支持按积分/评论数/时间排序、筛选 Top N、每日存档、RSS 订阅与中文翻译（翻译同样由 LLM 完成）。摘要默认调用 OpenAI API，API 不可用时回退到本地模型。使用者直接消费生成的摘要页面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 远程 LLM 生成摘要，本地 Qwen 作为 API 不可用时的回退
- 中文翻译由 LLM 完成
- 每日存档与 RSS 订阅
- 按积分/评论数/提交时间排序并筛选 Top N

## 适用场景

- 快速浏览 Hacker News 首页哪些文章值得细读
- 通过 RSS 订阅每日 AI 摘要
- 阅读 Hacker News 新闻的中文译版

## 场景标签

 · 领域:内容聚合/新闻阅读

## 证据(README 行号)

> L10: Hacker News Summary adds short AI summaries and images to stories
> L46: 4. Generating summaries of the article's content using OpenAI API or invoking a local model as a

## 星数曲线

```mermaid
xychart-beta
    title "polyrabbit/hacker-news-digest 星数(近 6 点)"
    x-axis ["2026-10-22", "2026-11-08", "2026-11-10", "2026-11-18", "2026-11-20", "2026-11-24"]
    y-axis "stars" 752 --> 756
    line [754, 753, 754, 755, 754, 754]
```

2026-10-22 754 → 2026-11-24 754（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `fcaad335b117` · [字段定义](../../DATASET.md)*
