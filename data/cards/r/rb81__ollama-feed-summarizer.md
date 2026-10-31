# rb81/ollama-feed-summarizer

⭐ 16 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/rb81/ollama-feed-summarizer) · 个人维护

**给阅读者：用本地/任意 LLM 生成 RSS 订阅源文章摘要**

Python CLI 工具，读取 feeds.txt 中的 RSS 订阅源，并发抓取并提取全文（RSS 只有摘要片段时从网页 article/main 标签抽取），调用 OpenAI 兼容 API（如本地 Ollama、OpenRouter、OpenAI）生成摘要，输出 Markdown/JSON 文件。用 SQLite 按去重跟踪已处理文章，支持中断续跑、可配置并发、指数退避重试与连续失败阈值后移除订阅源。给希望低成本、私有化汇总每日新闻的用户使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意 OpenAI 兼容 LLM 提供方（Ollama/OpenRouter/OpenAI 等）
- RSS 片段不足时抓取网页全文并从 article/main 标签提取正文
- SQLite 去重与进度续跑，文章按 URL 跟踪不重复总结
- 可配置并发、指数退避重试、连续失败 N 次才移除订阅源

## 适用场景

- 每天自动汇总我的 RSS 订阅新闻并生成可读的 Markdown 摘要
- 用本地 Ollama 私有化运行摘要生成，不依赖云 API
- 增量跟踪多个订阅源，只处理新增文章

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: A fast, modern RSS feed summarizer that works with **any OpenAI-compatible LLM provider** — Ollama, OpenRouter, Open
> L93: 5. **Summarizes** new articles using your configured LLM with a prompt optimized for insightful, multi-sentence ana

## 星数曲线

```mermaid
xychart-beta
    title "rb81/ollama-feed-summarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d6969ed3b8eb` · [字段定义](../../DATASET.md)*
