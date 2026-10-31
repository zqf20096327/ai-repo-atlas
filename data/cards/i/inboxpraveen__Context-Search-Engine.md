# inboxpraveen/Context-Search-Engine

⭐ 14 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/inboxpraveen/Context-Search-Engine) · [官网](https://inboxpraveen.github.io/projects/project-1.html) · 个人维护

**自托管文档混合搜索引擎：BM25+向量检索，结果带出处与排名理由**

面向自有文档的自托管搜索引擎：索引 PDF/DOCX/PPTX/Markdown/HTML 等格式，监听文件夹变更并增量更新。检索提供 BM25（SQLite FTS5）、稠密向量（任意 sentence-transformers 模型）与 RRF 融合的 hybrid 三种策略，可选用 cross-encoder 重排；每个结果返回页面、精确段落、命中的检索器与排名原因、各阶段耗时。单进程单 SQLite 文件运行，无外部服务；明确声明不使用语言模型改写结果。附带 Web UI、REST API（OpenAPI）、CLI、评测命令、Prometheus 指标与 API key 认证，也可作为 Python 库使用。

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

- lexical/dense/hybrid 三策略 + 可选 cross-encoder 重排，RRF 融合
- 每个结果带页面、字符区间、排名原因、置信标签与各阶段耗时
- 文件夹监听：新增秒级索引、修改生成新版本、删除移出索引
- 单进程单 SQLite 文件，附 Web UI、REST API、CLI、eval 评测（recall/MRR/nDCG/延迟）与 Prometheus 指标

## 适用场景

- 给自己的 PDF/Office/Markdown 文档库做可解释的本地搜索
- 为 RAG 流水线提供可溯源的检索层
- 用自有标注查询对比评估不同检索与重排策略

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: contextsearch is a self-hosted search engine for your own documents. Point it at a folder of PDFs, Word and PowerPoi
> L16: - Searches three ways: `lexical` (BM25 on SQLite FTS5), `dense` (any sentence-transformers model, several at once i

## 星数曲线

```mermaid
xychart-beta
    title "inboxpraveen/Context-Search-Engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6e94715bd94b` · [字段定义](../../DATASET.md)*
