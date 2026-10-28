# ontorag/ontorag

⭐ 32 · Python · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/ontorag/ontorag) · [官网](https://ontorag.github.io) · 组织维护

**本体优先的 RAG 框架：从文档构建可治理的 RDF 知识图谱**

以本体（Ontology）为中心的文档处理管线：文档经内容寻址哈希后解析为 DTO，LLM 仅用于提出候选类/属性建议（提案而非定论），经人工可审的 Schema Card 确定性合并后，从文档抽取带出处的 RDF 实例（W3C Web Annotation 溯源），最终通过 SPARQL 端点与两个 MCP 服务器供 LLM agent 查询。LLM 调用默认走 OpenRouter，可指向任意 OpenAI 兼容端点（含本地 Ollama）实现离线运行。以 Python 库与 CLI 形式提供（Python ≥ 3.12），内置引擎无需外部依赖与 API key，PDF 等格式经可选 extras 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档内容寻址（SHA-256）：相同内容不重复处理，输出可重放的 DTO
- LLM 提案、代码裁决、Schema Card 版本化且带 origin 溯源
- 每条抽取事实通过 W3C Web Annotation 关联到原文段落与页码
- 提供 Knowledge MCP 与 Ontology Catalog MCP 两个服务器，支持 SPARQL 查询

## 适用场景

- 构建可审计、可治理的企业知识图谱而非纯文本检索
- 复用 FOAF/Schema.org 等标准本体作为抽取的基础 schema
- 让 LLM agent 通过 MCP 工具查询与组合本体、检索图谱实例
- 离线/私有化部署：接入本地 Ollama 等 OpenAI 兼容端点

## 场景标签

`RAG` `知识图谱` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: **OntoRAG** is an ontology-first alternative to traditional Retrieval-Augmented Generation (RAG).
> L23: > **Baselines --> Documents --> DTOs --> Ontology --> Instances --> SPARQL --> MCP tools --> LLM reasoning**

## 星数曲线

```mermaid
xychart-beta
    title "ontorag/ontorag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5193b776b04d` · [字段定义](../../DATASET.md)*
