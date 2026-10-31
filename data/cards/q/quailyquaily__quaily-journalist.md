# quailyquaily/quaily-journalist

⭐ 13 · Go · AGPL-3.0 · 推送 2026-01-29 · [GitHub](https://github.com/quailyquaily/quaily-journalist) · [官网](https://quaily.com/opensource) · 组织维护 · 中文 README

**从 V2EX/HN 抓取排名并生成 Markdown 日报的 CLI 工具**

Go 编写的 CLI 工具与服务：定时轮询 V2EX 节点与 Hacker News 列表，用类 HN 的时间衰减公式对帖子评分，存入 Redis，按模板渲染频道专属的日/周 Markdown 日报，并可自动发布到 Quaily 平台。支持 OpenAI 生成条目摘要与帖子总结，可选通过 Cloudflare Browser Rendering 从 URL 清单抓取。面向需要自动化运营中文技术日报频道的运营者/开发者，需自备 Go 1.21+ 与 Redis。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- V2EX 节点与 Hacker News 列表采集，类 HN 时间衰减评分
- Redis 存储与日/周周期 ZSET，按模板渲染 Markdown
- OpenAI 生成条目摘要与帖子总结
- serve/generate/publish/send 等 CLI，支持自动发布到 Quaily 与 systemd 部署

## 适用场景

- 自动生成并发布 V2EX / Hacker News 日报频道
- 从 URL 清单批量抓取并渲染成 Markdown 合集
- 通过 Telegram 等渠道分发每日/每周技术摘要

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L5: Collect, score, and publish Markdown newsletters from V2EX and Hacker News. Quaily Journalist runs small workers tha
> L27: - AI-powered summaries (OpenAI) for item descriptions and a post summary

## 星数曲线

```mermaid
xychart-beta
    title "quailyquaily/quaily-journalist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `88a73ea8462e` · [字段定义](../../DATASET.md)*
