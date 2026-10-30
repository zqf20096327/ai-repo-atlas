# benjamincanac/nuxt-agent-discovery

⭐ 18 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/benjamincanac/nuxt-agent-discovery) · [官网](https://nuxt-agent-discovery.vercel.app) · 个人维护

**让 Nuxt 站点对 AI agent 可读的发现模块：markdown 协商与发现文档**

面向 Nuxt 文档站点的 Nuxt 模块：按 RFC 9110 做 Accept/User-Agent 内容协商，向已知 AI agent 返回 markdown 版本（.md 孪生 URL、/raw 路由），并生成一组发现文档：/.well-known/api-catalog（RFC 9727）、可选 MCP server card、Agent Skills（/.well-known/skills/）、/sitemap.md 与 robots.txt AI 策略。内容源可插拔，内置 @nuxt/content，另有 nuxt-llms 桥接。支持 Vercel 边缘预渲染协商，零配置即可运行。

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

- RFC 9110 q 值解析的 Accept/User-Agent 内容协商与 .md 孪生 URL
- /.well-known/api-catalog、MCP server card、Agent Skills 等发现文档
- 可插拔内容适配器（内置 @nuxt/content、commark 工厂或自定义）
- nuxt-llms 桥接与 markdown 404 错误体（附恢复链接）

## 适用场景

- 让文档站的页面能被 AI agent 以 markdown 形式抓取
- 为站点生成 llms.txt 相关内容与 api-catalog 等发现文档
- 通过 robots.txt AI 策略声明站点对 agent 的开放范围

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: Markdown content negotiation, CDN-level rewrites, and discovery documents for AI agents on Nuxt documentation sites.
> L18: - `/.well-known/api-catalog` (RFC 9727), an optional MCP server card, and Agent Skills under `/.well-known/skills/`

## 星数曲线

```mermaid
xychart-beta
    title "benjamincanac/nuxt-agent-discovery 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3cd826aa792a` · [字段定义](../../DATASET.md)*
