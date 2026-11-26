# Lightningsobad/hackernews-daily-bot

⭐ 3 · Python · 推送 2026-11-02 · [GitHub](https://github.com/Lightningsobad/hackernews-daily-bot) · [官网](https://news.ycombinator.com/) · 个人维护

**Telegram 机器人：每日推送 Hacker News AI 与编程要闻摘要**

运行在 GitHub Actions 上的自动化摘要机器人（声明 $0 服务器成本）：定时抓取 Hacker News 过去 24 小时内 AI 与编程领域的热门故事，提取全文后调用 Google Gemini 生成每篇 2-3 条要点的摘要，于每日 00:17 UTC 组装成结构化 digest 发送到用户的 Telegram 频道、群组或私信。用户通过 /start 订阅、/stop 退订，订阅者可由 Cloudflare Worker + D1 可选存储。内置模型级联容错（配置模型失效时切换备用模型）与无 AI 时的降级推送（仅标题与链接）。支持 dry-run 本地测试与 pytest 测试套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每日定时抓取 Hacker News AI 与编程热门故事并广播 digest
- Google Gemini 生成每篇 2-3 条要点摘要，模型可通过 GEMINI_MODEL 变量切换
- 模型级联容错：模型 404 时自动切换备用模型，网络故障时降级为纯标题推送
- GitHub Actions cron 触发运行，无需自建服务器，亦支持本地 dry-run 测试

## 适用场景

- 为团队 Telegram 频道自动推送每日 AI 与编程资讯
- 个人订阅 Hacker News 热门内容的中文以外轻量渠道
- 在无服务器预算的情况下用 GitHub Actions 定时任务跑信息聚合

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10: A lightweight, automated daily digest bot running 100% free on **GitHub Actions** ($0 server cost):
> L12: 2. Extracts full article content and leverages **Google Gemini AI** to produce concise 2–3 bullet point summaries.

## 星数曲线

```mermaid
xychart-beta
    title "Lightningsobad/hackernews-daily-bot 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ba6c1f186808` · [字段定义](../../DATASET.md)*
