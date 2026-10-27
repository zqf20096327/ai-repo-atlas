# bridgerust/bridgerust

⭐ 27 · Rust · 推送 2026-03-03 · [GitHub](https://github.com/bridgerust/bridgerust) · [官网](https://bridgerust.dev) · 组织维护

**Rust 跨语言绑定框架与通用向量数据库客户端 Embex 的单仓库**

monorepo 内含三个部分：Embex 是统一 API 的向量数据库客户端，覆盖 LanceDB、Qdrant、Pinecone、Chroma、PgVector、Milvus、Weaviate 七种后端，切换后端仅需改一行配置，Rust 核心带 SIMD 加速，发布到 PyPI 与 npm；BridgeTime 是 Day.js/Moment 风格的 Rust 日期时间工具库；BridgeRust 框架用单个 #[export] 宏统一 PyO3 与 napi-rs 绑定生成，另附 bridge 脚手架 CLI 与 embex-cli 集合管理 CLI。bridgeq 任务队列处于 preview/alpha 状态。面向需要跨 Python/Node.js 交付 Rust 库的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Embex 单一 API 接入七种向量数据库（LanceDB/Qdrant/Pinecone/Chroma/PgVector/Milvus/Weaviate）
- 单一 #[export] 宏统一 PyO3 与 napi-rs 跨语言绑定
- embex-cli 命令行管理 Embex 集合，bridge CLI 脚手架新建库
- bridgeq 队列工具链含 Redis 与 PostgreSQL 持久化适配器（preview/alpha）

## 适用场景

- Python/Node.js 项目用统一客户端切换不同向量数据库后端
- 把 Rust 核心库同时发布到 PyPI 与 npm 而不维护两套绑定
- 在终端管理 Embex 向量集合

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L14: BridgeRust is a monorepo shipping two AI-infrastructure products — **Embex** and **BridgeTime** — and the **BridgeR
> L52: Embex abstracts vector database fragmentation into a single, production-ready API. Switch from LanceDB to Qdrant to
> L59: Supported providers: **LanceDB** • **Qdrant** • **Pinecone** • **Chroma** • **PgVector** • **Milvus** • **Weaviate*

## 星数曲线

```mermaid
xychart-beta
    title "bridgerust/bridgerust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bfea3e7ce569` · [字段定义](../../DATASET.md)*
