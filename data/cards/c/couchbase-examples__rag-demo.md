# couchbase-examples/rag-demo

⭐ 25 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/couchbase-examples/rag-demo) · 组织维护

**基于 Couchbase 向量检索的 PDF 对话 RAG 演示应用**

Streamlit 演示应用：上传 PDF 后在聊天框提问，用 Couchbase 向量检索相关片段作为上下文交给 OpenAI 生成回答，并同时展示纯 LLM 回答作对照。提供两种向量检索实现：CouchbaseQueryVectorStore（Hyperscale/Composite 向量索引，SQL++ 余弦相似度）与 CouchbaseSearchVectorStore（Search 服务，需手动导入索引）。LLM 回答复用 CouchbaseCache 缓存以减少重复调用。需自备 OpenAI API key 与 Couchbase Server 7.6+/8.0+ 或 Capella，配置 secrets.toml 后以 streamlit run 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两种 Couchbase 向量检索实现（Query 向量索引与 Search 服务）
- CouchbaseCache 缓存 LLM 响应，避免重复调用
- 每个问题并列输出 RAG 回答与纯 LLM 回答
- 支持 Hyperscale/Composite 索引与量化参数（SQ/PQ）配置说明

## 适用场景

- 体验用 Couchbase 向量检索做 PDF 问答的 RAG 流程
- 对比 Couchbase 两种向量检索方案的实现差异
- 学习 LangChain 与 Couchbase 集成及响应缓存机制

## 场景标签

`RAG` `文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This is a demo app built to chat with your custom PDFs using the vector search capabilities of Couchbase to augment 
> L16: You can upload your PDFs with custom data & ask questions about the data in the chat box.
> L23: For RAG, we are using LangChain, Couchbase Vector Search & OpenAI. We fetch parts of the PDF relevant to the questi

## 星数曲线

```mermaid
xychart-beta
    title "couchbase-examples/rag-demo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e7351907c92` · [字段定义](../../DATASET.md)*
