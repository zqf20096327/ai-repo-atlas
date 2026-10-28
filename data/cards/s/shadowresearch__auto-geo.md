# shadowresearch/auto-geo

⭐ 28 · TypeScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/shadowresearch/auto-geo) · [官网](https://shadowresearch.github.io/auto-geo/) · 组织维护

**开源 GEO 引擎：让品牌被 ChatGPT/Claude/Gemini 等 AI 搜索引用**

面向希望提升 AI 搜索引擎引用率的品牌与营销团队的文件式 CLI 工具，MIT 协议。闭环流程：doctor 按七块 GEO 架构审计任意 URL 的引用就绪度并给出分数；write/fix 调用 LLM（默认 gpt-5.4 或 claude-sonnet-4-6，经 Vercel AI SDK generateObject 约束输出到 schema）生成或重写页面；check 向 Perplexity/OpenAI/Anthropic/Gemini/xAI 实测域名是否被引用；history 输出趋势。全部数据存本地文件，无服务器、无账号、无数据库，需自备各引擎 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- doctor 审计页面引用就绪度，退出码可用于 CI 门禁（≥75% 通过）
- write/fix 通过 LLM 生成符合 GEO schema 的结构化页面 JSON，含成本估算与 dry-run
- check 实测 5 家 AI 引擎（Perplexity/OpenAI/Anthropic/Gemini/xAI）的真实引用情况
- 全文件式、可提交版本库，无服务器/账号/数据库

## 适用场景

- 审计我的页面在 AI 搜索回答中被引用的就绪度
- 为目标查询批量生成符合 GEO 架构的发布页
- 持续跟踪域名在 ChatGPT/Perplexity 等引擎中的引用覆盖率变化

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L13: **The open-source GEO engine that gets your brand mentioned in ChatGPT, Claude, Gemini, Perplexity, and Grok.**
> L15: Audit, generate, fix, and track the pages large language models cite — one CLI, file-based, MIT.
> L144: The system prompt encodes the GEO SOP — TL;DR length, answer-capsule windows, banned superlatives, FAQ structure —
> L212: Engines: **perplexity** (default), **openai**, **anthropic**, **gemini**, **xai** (alias `grok`), or **`--engine a

## 星数曲线

```mermaid
xychart-beta
    title "shadowresearch/auto-geo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ab01d98065ab` · [字段定义](../../DATASET.md)*
