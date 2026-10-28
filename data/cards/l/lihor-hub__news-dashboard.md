# lihor-hub/news-dashboard

⭐ 37 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/lihor-hub/news-dashboard) · [官网](https://docs.lihor.ro/) · 个人维护

**自托管技术新闻聚合阅读台，带 AI 摘要与问答**

面向开发者的自托管技术新闻中心：聚合 RSS/Atom、GitHub release、Hacker News/GitHub trending 与自抓取源，生成按新鲜度与个性化推荐排序的 Today Feed，支持文章分诊状态、来源健康、搜索与阅读历史。配置 AI provider 后提供 OpenAI 兼容嵌入、带引用的 Ask AI 问答、文章要点与个性化简报；不配置 AI 时仍可作为新闻聚合器运行（demo 模式无 AI key）。技术栈为 FastAPI + React + PostgreSQL(pgvector)，可选 Neo4j 知识图谱。

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

- RSS/Atom、GitHub release、Hacker News/GitHub trending 等多源聚合与 Today Feed 排序
- 配置 AI provider 后提供带引用的 Ask AI、文章智能要点与个性化简报
- Google Reader 兼容同步 API，可接入 NetNewsWire/Reeder 等第三方 RSS 客户端
- Docker/Helm/Kubernetes 部署支持，本地密码认证与可选 Keycloak 登录

## 适用场景

- 在一个自托管实例里订阅和筛选我关注的技术新闻源
- 让 AI 帮我把文章读成要点、背景与带引用的追问回答
- 每天收一份基于自己源集合的个性化简报

## 场景标签

 · 领域:新闻聚合/自托管应用

## 证据(README 行号)

> L58: - OpenAI-compatible embeddings, cited Ask AI answers, article intelligence, and generated briefings when an AI prov
> L92: Want to try News Dashboard before self-hosting it? One command runs a

## 星数曲线

```mermaid
xychart-beta
    title "lihor-hub/news-dashboard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-28 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2ce764f75131` · [字段定义](../../DATASET.md)*
