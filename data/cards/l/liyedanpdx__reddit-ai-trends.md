# liyedanpdx/reddit-ai-trends

⭐ 878 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/liyedanpdx/reddit-ai-trends) · 个人维护 · 中文 README

**自动扫描 Reddit 社区并生成 AI 趋势日报的工具**

通过 Reddit 官方 API 抓取 AI 相关子版块的中英文帖子，调用 LLM（经 Groq 或 OpenRouter）分析帖子、总结关键讨论、对比周/月趋势，按年/月/日目录生成每日趋势报告。支持图像分析（视觉模型）、YouTube 字幕提取、网页抓取总结（Firecrawl）、评论整合与机器人过滤；所有增强数据入库缓存以降低 API 调用，MongoDB 持久化历史数据。需自备 Reddit API 凭据与 LLM API key，Docker Compose 部署或手动运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中英双语报告，覆盖多个 AI 子版块数据采集
- 多种内容增强：视觉模型图像分析、YouTube 字幕、Firecrawl 网页总结
- Groq 与 OpenRouter 双 LLM 通道，模型可经 .env 配置
- 数据库缓存与 MongoDB 持久化，支持定时生成（--interval）

## 适用场景

- 每天自动追踪 AI 社区的新兴话题与热点排名
- 对比当前讨论与历史数据以发现趋势演变
- 监控小众 AI 社区中可能被忽略的深度讨论

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: Automatically generate trend reports from AI-related Reddit communities, supporting both English and Chinese languag
> L14: - **Real-time AI Trend Monitoring**: Track emerging AI technologies, discussions, and breakthroughs as they happen
> L23: - **Multiple LLM Providers**: Supports both Groq and OpenRouter APIs

## 星数曲线

```mermaid
xychart-beta
    title "liyedanpdx/reddit-ai-trends 星数(近 9 点)"
    x-axis ["2026-10-26", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-26", "2026-11-28"]
    y-axis "stars" 870 --> 879
    line [871, 872, 871, 873, 874, 875, 876, 878, 878]
```

2026-10-26 871 → 2026-11-28 878（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f2ca6430e01c` · [字段定义](../../DATASET.md)*
