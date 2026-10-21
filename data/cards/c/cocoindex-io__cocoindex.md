# cocoindex-io/cocoindex

⭐ 11,726 · Rust · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/cocoindex-io/cocoindex) · [官网](https://cocoindex.io) · 组织维护 · 中文 README

**面向 AI agent 的增量数据索引/RAG 流水线 Python 框架**

开源 Python 框架，把代码库、PDF、Slack、会议记录、视频等数据源转为持续新鲜的目标索引（pgvector/LanceDB/Neo4j 等向量库与图库），供 AI agent 与 LLM 应用检索。核心是声明式增量引擎：声明目标状态后引擎持续同步，仅重算 Δ，支持按行溯源、跨 join/lookup 的变更传播与失效重算。内置核心为 Rust，Apache 2.0 许可，另提供 MCP 代码索引服务与企业版页面。以 pip 安装，附 20+ 示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式目标状态（Target = F(Source)），仅重算 Δ 的增量同步引擎
- 端到端按行数据溯源，代码变更可做细粒度失效与重算
- Rust 核心引擎，默认并行、零拷贝变换与故障隔离
- 示例覆盖代码索引、PDF RAG、知识图谱、结构化抽取、CSV→Kafka

## 适用场景

- 为生产 AI agent 构建持续新鲜的知识库/上下文管道
- 增量维护代码库或文档库的向量索引供语义检索
- 把会议记录、播客等转录内容增量抽取为知识图谱

## 场景标签

`RAG` `知识图谱` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5:  Star us&nbsp;❤️&nbsp;→ &nbsp; Star CocoIndex on GitHub — open-source Python framework for RAG, vector search, and l
> L10:  CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context f
> L47: pip install -U cocoindex

## 星数曲线

```mermaid
xychart-beta
    title "cocoindex-io/cocoindex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 11711 --> 11727
    line [11712, 11726, 11726]
```

2026-10-18 11,712 → 2026-10-21 11,726（+14）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `53a548db3c92` · [字段定义](../../DATASET.md)*
