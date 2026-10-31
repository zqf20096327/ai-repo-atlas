# anyin-ai/aperture

⭐ 29 · TypeScript · MIT · 推送 2026-07-21 · [GitHub](https://github.com/anyin-ai/aperture) · 组织维护 · 中文 README

**自托管的品牌 AI 搜索可见度监测与分析工具**

面向品牌方、代理机构与 SEO/AEO 团队的开源 AI 可见度监测基础设施：跟踪品牌在 ChatGPT、Perplexity 等 LLM 搜索引擎中是否被提及/推荐，支持竞品引用对比、跨模型/语言/市场的结构化审计与随时间变化的追踪。采用 BYOK 模式，自带 OpenAI 与 Perplexity API key 接入，兼容任意 OpenAI 兼容端点（Ollama、vLLM 等），可自托管、无按席位收费。安全限制：API key 在本地 SQLite 中明文存储且默认无身份验证，需保持在 localhost/私有网络或置于反向代理之后。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 监测 AI 模型对品牌的推荐与竞品引用情况
- 跨模型、语言、市场的结构化可见度审计与时间追踪
- BYOK：自带 OpenAI/Perplexity key，支持任意 OpenAI 兼容端点（Ollama、vLLM 等）
- 自托管，数据留在本地服务器

## 适用场景

- 跟踪我的品牌在 ChatGPT/Perplexity 回答中是否被推荐
- 查看哪些竞品在 AI 搜索中被引用而我未被提及
- 评估内容优化对 AI 可见度的影响

## 场景标签

 · 领域:AI 搜索可见度分析

## 证据(README 行号)

> L5: Track how your brand appears (or doesn't) across ChatGPT, Perplexity, Google AI Overviews, and other LLM-powered sea
> L15: - **Monitor** — Track whether AI models recommend your brand for the queries that matter
> L17: - **Audit** — Run structured visibility audits across models, languages, and markets

## 星数曲线

```mermaid
xychart-beta
    title "anyin-ai/aperture 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9703e621c6c6` · [字段定义](../../DATASET.md)*
