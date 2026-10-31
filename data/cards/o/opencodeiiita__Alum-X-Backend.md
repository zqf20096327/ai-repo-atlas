# opencodeiiita/Alum-X-Backend

⭐ 13 · Java · 推送 2026-01-31 · [GitHub](https://github.com/opencodeiiita/Alum-X-Backend) · 组织维护

**校友导师制社交平台 AlumX 的 Spring Boot 后端**

面向连接学生、校友与教授的校友社交平台 AlumX 的后端：提供 JWT/OAuth2 登录与角色访问控制、导师制工作流（申请/接受/聊天）、校友博客与互动排序、按公司/技能/年份等条件的校友搜索、AI 辅助简历生成（用户提供 API key）。技术栈为 Spring Boot 4、MySQL/Redis、向量库（Pinecone/Weaviate/FAISS）配合 OpenAI/Gemini/HuggingFace API 与 LangChain/Spring AI 做 RAG 语义搜索。需 Java 21、Maven、PostgreSQL 环境，git clone 后 mvn 构建运行，配置由导师提供的 .env 文件注入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JWT + OAuth2（Google/LinkedIn）认证与三种角色访问控制
- 导师制工作流含师生聊天与教授调解角色
- RAG 语义搜索与 AI 辅助简历生成（用户提供 API key）
- MySQL 主库 + Redis 缓存 + 向量库的数据库设计

## 适用场景

- 搭建连接学生与校友的导师制社交平台
- 为校友网络应用提供认证、聊天、博客、职位帖等后端 API
- 在简历生成与校友搜索中加入语义检索能力

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: **AlumX** is a scalable, backend-heavy alumni networking platform designed to connect **students, alumni, and facult
> L41: - AI-powered semantic search (RAG-based)

## 星数曲线

```mermaid
xychart-beta
    title "opencodeiiita/Alum-X-Backend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `758c7213d1ee` · [字段定义](../../DATASET.md)*
