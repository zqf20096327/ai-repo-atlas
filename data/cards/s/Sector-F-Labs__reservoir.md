# Sector-F-Labs/reservoir

⭐ 14 · Rust · BSD-3-Clause · 推送 2026-10-29 · [GitHub](https://github.com/Sector-F-Labs/reservoir) · [官网](http://sectorflabs.com/reservoir/) · 组织维护

**面向 LLM 对话的 CLI 记忆存储：Neo4j 图库与语义检索**

以 CLI 为主要接口的对话消息存储层：将消息写入 Neo4j 图数据库，用 BGE-Large-EN-v1.5 计算 embedding，并在余弦相似度超过 0.85 时建立消息间 SYNAPSE 关系，从而支持关键词/语义搜索与线程上下文检索；按 partition/instance 层级做多租户隔离，支持 export/import 备份与批量导入。内置 egui+wasm 编译的只读浏览器图视图（默认监听 localhost，无鉴权）。用 Rust 实现，通过 cargo 运行，需外部 Neo4j 并以 reservoir.toml 或环境变量配置连接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Neo4j 图数据模型（MessageNode/EmbeddingNode/SYNAPSE 等关系）
- BGE-Large-EN-v1.5 计算 embedding，余弦相似度>0.85 建立语义关联
- 关键词与语义两种搜索方式及线程上下文检索
- 内置浏览器图视图（egui 编译为 wasm，只读、默认无鉴权）

## 适用场景

- 为无状态的聊天系统提供持久化对话记忆与上下文检索
- 跨对话引用语义相关的历史消息
- 多租户场景下按 partition/instance 隔离管理对话数据

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L5: Reservoir is a CLI-first memory store for conversational messages. It stores messages in a Neo4j graph database, com
> L19: Reservoir provides a CLI workflow that:
> L24: - Enables semantic search and thread context retrieval

## 星数曲线

```mermaid
xychart-beta
    title "Sector-F-Labs/reservoir 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-29 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c84f6563b037` · [字段定义](../../DATASET.md)*
