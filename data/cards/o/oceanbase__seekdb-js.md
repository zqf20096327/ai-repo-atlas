# oceanbase/seekdb-js

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/oceanbase/seekdb-js) · [官网](https://seekdb.ai) · 组织维护 · 中文 README

**seekdb/OceanBase 向量数据库的 JS/TS SDK，含语义与混合检索**

OceanBase 官方维护的 monorepo，为 seekdb 与 OceanBase 提供向量数据库 JavaScript/TypeScript SDK。支持 Embedded（本地文件、原生绑定预编译二进制覆盖 Linux/macOS/Windows 四平台）与 Server 两种运行模式（连 OceanBase 需传 tenant）。核心包 seekdb 提供集合/Schema/全文/向量/稀疏向量索引、query 与 hybridSearch；另含多个嵌入函数包：本地 all-MiniLM-L6-v2 默认嵌入（无需 API Key）、通义千问 DashScope、OpenAI、Jina、BM25 稀疏嵌入及 Prisma 适配器，支持自定义嵌入接口。

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

- Embedded 本地模式无需服务端，预编译二进制覆盖 Linux/macOS ARM64/Windows x64
- 全文、稠密向量、稀疏向量三类索引与 hybridSearch 混合检索
- 内置本地默认嵌入（all-MiniLM-L6-v2，无需 API Key），另提供 Qwen/OpenAI/Jina/BM25 嵌入包
- 支持自定义 EmbeddingFunction 与 SparseEmbeddingFunction 接口，含 Prisma 适配器

## 适用场景

- 在 Node.js/TypeScript 项目中为 seekdb/OceanBase 做语义检索
- 无需部署服务端，本地嵌入式模式快速开发向量搜索原型
- 结合关系表与向量检索结果做关联查询

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5:  Vector database SDK for JavaScript/TypeScript with built-in semantic search
> L7:  Works seamlessly with seekdb and OceanBase
> L27: |`seekdb`|Core SDK for seekdb operations|

## 星数曲线

```mermaid
xychart-beta
    title "oceanbase/seekdb-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6ad3ee0b2ec5` · [字段定义](../../DATASET.md)*
