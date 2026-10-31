# philippe2803/contentmap

⭐ 49 · Python · 推送 2026-10-16 · [GitHub](https://github.com/philippe2803/contentmap) · [官网](https://philippeoger.com/pages/can-we-rag-the-whole-web) · 个人维护

**用网站 XML sitemap 生成 SQLite 内容数据集（RAG 用）的 Python 库**

Python 库 contentmap：以网站 XML sitemap 为起点抓取页面内容，生成 SQLite 数据库形式的内容数据集，作为 RSS 的替代分发方式；可选集成 sqlite-vss 向量搜索能力（借助 LangChain 集成），几行代码即可产出带向量检索的 contentmap.db，可直接用于 RAG 数据准备。面向需要为自有域名构建内容数据集的开发者，通过 pip 安装。README 未说明支持的页面解析细节与规模限制。

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

- 从 XML sitemap 自动生成 SQLite 内容数据集
- 可选向量搜索能力（sqlite-vss，经 LangChain 集成）
- pip 安装，数行代码完成构建

## 适用场景

- 为自己的网站快速构建 RAG 检索数据集
- 以 SQLite 数据库替代 RSS 分享站点内容
- 为域名内容建立带向量相似度检索的数据库

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L4: RSS feeds. The purpose of this library is to simply create a dataset for all the
> L32: This will automatically create the SQLite database file, with vector search

## 星数曲线

```mermaid
xychart-beta
    title "philippe2803/contentmap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-31 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `18652ba49269` · [字段定义](../../DATASET.md)*
