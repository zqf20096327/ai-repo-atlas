# memvid/memvid

⭐ 16,603 · Rust · Apache-2.0 · 推送 2026-07-14 · [GitHub](https://github.com/memvid/memvid) · [官网](https://www.memvid.com) · 组织维护

**为 AI Agent 提供单文件、免数据库的持久记忆层**

Memvid 将数据、嵌入、检索结构与元数据打包为单个 .mv2 文件，作为 AI Agent 的可移植记忆层，无需运行 RAG 流水线或服务器式向量数据库。核心机制是把记忆组织为不可变的 Smart Frame 序列（借鉴视频编码思路），支持追加写入、按时间线回溯与分支、崩溃安全。提供 CLI、Node.js、Python、Rust SDK；检索支持 BM25 全文、本地 ONNX 向量嵌入（BGE/Nomic/GTE）与 OpenAI 云端嵌入，需 Rust 1.85+。README 中含 LoCoMo 等基准数据，此处不作评价。

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

## 动量与使用信号

- 维护:`maintenance` — 距上次 push 95.8 天,年发版 10,23 位贡献者
- 涨星:近 1 天 **+5**(自 20261016 起算)
- 安装:npm 包 `memvid-cli` 月下载 4,863
- 平台:— · 协议:OPENAI-API

## 能力要点

- 数据、嵌入与索引打包为单个 .mv2 文件，无 sidecar 文件
- Smart Frame 追加式设计：支持时间线回溯、分支与查询过去状态
- 本地 ONNX 嵌入（BGE/Nomic/GTE）与 OpenAI API 嵌入可选
- 提供 npm、pip、cargo 多语言 SDK 与 CLI

## 适用场景

- 给长时间运行的 AI Agent 添加持久记忆
- 构建离线优先、可携带的知识库
- 需要审计与回放记忆状态的 Agent 工作流

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6:  Memvid is a single-file memory layer for AI agents with instant retrieval and long-term memory.
> L38: Memvid is a portable AI memory system that packages your data, embeddings, search structure, and metadata into a si
> L42: The result is a model-agnostic, infrastructure-free memory layer that gives AI agents persistent, long-term memory 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `3c5dc68b229b` · [字段定义](../../DATASET.md)*
