# arc-labs-ai/brain-db

⭐ 42 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/arc-labs-ai/brain-db) · 组织维护

**面向 AI agent 的记忆数据库：类型化记忆存储与融合检索**

用 Rust 实现的单核心记忆数据库，为 AI agent 存储四种记录（Memory/Entity/Statement/Relation），带溯源、置信度与双时间有效性。通过三级抽取管线（pattern→GLiNER→LLM）从原始记忆派生实体与关系，RECALL 以语义+词法+图三路检索做加权 RRF 融合；提供 ENCODE/RECALL/PLAN/REASON/FORGET 等认知动词与单一二进制线协议。限制：启动必须持有 LLM provider API key（写路径依赖 HyPE），本仓库不附带客户端/SDK。开发环境需 Docker 与 devcontainer CLI，以源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四种类型化记录，带溯源、置信度与双时间有效期
- 语义/词法/图三路检索加权 RRF 融合，单 Rust 核心单线协议
- 三级抽取管线（pattern→GLiNER→LLM）按 schema 准入派生类型化图
- 每 agent 记忆严格隔离，WAL 先于确认等七项存储不变量

## 适用场景

- 为长期运行的 agent 提供带溯源与时间语义的记忆后端
- 在自有词汇表 schema 上做实体锚定的类型化查询
- 替换向量库+图库+全文库拼装的多系统 agent 记忆栈

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L11: > **A memory database for AI agents.** Stores four record types — Memory, Entity, Statement, Relation — with explic
> L99: - **`brain-server`** — the database. Binary wire protocol on the data port; a loopback HTTP admin listener (stats, 

## 星数曲线

```mermaid
xychart-beta
    title "arc-labs-ai/brain-db 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cf181e1db7b7` · [字段定义](../../DATASET.md)*
