# lightfeed/scrapedown

⭐ 15 · TypeScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/lightfeed/scrapedown) · 组织维护

**带 CSS/XPath 标注的 HTML 转 Markdown 转换库，用于生成爬虫代码**

TypeScript/npm 库，将 HTML 转为 Markdown 并为标题、段落、链接、图片等元素附带 CSS 选择器与 XPath 标注（inline 注释或 footnote 两种模式）。设计用途：让 LLM 读取标注后的 Markdown，一次性生成无需 LLM 参与运行的可复用爬虫代码，以减少逐页 token 消耗。选择器按稳定性排序生成，自动过滤动态 ID、CSS-in-JS 哈希等易碎模式。提供 API、可复用实例、CLI（npx 可用）及导出的选择器工具函数。

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

- HTML→Markdown 并为元素附带 CSS 选择器/XPath 标注（inline/footnote 两种模式）
- 选择器按稳定性优先级生成，自动过滤动态 ID、UUID、框架生成属性等易碎模式
- 基于 Turndown，暴露 TurndownService 实例支持自定义规则与插件
- 提供 CLI（npx 免安装）与 computeCSSSelector/computeXPath 导出工具

## 适用场景

- 让 LLM 一次性生成可独立运行的选择器/XPath 爬虫代码
- 为 LLM 准备保留 DOM 定位信息的 Markdown 文档
- 批量抓取长或重复页面时减少每页的 LLM token 消耗

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: HTML to Markdown with CSS selector and XPath annotations — built for LLM-powered web scraping.
> L15: **Scrapedown** does exactly this: it converts HTML to Markdown and annotates each element with its CSS selector and
> L19: With scrapedown: HTML → Annotated Markdown → LLM generates scraper (once)

## 星数曲线

```mermaid
xychart-beta
    title "lightfeed/scrapedown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `634cc94c3586` · [字段定义](../../DATASET.md)*
