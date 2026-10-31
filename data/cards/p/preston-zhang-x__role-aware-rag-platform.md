# preston-zhang-x/role-aware-rag-platform

⭐ 16 · Python · Apache-2.0 · 推送 2026-05-15 · [GitHub](https://github.com/preston-zhang-x/role-aware-rag-platform) · 个人维护 · 中文 README

**面向企业文档的带权限过滤 RAG 问答平台**

面向企业内知识库的 RAG 应用：检索入口按用户角色（admin/manager/staff）过滤文档权限，将角色过滤、文档权限、混合检索与回答溯源整合进单一 QA 流程。重点解析日式 Excel 仕様書（保留合并单元格、KV 区域、表结构），检索支持 vector/BM25/hybrid/hybrid_rerank 四种模式。后端 FastAPI，前端 React+Vite，向量库 Qdrant，标准配置为 Ollama + BGE-M3 + qwen3.5:4b 本地运行。另附独立 Excel→Markdown 转换脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索前按 allowed_roles 做角色权限过滤（admin/manager/staff）
- 日式 Excel 仕様書专用解析（保留 Sheet 语义、合并单元格、KV/表区域）
- 四种检索模式：vector / bm25 / hybrid（RRF 融合）/ hybrid_rerank
- 回答返回命中来源、chunk 位置、token 与延迟；RAGBench emanual 子集离线评估 Accuracy 90.9%

## 适用场景

- 在企业内知识库检索中限制用户按角色查看文档
- 对日式 Excel 仕様書/設計書做结构化问答
- 需要回答来源可溯源的内部 QA 系统搭建

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L20: Role Aware RAG Platform は、企業内文書を対象にした RAG アプリケーションです。ユーザーロール、文書権限、ハイブリッド検索、回答ソースの追跡を 1 つの QA フローに統合し、社内ナレッジ検索、設計書 Q
> L32: - **追跡可能な回答**：回答本文、ヒットしたソース、chunk 位置、token、レイテンシを返却

## 星数曲线

```mermaid
xychart-beta
    title "preston-zhang-x/role-aware-rag-platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3084683303bb` · [字段定义](../../DATASET.md)*
