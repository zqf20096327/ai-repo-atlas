# sansan0/TrendRadar

⭐ 62,998 · Python · GPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/sansan0/TrendRadar) · [官网](https://trendradar.sandev.cc) · 个人维护 · 中文 README

**面向个人用户的多平台热点聚合监控与 AI 舆情筛选推送工具**

聚合多平台热榜与 RSS 订阅，按关键词或自然语言兴趣描述筛选新闻，通过微信、飞书、钉钉、Telegram、邮件、ntfy、bark、slack 等渠道推送。AI 功能包括智能筛选（自动提取标签并对新闻打分，失败时回退关键词匹配）、标题翻译、分析简报（趋势概述、情感倾向等），底层经 LiteLLM 统一接入 100+ 模型提供商。支持 Docker、GitHub Actions、本地部署与 Cloudflare Pages，数据本地/云端自持；另提供 MCP Server，支持自然语言对话式查询与分析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.8 天,年发版 0,9 位贡献者
- 涨星:近 1 天 **+49**(自 20261016 起算)
- 平台:LINUX · 协议:MCP / OLLAMA

## 能力要点

- AI 智能筛选：自然语言兴趣描述自动打分，失败回退关键词匹配
- 通过 LiteLLM 接入 DeepSeek、OpenAI、Gemini、Anthropic 等 100+ 提供商
- MCP Server 提供 21 个工具与 4 个资源，支持对话式分析与文章正文读取
- 9 个推送渠道，含通用 Webhook 适配 Discord/IFTTT 等平台

## 适用场景

- 每天定时收到按我的关键词和 AI 兴趣筛选的热点推送
- 追踪某话题在不同平台热榜的排名变化趋势
- 把英文科技新闻翻译后推送到我的 IM
- 用 AI 对话方式查询和分析近期热点

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L339: - **统一 AI 接口**：使用 LiteLLM 替代手动实现，支持 100+ AI 提供商
> L269: - **AI 智能筛选系统**：不用再手动设关键词！在 `ai_interests.txt` 里用日常语言写下你关注的方向（如"我想看 AI 和新能源相关新闻"），AI 会自动提取标签并对每条新闻打分，只推送真正和你相关的内容。

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `41b6f389242c` · [字段定义](../../DATASET.md)*
