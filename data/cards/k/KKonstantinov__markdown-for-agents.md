# KKonstantinov/markdown-for-agents

⭐ 34 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/KKonstantinov/markdown-for-agents) · [官网](http://markdown-for-agents.vercel.app) · 个人维护

**面向 AI agent 的 HTML 转 Markdown 转换库，降低 token 消耗**

运行时无关的 HTML 转 Markdown 转换器，面向为 AI agent 提供网页内容的场景：内置内容提取以剥离导航、广告、页脚等非正文元素，提供启发式 token 估算（可换用自定义分词器如 tiktoken）、内容去重选项与自定义转换规则插件系统。提供 TypeScript 与纯 Python（零依赖）两个版本，并以中间件包形式支持 Express/Fastify/Hono/Next.js/SvelteKit 等，通过 Accept: text/markdown 内容协商自动返回 Markdown，附带 HTTP 缓存头支持。受 Cloudflare 的 Markdown for Agents 启发。

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

- 内置内容提取，自动剥离 nav/ads/sidebars/cookie banners 等非正文元素
- 内容协商中间件：客户端发送 Accept: text/markdown 时自动返回 Markdown
- 启发式 token 估算，可替换为 tiktoken 等精确分词器
- TypeScript 与零依赖 Python 双实现，单依赖 htmlparser2

## 适用场景

- 让 AI agent 以低 token 成本读取网页正文内容
- 在现有 Web 框架中为 agent 请求自动提供 Markdown 版本
- 审计某 URL 转为 Markdown 后的 token/字节节省情况

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: Runtime-agnostic HTML to Markdown converter built for AI agents. One dependency, works everywhere.
> L9: Convert any HTML page into clean, token-efficient Markdown — with built-in content extraction to strip away navigati
> L34: - **Framework middleware** — drop-in support for Express, Fastify, Hono, Next.js, SvelteKit, and any Web Standard s

## 星数曲线

```mermaid
xychart-beta
    title "KKonstantinov/markdown-for-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f6936cf8c85f` · [字段定义](../../DATASET.md)*
