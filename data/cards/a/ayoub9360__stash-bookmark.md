# ayoub9360/stash-bookmark

⭐ 13 · TypeScript · MIT · 推送 2026-02-28 · [GitHub](https://github.com/ayoub9360/stash-bookmark) · [官网](https://github.com/ayoub9360/stash-bookmark) · 个人维护

**自托管 AI 书签管理器：粘贴链接自动摘要、分类并可自然语言搜索**

单用户自托管的书签管理应用：粘贴 URL 后由 BullMQ 异步任务抓取内容、提取元数据、用 OpenAI 生成 LLM 摘要、自动分类打标签并生成向量嵌入。搜索采用 pgvector 余弦相似度与 PostgreSQL 全文检索的混合方案（RRF 融合）。提供集合、筛选、阅读模式、深色模式等功能，无账号系统，单密码登录，一条 docker compose 命令部署。LLM 失败时书签仍可保存，AI 分析在 API 恢复后补跑。技术栈为 React 19 + Express/tRPC + PostgreSQL 17/pgvector，需配置 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 粘贴 URL 后自动抓取、LLM 摘要、自动分类打标签并生成向量嵌入
- pgvector 语义搜索与 PostgreSQL 全文检索的 RRF 混合搜索
- 单租户、无账号追踪，docker compose 一条命令部署
- LLM 调用失败时书签仍保存，各步骤独立重试

## 适用场景

- 个人收藏网页链接并自动生成摘要与分类
- 用自然语言描述搜索历史保存的文章
- 在自己服务器上管理书签数据，不依赖第三方托管服务

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L7: A self-hosted bookmark manager that uses AI to do the work for you. Paste a link — Stash fetches the content, summar
> L17: - **AI-powered processing** — Paste a URL and Stash fetches the content, extracts metadata (title, favicon, OG imag

## 星数曲线

```mermaid
xychart-beta
    title "ayoub9360/stash-bookmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8ca127b5d103` · [字段定义](../../DATASET.md)*
