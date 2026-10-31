# EPFLiGHT/LiGHT-Conferences-Calendar

⭐ 17 · JavaScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/EPFLiGHT/LiGHT-Conferences-Calendar) · [官网](https://conferences.light-laboratory.org/) · 组织维护

**全球健康领域学术会议截止日期追踪日历与 Slack 提醒机器人**

面向全球健康与人道响应研究的会议日历网站：以 YAML 静态文件存储会议数据（无数据库），提供时区感知的截止日期倒计时、搜索过滤、ICS 导出至 Google/Apple/Outlook 日历、演讲者页面，以及带每日摘要和 DM 提醒（截止前 30/7/3 天）的 Slack 机器人。数据保鲜由两个每月 GitHub Actions 完成：从 OpenReview API 同步，以及抓取会议官网页面并用 OpenAI 模型抽取截止日期（要求附带原文引句并校验）；另有 Action 自动发现瑞士境内新会议。技术栈为 Next.js 16 静态导出，Slack 路由部署于 Vercel，状态存 Upstash Redis。由 EPFL LiGHT Lab 成员构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无数据库架构：会议数据以 YAML 静态文件发布，浏览器端解析
- Slack 机器人提供斜杠命令、每日摘要与截止前 30/7/3 天 DM 提醒
- OpenReview API 月度同步与 LLM 抽取官网截止日期（引句核验后开 PR）
- ICS 导出单个会议或整份日历

## 适用场景

- 追踪相关学术会议的投稿截止日期与时间
- 把会议日历导入我自己的日历应用
- 在 Slack 频道接收截止日期每日摘要和提醒

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **Discover conferences and events relevant to global health and humanitarian response. Track opportunities, key date
> L21: - **Deadline index.** Every tracked venue with a live countdown, in your own timezone. Search by name or keyword, f

## 星数曲线

```mermaid
xychart-beta
    title "EPFLiGHT/LiGHT-Conferences-Calendar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e4eff70ff3c5` · [字段定义](../../DATASET.md)*
