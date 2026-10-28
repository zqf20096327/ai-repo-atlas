# nidhi-singh02/mark-it-down

⭐ 23 · TypeScript · MIT · 推送 2026-03-01 · [GitHub](https://github.com/nidhi-singh02/mark-it-down) · [官网](https://www.npmjs.com/package/web-to-markdown) · 个人维护

**把任意网页转换为干净 Markdown 的 CLI/库，面向开发者与 LLM 流水线**

网页转 Markdown 工具：按顺序尝试三种提取策略（原始 .md 端点、Next.js/Mintlify 的 MDX 载荷提取、Readability+Turndown 通用回退），自动剥离导航等模板内容，输出支持 GFM 的 Markdown；对 GitBook 等站点有专门处理，支持 Playwright 无头浏览器渲染 SPA 页面（可选依赖）。以 npm 包与 npx 免安装方式提供，亦有程序化 API。内置 SSRF 防护、危险协议过滤、内容大小限制与沙箱化 MDX 执行等安全机制。需 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级提取策略：原始 .md 端点→MDX 载荷→Readability+Turndown 回退
- SPA 页面可选 Playwright 无头 Chromium 渲染
- GFM 支持（表格、任务列表、删除线、代码块）与代码块语言检测
- SSRF 防护、危险协议过滤、沙箱化 MDX 执行等安全机制

## 适用场景

- 为 LLM/RAG 流水线准备干净的网页语料
- 把文档站、博客、新闻文章批量转为 Markdown 归档
- 抓取 JS 渲染的 SPA 页面内容并转为可读文本

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Convert any web page to clean Markdown. Built for developers and LLM pipelines.
> L5: Handles documentation sites (Mintlify, GitBook, Docusaurus, Next.js docs), blogs, news articles, and more. Automatic

## 星数曲线

```mermaid
xychart-beta
    title "nidhi-singh02/mark-it-down 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `27fd10ca1a3b` · [字段定义](../../DATASET.md)*
