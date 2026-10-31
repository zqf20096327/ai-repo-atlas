# pltnk/habr-observer

⭐ 31 · Go · MIT · 推送 2026-07-13 · [GitHub](https://github.com/pltnk/habr-observer) · [官网](https://habr.observer) · 个人维护

**自动更新的 Habr 优质文章 AI 摘要聚合站**

面向读者用户的网站应用：抓取 habr.com 的文章内容，通过 YandexGPT 服务（300.ya.ru）生成文章简短摘要，形成自动更新的文章流，线上部署于 habr.observer。仓库提供 Docker Compose 部署方式：克隆仓库、配置 .env（MongoDB 用户密码、300.ya.ru API token）后 docker compose up -d 启动；初次抓取受 API 速率限制可能耗时数分钟。项目采用 MIT 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动抓取 Habr 文章并生成 YandexGPT 摘要流
- 提供线上站点 habr.observer
- 支持 Docker Compose 一键部署，依赖 MongoDB 存储

## 适用场景

- 快速浏览 Habr 优质文章的 AI 摘要
- 自部署一个 Habr 文章摘要聚合服务

## 场景标签

 · 领域:内容聚合/NLP 应用

## 证据(README 行号)

> L2: ### Лента кратких пересказов лучших статей с Хабра от нейросети YandexGPT
> L5: В приложении используются материалы сайта habr.com, краткие пересказы которых получены с помощью сервиса 300.ya.ru.

## 星数曲线

```mermaid
xychart-beta
    title "pltnk/habr-observer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a5a9149dd73a` · [字段定义](../../DATASET.md)*
