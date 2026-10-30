# m0wer/rssfilter

⭐ 46 · Python · MIT · 推送 2026-02-03 · [GitHub](https://github.com/m0wer/rssfilter) · [官网](https://rssfilter.sgn.space/) · 个人维护

**基于阅读历史的 AI RSS 过滤与文章推荐自托管服务**

用户将 RSS 阅读器中的订阅源 URL 替换为本服务后端地址，由后端抓取并过滤订阅条目、记录已读文章；对已读文章计算 LLM embeddings 并聚类，据此推荐相似文章，同时保留随机条目用于新话题发现；默认读过约 10 篇文章后开始推荐。自托管通过 docker-compose 部署，架构含 FastAPI 后端、静态前端、Redis 队列、CPU/GPU worker、调度器与 Traefik 反代，内置 SSRF 防护与可选代理隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 追踪已读文章并计算 LLM embeddings 聚类，推荐相似条目
- 保留随机条目以支持新话题发现
- docker-compose 一键自托管，含 SSRF 防护与可选代理隔离
- 内置调度器承担抓取、维护、重试等周期任务，无需外部 cron

## 适用场景

- 在我的 RSS 阅读器中过滤不感兴趣的条目
- 根据我读过的文章获得相似内容推荐
- 自托管一个可控的个性化 RSS 过滤后端

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L8: RSS feeds recommendation system based on user read articles. Replaces the feed
> L10: and track user read articles. Uses LLM embeddings and machine learning to
> L16: It works by tracking the users read articles, computing their embeddings,

## 星数曲线

```mermaid
xychart-beta
    title "m0wer/rssfilter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-30 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1d0c7342cb5d` · [字段定义](../../DATASET.md)*
