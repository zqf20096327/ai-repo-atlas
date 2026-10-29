# mashrulhaque/EasyAppDev.Blazor.AutoComplete

⭐ 20 · C# · 推送 2025-12-21 · [GitHub](https://github.com/mashrulhaque/EasyAppDev.Blazor.AutoComplete) · 个人维护

**Blazor 自动补全组件，含 AI 语义搜索与 OData/向量库集成**

面向 Blazor 开发者的 AutoComplete（TypeAhead）UI 组件库：核心提供多字段搜索、四种过滤策略（含 Levenshtein 模糊匹配）、8 种显示模式、分组、10 万条数据的虚拟化滚动、主题系统与 WCAG 2.1 AA 可访问性。通过可选包扩展：OData v3/v4 服务端过滤（自动生成 $filter）、基于文本嵌入与余弦相似度的 AI 语义搜索（OpenAI/Azure OpenAI，含双缓存与预热），以及 pgvector、Azure AI Search、Pinecone、Qdrant、CosmosDB 五种向量库提供方。以 NuGet 包分发，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 语义搜索（嵌入+余弦相似度），支持 OpenAI/Azure OpenAI 及任意嵌入提供方
- OData v3/v4 服务端过滤，自动生成 $filter 查询
- 5 种向量数据库提供方（pgvector/Azure AI Search/Pinecone/Qdrant/CosmosDB）
- 10 万+条目虚拟化与 WCAG 2.1 AA 可访问性

## 适用场景

- 在 Blazor 应用中添加支持拼写容错的搜索下拉框
- 为 OData API 接入服务端过滤的自动补全
- 用语义搜索按含义而非关键词检索数据，配合向量库持久化嵌入

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A high-performance, AI-powered AutoComplete (TypeAhead) component for Blazor applications with semantic search, ODat
> L367: ## AI Semantic Search

## 星数曲线

```mermaid
xychart-beta
    title "mashrulhaque/EasyAppDev.Blazor.AutoComplete 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `276152376861` · [字段定义](../../DATASET.md)*
