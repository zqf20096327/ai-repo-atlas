# stefanros481/ott-platform

⭐ 16 · Python · Apache-2.0 · 推送 2026-03-16 · [GitHub](https://github.com/stefanros481/ott-platform) · 个人维护

**用 Claude Code 开发的 OTT 流媒体学习平台示例项目**

以实现一个可运行的 OTT 流媒体平台（VOD 目录、EPG、直播、推荐、多档位授权、TSTV、ClearKey DRM）为载体，学习 Claude Code 辅助开发的实践项目。每个编号分支对应一个独立功能实现，功能开发用 speckit 技能先写规格与计划再写代码。AI 部分：基于 sentence-transformers + pgvector 的内容推荐（For You / More Like This）、自然语言内容分析查询与 FastMCP 只读目录服务。README 明确声明非生产就绪、仅供学习。技术栈为 FastAPI + PostgreSQL + Redis + 双 React 前端，Docker Compose 一键启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 推荐基于 all-MiniLM-L6-v2 嵌入与 pgvector 余弦相似度（HNSW 索引）
- 编号分支结构，每支对应一个独立功能实现
- FastMCP 服务器提供对内容目录的只读 AI agent 访问
- Docker Compose 一键启动全栈并自动播种数据（70 部影片、25 频道、7 天 EPG）

## 适用场景

- 学习 Claude Code 在真实工程任务中的开发流程
- 参考 OTT 平台的推荐系统与授权分层实现
- 运行完整演示环境体验 VOD、EPG 与直播回看功能

## 场景标签

`推荐系统` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: This repo implements a working OTT platform (VOD catalog, EPG grid, live TV, recommendations, entitlements, and more
> L31: - AI-powered content recommendations using pgvector embeddings
> L118: - **AI:** sentence-transformers (`all-MiniLM-L6-v2`, 384-dim embeddings)

## 星数曲线

```mermaid
xychart-beta
    title "stefanros481/ott-platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `825e6b526fde` · [字段定义](../../DATASET.md)*
