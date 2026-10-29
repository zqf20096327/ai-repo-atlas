# astandrik/ydb-qdrant

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-06-29 · [GitHub](https://github.com/astandrik/ydb-qdrant) · [官网](https://ydb-qdrant.tech) · 个人维护

**YDB 上跑 Qdrant 兼容 API 的向量存储检索服务**

用 Node.js/TypeScript 编写的服务与 npm 库，把向量存入 YDB 的全局单表布局（qdrant_all_points），在 embedding 上做精确 KNN 搜索，并暴露 Qdrant 兼容的 REST API（/collections、/points/*）。三种使用方式：HTTP 服务、进程内程序化客户端（createYdbQdrantClient）、GitHub App 代码索引器（含公开 beta 与自托管）。认证依赖 YDB 环境变量，另有 npm 安装、Docker 与 all-in-one 本地容器部署路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qdrant 兼容 REST API 与镜像同样语义的 npm 程序化客户端
- YDB 全局单表布局上的精确 KNN 向量搜索
- all-in-one Docker 镜像同时包含 YDB 与服务，无需外部依赖
- GitHub App 代码索引器支持 MCP/IDE/coding-agent 检索

## 适用场景

- 已有 YDB 的团队用它替代独立向量库做语义检索
- 让 Roo Code/Cline 等 IDE agent 通过 Qdrant 协议检索代码库
- 在业务代码中以库形式直接调用 YDB 向量搜索

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L19: Qdrant-compatible Node.js/TypeScript **service and npm library** that stores and searches vectors in YDB using a gl
> L22: - **HTTP server**: Qdrant-compatible REST API (`/collections`, `/points/*`) on top of YDB.
> L23: - **Node.js package**: programmatic client via `createYdbQdrantClient` for direct YDB-backed vector search without 

## 星数曲线

```mermaid
xychart-beta
    title "astandrik/ydb-qdrant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `45e5fb3e08b6` · [字段定义](../../DATASET.md)*
