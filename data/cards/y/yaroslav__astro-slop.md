# yaroslav/astro-slop

⭐ 15 · TypeScript · MIT · 推送 2026-05-11 · [GitHub](https://github.com/yaroslav/astro-slop) · [官网](https://yaroslav.io/opensource/astro-slop) · 个人维护

**Astro 站点的 LLM 友好内容导出集成：生成 .md 页面与 llms.txt**

面向 Astro 开发者的站点集成：通过 md 标签模板让用户为每个页面编写 .md.ts 端点，生成 Markdown 版本页面；自动汇总 /llms.txt 与 /llms-full.txt 索引，向 HTML 页面注入 link rel=alternate，并在 dev/SSR 下实现 RFC 9110 的 HTTP 内容协商（Accept 偏好 markdown 时重定向到 .md）。对无 markdown 源的页面提供 fromHtml（基于 Defuddle 的正文提取与 HTML→MD 转换），cleanMdx 用于剥离 MDX 语法。采用自底向上方式，不自动生成内容，需用户逐页编写端点；纯静态预渲染下 fromHtml 的往返对代码块有损。npm/bun/pnpm 安装，共六个导出。

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

- md 标签模板编写 .md.ts 端点，支持 per-entry/列表/组合页三种模式
- 自动生成 /llms.txt 与 /llms-full.txt，可用 defaultLlmsTxt 自定义结构
- RFC 9110 内容协商：Accept 偏好 text/markdown 时重定向到 .md 兄弟页
- fromHtml 基于 Defuddle 做正文提取与 HTML→Markdown 转换，cleanMdx 剥离 MDX 语法

## 适用场景

- 为 Astro 博客/文档站生成供 LLM 摄取的 llms.txt
- 让爬虫或 curl 脚本通过内容协商自动获取 Markdown 版页面
- 为 MDX 内容集合导出干净的 Markdown 视图

## 场景标签

 · 领域:Web 开发/静态站点工具

## 证据(README 行号)

> L5: Content slop for LLMs to slurp. The most complete and flexible Astro integration for LLMs and generating markdown ve
> L34: - **`/llms.txt`** auto-assembled from your `.md` routes per the llmstxt.org spec. H1 site name, blockquote summary,

## 星数曲线

```mermaid
xychart-beta
    title "yaroslav/astro-slop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `41b2226147af` · [字段定义](../../DATASET.md)*
