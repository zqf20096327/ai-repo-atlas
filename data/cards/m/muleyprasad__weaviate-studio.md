# muleyprasad/weaviate-studio

⭐ 18 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/muleyprasad/weaviate-studio) · [官网](https://marketplace.visualstudio.com/items?itemName=prasadmuley.weaviate-studio) · 个人维护

**在 VS Code 内管理 Weaviate 向量库的扩展：查询、浏览、备份**

TypeScript/React 编写的 VS Code 扩展，用于连接本地、自托管或云端 Weaviate 实例，提供多连接管理、可视化数据浏览器（4 种向量搜索模式、过滤、JSON/CSV 导出）、Monaco 驱动的 GraphQL 编辑器、schema 浏览、RBAC 用户/角色管理、只读模式、多后端（S3/GCS/Azure/filesystem）备份恢复与集群健康监控。另含生成式搜索界面，依赖 Weaviate 服务端生成模块配置，扩展自身无需额外 API key。通过 VS Code Marketplace / Open VSX 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多连接管理与集群健康监控面板
- 数据浏览器支持 4 种向量搜索模式与查询 profiling
- RBAC 管理、API key 轮换与连接级只读保护
- 生成式搜索：多集合 RAG 问答，来源标注与服务端生成模块配置

## 适用场景

- 在 VS Code 内浏览和查询 Weaviate 数据，无需切换浏览器
- 管理生产实例的备份、恢复与 RBAC 权限
- 对多个集合做自然语言问答并查看检索上下文来源

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L9: **A powerful VS Code extension for managing Weaviate vector databases with an intuitive GraphQL
> L41: - **Generative Search:** Ask natural-language questions across one or more collections—configure top-k results per 
> L148: - Relies on Weaviate's server-side generative config—no additional API keys needed in the extension

## 星数曲线

```mermaid
xychart-beta
    title "muleyprasad/weaviate-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `18700d0e8782` · [字段定义](../../DATASET.md)*
