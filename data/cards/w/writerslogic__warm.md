# writerslogic/warm

⭐ 25 · Rust · Apache-2.0 · 推送 2026-10-31 · [GitHub](https://github.com/writerslogic/warm) · [官网](https://docs.holographic-memory.com/) · 组织维护

**给 AI agent 的本地记忆与混合检索 Rust 引擎，含 MCP 服务**

嵌入式 Rust 引擎，把全文检索（BM25、布尔、短语）、向量图索引、记忆 API（remember/recall/forget/explain）与向量符号事实存储（稀疏超向量、三重关系、Hopfield 清理）合并到本地目录，无网络调用与遥测。面向需要记忆的 agent、本地优先离线应用、需要检索服务的开发者及向量符号记忆研究者。提供 Node.js/C/WASM/UniFFI 绑定、HTTP 服务器（Python 客户端 warm-sdk）与 MCP 服务器（npx 安装）。README 附带与 hnswlib、tantivy、FAISS 等的基准结果并单列落后项；已发布 crate 0.6.1 为 AGPL，当前源码为 Apache-2.0。

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

- 单目录存储的混合检索：BM25 + 用户提供的 embeddings 融合
- 记忆 API 含遗忘、时间有效性与来源溯源
- 向量符号层：bind/bundle/permute 与 Hopfield 清理
- 无网络调用、无遥测，提供 MCP 服务器与可选 AES-256-GCM 加密

## 适用场景

- 为 agent 或助手接入本地对话记忆与事实存储
- 本地优先/离线应用嵌入文本与向量检索
- 通过 MCP 让编辑器或 agent 宿主使用记忆存储
- 做向量符号记忆的绑定/捆绑代数与容量实验

## 场景标签

`Agent 记忆` `向量数据库` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Local memory for agents and apps: full-text and vector search, a memory API and a vector-symbolic fact store in on
> L33: WARM is a Rust library that stores text, vectors and facts in a
> L202: `warm-mcp` serves a store to any Model Context Protocol client over stdio or HTTP:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d1ab504aac55` · [字段定义](../../DATASET.md)*
