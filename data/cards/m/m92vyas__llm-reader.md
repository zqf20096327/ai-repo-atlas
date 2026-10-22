# m92vyas/llm-reader

⭐ 314 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/m92vyas/llm-reader) · 个人维护

**将网页/URL 转为 LLM 友好输入文本的 Python 库**

预处理网页 HTML 并生成适合输入 LLM 的文本，用于提升链接、图片地址、表格等结构化信息的抽取/抓取准确率，典型场景如电商网站抓取。基于 Playwright 获取页面源码（从 Selenium 迁移以支持并发抓取），可替换为自有代理或付费 API 获取源码。自称为 Firecrawl 与 Jina Reader API 的开源替代，提供 URL 转 Markdown、HTML 转 Markdown 的免费工具及 wiki 文档。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页 URL/HTML 转 LLM 友好文本，含链接、图片地址与表格保留
- 基于 Playwright 的异步/并发抓取支持
- get_page_source 可替换为自有代理或付费 API 以规避封锁
- 附带免费书签工具：URL/HTML 转 Markdown

## 适用场景

- 我要让 LLM 从网页中抽取商品名、链接、图片和价格
- 做 RAG 或 AI 网页抓取前先把网页转成干净的输入文本
- 已有 HTML 源码，想低成本转成 Markdown 给 LLM 用

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Pre-processing webpage before giving it as input to the LLM improves extraction/scraping accuracy especially if you 
> L5: Use this library to turn any webpage/url to LLM friendly text. Fully open source alternative to firecrawl and jina r

## 星数曲线

```mermaid
xychart-beta
    title "m92vyas/llm-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 312 --> 314
    line [313, 313]
```

2026-10-18 313 → 2026-10-22 313（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `466c7c96de2a` · [字段定义](../../DATASET.md)*
