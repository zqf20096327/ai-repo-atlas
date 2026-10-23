# nambok/mentedb

⭐ 120 · Rust · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/nambok/mentedb) · [官网](https://mentedb.com) · 个人维护

**面向 AI agent 记忆的 Rust 数据库引擎：存储、检索与上下文预组装**

用 Rust 从底层构建的 agent 记忆数据库引擎，非对既有数据库的封装。提供 WAL、HNSW 向量检索与 BM25 融合、知识图谱、双时态有效期、矛盾检测与信念传播、按 token 预算组装上下文等机制。单次 process_turn 调用即可完成嵌入、混合检索、情景存储与模式抽取；基础认知管线无需 LLM，更丰富的语义抽取与实体图谱需配置 LLM。部署方式有托管云服务与自托管（cargo、Docker），并提供 Python/TypeScript SDK、gRPC/REST/MCP 三种接入路径及 LangChain/CrewAI 集成包。README 声明处于 Beta，API 可能随次版本变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 写入时智能：质量过滤、去重、矛盾检测与信念传播
- 混合检索：HNSW 向量 + BM25 经倒数排名融合，可选重排与 MMR
- 实体中心记忆：自动抽取类型化实体并以图边关联记忆
- 本地 Candle 嵌入（all-MiniLM-L6-v2）零配置语义检索，无需 API key

## 适用场景

- 给自建 agent 提供带认知分层的长期记忆存储
- 多 agent 场景下按记忆空间与 ACL 隔离记忆
- 通过 MCP 让 Claude Code/Cursor/Copilot 等工具自动积累与调用记忆

## 场景标签

`Agent 记忆` `向量数据库` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L9: MenteDB is a purpose built database engine for AI agent memory. Not a wrapper around existing databases, but a groun
> L103: Memory is one call. `process_turn` embeds the user message, recalls what is

## 星数曲线

```mermaid
xychart-beta
    title "nambok/mentedb 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 118 --> 121
    line [119, 120, 120]
```

2026-10-18 119 → 2026-10-23 120（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e58e0db0ef31` · [字段定义](../../DATASET.md)*
