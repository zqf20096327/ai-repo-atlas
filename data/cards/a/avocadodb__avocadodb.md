# avocadodb/avocadodb

⭐ 13 · Rust · MIT · 推送 2025-12-10 · [GitHub](https://github.com/avocadodb/avocadodb) · [官网](https://avocadodb.ai) · 组织维护

**面向 AI agent 的确定性上下文数据库，同一查询输出同一上下文**

用 Rust 编写的 span 级上下文编译器，替代向量数据库的 top-k 检索：文档切分为 20-50 行的 span 并附精确行号引用，经语义+词法混合检索、MMR 去重、token 装箱与确定性排序后输出可复现的 WorkingSet，可用 SHA256 校验。默认使用本地 fastembed 嵌入（minilm/nomic/bgelarge），也可切换 Ollama 或 OpenAI 作为嵌入提供方。提供 CLI、Python/TypeScript SDK、HTTP 服务端，另有 Docker 镜像（含 PostgreSQL+pgvector 扩展版）与 Kubernetes 部署清单，支持会话管理、explain 计划、WorkingSet diff 与增量重建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一查询确定性输出相同上下文，附 SHA256 上下文哈希可校验
- span 级索引（20-50 行）带精确行号引用
- 本地 fastembed 嵌入默认离线运行，可选 Ollama/OpenAI 提供方
- 提供 CLI、Python/TypeScript SDK、HTTP 服务、PostgreSQL 扩展与 Kubernetes 部署

## 适用场景

- 为 AI agent 的 RAG 流程提供可复现、可引用的上下文
- 替代现有向量数据库做确定性检索与 token 装箱
- 在 SQL 内（PostgreSQL 扩展）直接做确定性上下文编译
- 多轮会话中跟踪并回放 agent 的上下文历史

## 场景标签

`语义搜索` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L19: AvocadoDB is a span-based context compiler that replaces traditional vector databases' chaotic "top-k" retrieval wi
> L249: Query → Embed → [Semantic Search + Lexical Search] → Hybrid Fusion

## 星数曲线

```mermaid
xychart-beta
    title "avocadodb/avocadodb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `32df3f6f5082` · [字段定义](../../DATASET.md)*
