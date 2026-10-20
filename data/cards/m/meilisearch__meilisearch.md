# meilisearch/meilisearch

⭐ 59,596 · Rust · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/meilisearch/meilisearch) · [官网](https://www.meilisearch.com) · 组织维护 · 中文 README

**为网站与应用提供 AI 混合搜索的搜索引擎 API**

开源搜索引擎，提供 RESTful API 与多语言 SDK，供应用与网站集成搜索功能。核心机制包括语义与全文结合的混合搜索、输入即搜（50 毫秒内返回）、容错、过滤与分面、地理搜索、多语言支持（含中文/日文优化）与多租户。支持自然语言对话式搜索并生成基于检索结果的 AI 回答，可与 LangChain 及 MCP 配合。分社区版（MIT）与企业版（商业许可/BSL 1.1，生产环境需商业协议），官方提供 Cloud 托管服务，并默认收集可关闭的匿名遥测数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.7 天,年发版 63,229 位贡献者
- 涨星:近 1 天 **+10**(自 20261016 起算)
- 平台:— · 协议:MCP

## 能力要点

- 混合搜索：语义搜索与全文搜索结合
- 对话式搜索：基于检索结果生成 AI 回答
- 支持地理搜索、分面过滤、同义词与多租户
- 开箱支持 LangChain 与 Model Context Protocol

## 适用场景

- 给电商网站加带过滤分面的商品搜索
- 为媒体平台做语义混合搜索找影片
- 让用户用自然语言提问并获得基于站内内容的回答
- 多租户 SaaS 中的联系人/客户搜索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L45: - **Hybrid search:** Combine the best of both semantic & full-text search to get the most relevant results
> L57: - **Conversational search:** let users ask questions in natural language and get AI-generated answers grounded in y
> L62: - **AI-ready:** works out of the box with LangChain and the Model Context Protocol (MCP)

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `61bb05221049` · [字段定义](../../DATASET.md)*
