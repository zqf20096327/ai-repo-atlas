# odysseus0/feed

⭐ 16 · Go · 推送 2026-09-01 · [GitHub](https://github.com/odysseus0/feed) · 个人维护

**面向 AI agent 的无界面 RSS 阅读引擎 CLI**

用 Go 编写的无头 RSS 引擎，供 AI agent 或脚本调用：从任意网页自动发现 feed URL，10 并发抓取并预转换为 Markdown，SQLite FTS5 全文检索标题/摘要/正文，feed 过期 30 分钟自动刷新，支持批量标记已读与 table/JSON/wide 三种输出到 stdout、状态走 stderr 的 Unix 管道式设计。数据落在单一 SQLite 文件，无服务器无账号可离线。作者定位其为 RSS 与应用之间的管道层，与带 UI 的阅读器互补，附带 92 个技术博客的起始 OPML。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从任意网页自动发现 feed URL，无需手动找 XML 链接
- SQLite FTS5 全文检索标题/摘要/正文，单一文件存储
- 抓取时预转换 Markdown，feed 过期自动刷新（可跳过）
- table/JSON/wide 输出到 stdout，支持批量标记已读供 agent 分拣

## 适用场景

- 让本地 LLM agent 按我自己的优先级分拣 RSS 订阅
- 把 RSS 内容管道化接入通知、笔记库或脚本
- 直接用 SQL 查询自己积累的订阅数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: `feed` is a headless RSS engine that lets an AI agent read your feeds for you — your own algorithm.
> L49: Newsboat, miniflux, and NetNewsWire are readers. This is plumbing. They have UIs; this has clean table output for a

## 星数曲线

```mermaid
xychart-beta
    title "odysseus0/feed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `14d5b549ac8a` · [字段定义](../../DATASET.md)*
