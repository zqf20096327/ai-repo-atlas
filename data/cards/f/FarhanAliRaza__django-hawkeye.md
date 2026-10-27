# FarhanAliRaza/django-hawkeye

⭐ 79 · Python · 推送 2026-01-07 · [GitHub](https://github.com/FarhanAliRaza/django-hawkeye) · 个人维护

**Django BM25 全文检索库：基于 PostgreSQL，可作 RAG 检索层**

Django 库，通过 BM25Searchable Mixin 和 BM25Index 为模型提供 .search() 方法，利用 PostgreSQL 17+ 的 pg_textsearch 扩展实现 BM25 相关性排序，不依赖外部检索服务。定位为 Elasticsearch 的轻量替代，README 以功能对比表列出基础设施、索引同步与配置差异。支持直接使用 BM25Score 表达式手动控制，README 标注 pg_textsearch 返回负分、分值越低匹配越好，可作 RAG 的检索层。限制：需在服务器上安装 pg_textsearch 扩展，要求 PostgreSQL 17+、Django 4.2+、Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BM25Searchable Mixin 提供 .search() 方法，单行即可检索
- 基于 PostgreSQL 17+ pg_textsearch，无外部服务依赖
- 提供 BM25Score 直接表达式 API 支持手动控制
- 声明可用作 RAG 的检索层

## 适用场景

- 在 Django 项目中为模型添加 BM25 全文搜索
- 为 RAG 应用提供检索层而无需部署 Elasticsearch 集群
- 已有 PostgreSQL 的项目内实现带相关性排序的搜索

## 场景标签

`语义搜索` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: - **RAG-ready** - Use as the retrieval layer for Retrieval Augmented Generation
> L3: Django BM25 full-text search using PostgreSQL pg_textsearch - a lightweight Elasticsearch alternative.

## 星数曲线

```mermaid
xychart-beta
    title "FarhanAliRaza/django-hawkeye 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-27 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `20c536e6616b` · [字段定义](../../DATASET.md)*
