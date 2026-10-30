# crafter-station/lupa

⭐ 22 · TypeScript · GPL-3.0 · 推送 2025-11-17 · [GitHub](https://github.com/crafter-station/lupa) · [官网](https://www.lupa.build) · 组织维护

**面向 AI Agent 的知识库 API：RAG 检索基础设施**

自托管的 RAG 基础设施应用：将 PDF/Office/CSV/HTML 等文档与网页抓取内容（Firecrawl）解析为 markdown 分块，经 OpenAI text-embedding-3-small 生成嵌入并部署到 Upstash Vector 向量索引，向 Agent 提供 Search API 与带 RAG 的 Chat API。支持快照版本回滚、定时刷新、零停机部署与 Tinybird 分析流水线，可接入 Vercel AI SDK 与 LangChain。需 Bun/Node 20+、PostgreSQL（推荐 Neon）、Clerk 与 Trigger.dev 账号，部署依赖较多外部托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Search API 与带 RAG 的 Chat API，语义向量检索供 LLM 上下文增强
- 多格式解析（PDF/Word/Excel/PPT/CSV/HTML/TXT）与 Firecrawl 网页抓取
- 快照版本系统支持回滚与零停机部署，网站文档可定时刷新
- Tinybird 分析流水线：请求量、延迟、零结果查询等指标

## 适用场景

- 为 AI Agent 提供可检索的私有知识库 API
- 把公司文档和网站内容转化为向量索引供 LLM 引用
- 按项目/环境管理多个知识库部署并跟踪检索效果

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: Lupa is a production-ready RAG (Retrieval-Augmented Generation) infrastructure that gives AI agents instant access t
> L17: - **AI Framework Ready**: Drop-in integration with Vercel AI SDK, LangChain, and more

## 星数曲线

```mermaid
xychart-beta
    title "crafter-station/lupa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7cee8b9456a2` · [字段定义](../../DATASET.md)*
