# moodlehq/wiki-rag

⭐ 53 · Python · BSD-3-Clause · 推送 2026-06-15 · [GitHub](https://github.com/moodlehq/wiki-rag) · 组织维护

**把 MediaWiki 站点变成 RAG 问答服务的实验性系统**

Moodle Research 发起的实验项目：通过 MediaWiki API（非爬虫）抓取站点内容与元数据，存为 JSON 并载入 Milvus 向量库，采用混合检索（向量+关键词、融合重排）、上下文感知查询改写与可选 HyDE，做检索后优化（POP/POC）。模型可配置为任意 OpenAI 兼容提供方，用 LangGraph 编排。对外提供四个可执行命令：加载、索引、搜索 CLI、wr-server（以 OpenAI API 形式暴露、支持流式与 bearer 认证），另含内置 MCP server。仅支持 Milvus Standalone/Distributed，Lite 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MediaWiki API 抓取全站作为知识库，支持增量加载与索引
- Milvus 混合检索 + 融合重排 + POP/POC 检索后优化
- wr-server 以 OpenAI API（v1/models、v1/chat/completions）暴露，支持流式与 bearer 认证
- 内置 MCP server 暴露 prompts/resources/tools

## 适用场景

- 把组织的 MediaWiki 文档站变成可对话问答的知识库
- 以 OpenAI 兼容接口接入现有聊天前端做 wiki 问答
- 教育技术场景下基于 Moodle 文档做 RAG 实验研究

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L75:  - `wr-server`: A comprehensive and secure web service (documented with OpenAPI) that allows users to interact with
> L149:  * Exposed as a model using standard OpenAI API endpoints (`v1/models` and `v1/chat/completions`). Protected with 
> L9: Labeled as an experimental project, Wiki-RAG is part of the Moodle Research initiative, aiming to explore and develo

## 星数曲线

```mermaid
xychart-beta
    title "moodlehq/wiki-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9e8d18b07c0b` · [字段定义](../../DATASET.md)*
