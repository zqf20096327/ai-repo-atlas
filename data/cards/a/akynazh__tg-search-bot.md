# akynazh/tg-search-bot

⭐ 205 · Python · GPL-3.0 · 推送 2026-08-30 · [GitHub](https://github.com/akynazh/tg-search-bot) · 个人维护 · 中文 README

**Telegram 影视磁力搜索机器人：AI 理解自然语言并自动存 PikPak**

Python 3 编写的 Telegram 机器人，用于搜索影视磁力链接：聚合 TorrentKitty、apibay 与 Jvav 视频索引 API，支持按标题、番号、剧情、演员等检索，返回封面、评分与磁力链接，并可通过 PikPak OpenAPI 自动离线下载最佳磁力。AI 部分通过任意 OpenAI 兼容 API 做意图识别（intent/target/source），自动选择爬虫或数据源；未配置 AI 时回退到番号检测与 BT 关键词搜索流程。提供 Docker 与源码两种运行方式，配置文件位于 ~/.tg_search_bot/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意 OpenAI 兼容 API 做意图识别与自动路由，无 AI 配置时可回退
- PikPak OpenAPI 自动保存最佳磁力并支持离线下载
- 多数据源聚合搜索（TorrentKitty/apibay/Jvav），支持多轮翻页与收藏导出
- 提供 docker-compose 一键部署

## 适用场景

- 在 Telegram 里用自然语言描述想看的影视内容直接搜索
- 搜索后自动把磁力存入 PikPak 离线下载
- 翻页浏览结果并保存指定条目

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: - AI natural-language search that understands intent and selects the best source automatically
> L27: 2. The AI interprets the request and returns `intent`, `target`, `source`, and `explain`.

## 星数曲线

```mermaid
xychart-beta
    title "akynazh/tg-search-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-23 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `686d38c35282` · [字段定义](../../DATASET.md)*
