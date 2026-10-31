# guo-yichen/news-summary

⭐ 14 · Python · 推送 2026-10-30 · [GitHub](https://github.com/guo-yichen/news-summary) · 个人维护 · 中文 README

**用 Claude 聚合个人信息源生成每日 AI 简报并投递到 Notion 与邮箱**

运行在 GitHub Actions 上的自动化流水线：抓取 RSS、Substack、博客、播客、YouTube 字幕、Twitter/X 时间线、邮件 Newsletter 等 30 余种信息源，调用 Claude API 生成结构化摘要，输出中/英/双语简报，写入 Notion 数据库、发送 HTML 邮件或保存为 Markdown，并可推送 Telegram。支持跨日去重与 30 天时效过滤。面向希望每天自动收到个人定制信息简报的用户，Fork 后配置 Secrets 即可免费定时运行，无需服务器。Telegram 推送功能标注为未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ 种信息源类型（RSS/YouTube 字幕/Twitter 时间线/IMAP 邮件等）
- Claude AI 生成结构化摘要，支持 zh/en/bilingual 输出
- 每日北京时间 9:00 在 GitHub Actions 自动运行，无需服务器
- 投递到 Notion、HTML 邮件、Markdown 文件，Telegram 通知为未测试功能

## 适用场景

- 每天自动收到我关注的博客、播客与推文的 AI 摘要
- 把多来源信息整理成 Notion 页面作为个人日报归档
- 用双语摘要同时跟踪中英文 AI 资讯

## 场景标签

`网页抓取` `AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: An automated pipeline that aggregates your personal information sources every day, uses Claude AI to generate a stru
> L16: |**Claude AI summaries**|Structured digest with highlights, bullet points, and source-by-source breakdown|✅|

## 星数曲线

```mermaid
xychart-beta
    title "guo-yichen/news-summary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a57a47198bf3` · [字段定义](../../DATASET.md)*
