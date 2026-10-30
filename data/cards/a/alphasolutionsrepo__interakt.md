# alphasolutionsrepo/interakt

⭐ 16 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/alphasolutionsrepo/interakt) · [官网](https://interakt.app) · 组织维护

**自托管网站搜索与 AI 聊天平台，基于自有数据回答**

面向网站所有者的开源自托管平台：接入自有数据构建搜索索引，通过管理后台配置搜索与聊天体验，以脚本片段形式将搜索框和聊天窗口嵌入任意网站。搜索支持关键词、语义与混合模式（RRF 融合，基于 Elasticsearch 9 或 Azure AI Search）；聊天答案以工具调用方式基于索引生成，支持流式输出、可选引用、guardrails 与版本化提示词模板。模型可接 OpenAI、OpenAI 兼容端点或 Ollama 本地推理。部署形态为单 Docker 镜像 + Postgres(pgvector) + 搜索引擎，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关键词/向量结果经 RRF 融合的混合搜索，支持 facets、同义词、自动补全
- 确定性管线（plan→retrieve→synthesize）或 agentic 循环，按体验选择
- 每个索引自带 search/lookup/inspect/enumerate 工具，可接 MCP 服务器
- Preact + Shadow DOM 的可嵌入搜索与聊天挂件，无需框架

## 适用场景

- 给电商或内容网站加一个基于自有数据的搜索框和 AI 聊天助手
- 完全本地化部署（Ollama + 自托管）的站内问答
- 通过 API 或 Medusa/Storyblok 集成把 AI 搜索接入现有系统

## 场景标签

`语义搜索` `聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L10: **Open-source, self-hosted search and AI chat for your website, grounded in your own data.**
> L21: - **Chat that knows your data.** Answers are grounded in your indexes through tools, streamed, with optional citati
> L33:  💬 Grounded chat A deterministic pipeline (plan → retrieve → synthesize) or an agentic loop, chosen per experience.

## 星数曲线

```mermaid
xychart-beta
    title "alphasolutionsrepo/interakt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7b0c649b1806` · [字段定义](../../DATASET.md)*
