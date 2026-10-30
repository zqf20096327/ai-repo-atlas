# docsector/docsector-reader

⭐ 21 · JavaScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/docsector/docsector-reader) · [官网](https://docsector.com) · 组织维护

**面向 AI 的文档渲染引擎：Markdown 文档站 + LLM/Agent 友好层**

基于 Vue 3、Quasar v2 与 Vite 构建的文档渲染引擎，将 Markdown 转为多语言、带语法高亮、明暗主题与锚点导航的文档站。AI 部分覆盖：面向 LLM 爬虫自动返回纯 Markdown、llms.txt / llms-full.txt 生成、MCP Server 与 WebMCP 浏览器工具、Agent Skills 发现索引、基于 Cloudflare AI Search 的可选文档助手面板，以及 Open in ChatGPT/Claude 链接。构建期编译页面、按需加载内容，以 npm 包形式发布。

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

- 对已知 AI 爬虫（GPTBot、ClaudeBot 等 24 个）自动提供纯 Markdown，robots.txt 显式放行
- 自动生成 /mcp MCP Server、llms.txt、agent-skills 索引与 WebMCP 浏览器工具
- 可选文档助手面板（Cloudflare AI Search 后端）
- Markdown 渲染、i18n、KaTeX/Mermaid、构建期 SSG 与懒水合

## 适用场景

- 把 Markdown 项目文档发布为可导航的多语言文档站
- 让文档站对 LLM 爬虫与 AI 助手友好可发现、可问答
- 为 Claude Desktop/VS Code 等提供文档 MCP 接入

## 场景标签

 · 领域:开发者文档/Web 工程

## 证据(README 行号)

> L5:  A documentation rendering engine built with Vue 3, Quasar v2 and Vite with AI features.
> L32: - 🤖 **AI Assistant Panel** — Optional documentation assistant drawer backed by Cloudflare AI Search through an inte

## 星数曲线

```mermaid
xychart-beta
    title "docsector/docsector-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ccd17abff074` · [字段定义](../../DATASET.md)*
