# giftedunicorn/ai-news-bot

⭐ 27 · Python · GPL-3.0 · 推送 2026-07-20 · [GitHub](https://github.com/giftedunicorn/ai-news-bot) · [官网](https://giftedunicorn.github.io/ai-news-bot/) · 个人维护 · 中文 README

**自动抓取 RSS 并用 LLM 生成每日 AI 新闻摘要邮件的机器人**

Python 编写的自动化新闻摘要生成器：从 RSS 源（含 36Kr、机器之心等中文源）抓取实时 AI 新闻，调用 Claude/DeepSeek/Gemini/Grok/OpenAI 五家 LLM 生成新闻摘要，输出 HTML 邮件并支持 Slack、Telegram、Discord、Webhook 通知。提供 GitHub Actions 定时执行（默认每日 UTC 零点）与本地 .env 运行两种部署方式，支持 13+ 种输出语言、9 种预置提示词模板与可选 DuckDuckGo 补充搜索。使用需自备 LLM API key 与通知渠道账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 家 LLM 提供商可选（Claude/DeepSeek/Gemini/Grok/OpenAI）
- RSS 实时抓取 + 可选 DuckDuckGo 网络搜索
- 13+ 语言输出与内置中文 AI 新闻源（36Kr、机器之心等）
- GitHub Actions 每日自动执行，支持邮件/Slack/Telegram/Discord/Webhook 五种通知渠道

## 适用场景

- 每天定时收到 AI 领域新闻摘要邮件
- 通过 Telegram/Slack/Discord 频道订阅 AI 资讯
- 自定义主题与提示词模板生成面向特定方向的新闻摘要

## 场景标签

`AI 写作` `网页抓取` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L27: - **Multi-Provider LLM Support**: Choose between Claude, DeepSeek, Gemini, Grok, or OpenAI for news generation
> L29: - **AI-Powered News Generation**: Generate comprehensive AI news digests using your preferred LLM provider
> L37: - **Automated Scheduling**: GitHub Actions workflow for daily automated execution

## 星数曲线

```mermaid
xychart-beta
    title "giftedunicorn/ai-news-bot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-28 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c3de229e4a7a` · [字段定义](../../DATASET.md)*
