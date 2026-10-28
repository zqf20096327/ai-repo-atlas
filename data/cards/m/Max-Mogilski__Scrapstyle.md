# Max-Mogilski/Scrapstyle

⭐ 32 · TypeScript · 推送 2025-12-20 · [GitHub](https://github.com/Max-Mogilski/Scrapstyle) · [官网](https://www.scrapestyle.com/) · 个人维护

**输入网页 URL，生成供 Cursor/Lovable 使用的 AI 风格指南**

基于 Next.js 15 的 Web 工具：用户粘贴公开网站 URL，通过 Puppeteer 抓取页面并借助 Gemini 提取设计 token（颜色、字体、间距、阴影），生成可复制粘贴给 AI 编码工具（Cursor、Lovable）的风格指南。支持 OpenRouter（OpenAI 兼容）作为可选模型通道，API key 保存在浏览器本地。可在线使用，也可 git clone 后 npm 安装本地运行；本地运行需系统装有 Chrome/Edge/Brave/Chromium，Safari 不被 Puppeteer 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从任意公开 URL 提取设计 token（颜色/字体/间距/阴影）
- 使用 Gemini 理解设计模式，支持 OpenRouter（OpenAI 兼容）通道
- API key 仅保存在浏览器本地
- 生成结果可直接复制粘贴给 AI 编码工具

## 适用场景

- 我在 Cursor 或 Lovable 里做前端项目时，想快速复刻某个网站的视觉风格
- 为 AI 编码工具生成结构化的设计 token 参考文档
- 本地部署后用自己的 API key 私下使用

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: Generate AI-ready style guides for Cursor & Lovable in seconds.
> L29: - 🤖 **AI-powered** — Uses Gemini to understand design patterns
> L35: **Online:** Go to scrapestyle.com, get a free Gemini API key, paste a URL!

## 星数曲线

```mermaid
xychart-beta
    title "Max-Mogilski/Scrapstyle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `82709dc2d377` · [字段定义](../../DATASET.md)*
