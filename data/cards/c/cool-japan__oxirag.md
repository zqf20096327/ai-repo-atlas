# cool-japan/oxirag

⭐ 13 · Rust · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/cool-japan/oxirag) · [官网](https://github.com/cool-japan/oxirag) · 个人维护

**纯 Rust 实现的四层 RAG 引擎库，含 SMT 逻辑验证与知识图谱**

以 Rust crate 形式提供的 RAG 流水线库，由四层组成：Echo 语义检索（向量嵌入、可插拔 embedding provider）、Speculator 草稿验证（规则式与 Candle SLM 两种）、Judge 层基于 OxiZ SMT 求解器对声明做形式化逻辑验证、Graph 层提供 GraphRAG（实体关系抽取、图遍历、混合检索）。另含前缀 KV 缓存与查询模式蒸馏跟踪模块。支持原生 Tokio 与 WASM 两种运行时，通过 Cargo feature flags 按层启用，面向在 Rust 项目中集成 RAG 能力的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层架构：语义检索、草稿验证、SMT 逻辑验证、GraphRAG
- OxiZ SMT 求解器对提取声明做形式化验证
- 上下文感知前缀缓存（LRU+TTL、部分命中）与蒸馏训练数据导出
- 原生 Tokio 与 WASM 双运行时，CUDA/Metal 加速为可选 feature

## 适用场景

- 在 Rust 项目中嵌入带验证层的 RAG 检索流水线
- 需要形式化逻辑验证检索结果的问答系统
- 浏览器/边缘端 WASM 环境运行 RAG

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L7: A four-layer Retrieval-Augmented Generation (RAG) engine in **Pure Rust** with SMT-based logic verification and know
> L17: OxiRAG provides a robust RAG pipeline with four specialized layers:

## 星数曲线

```mermaid
xychart-beta
    title "cool-japan/oxirag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `dd1872b33daa` · [字段定义](../../DATASET.md)*
