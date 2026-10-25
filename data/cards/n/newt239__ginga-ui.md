# newt239/ginga-ui

⭐ 39 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/newt239/ginga-ui) · [官网](https://ginga-ui.vercel.app) · 个人维护

**React UI 组件库：以 LLM 依据网站内容或提示生成组件样式主题**

基于 React 的 UI 组件库，收录 19 种组件（Button、Dialog、Tab 等），组件 CSS 在导入时自动加载。其 AI 部分为主题生成：通过 Vercel AI SDK 的 ThemeClient 类，依据网站内容或用户提示生成主题，产出以 CSS 变量交付（颜色、边框、圆角、字体等），可混入自定义 CSS。支持 OpenAI/Google/Anthropic 三个云端 provider 及浏览器内置 Gemini Nano（免 API key、无网络请求）。推荐 React 18+、Next.js 13+ 环境，主题生成支持 SSR 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 种 React 组件，导入即自动加载 CSS
- ThemeClient 基于 Vercel AI SDK 按网站内容或提示生成主题
- 主题以 CSS 变量交付，可扩展自定义样式
- provider "browser" 使用 Chrome/Edge 内置 Gemini Nano，免 API key

## 适用场景

- 在 React/Next.js 项目中按品牌内容生成配套主题
- 通过提示词快速迭代配色与圆角等设计变量
- 无需 API key 在浏览器端离线生成主题

## 场景标签

 · 领域:前端/UI 组件

## 证据(README 行号)

> L8: **Ginga UI** is an UI component library for React. This libarary is using LLM to styling components. Components will
> L55: You can generate with your own theme by using `ThemeClient` class powered by Vercel AI SDK.

## 星数曲线

```mermaid
xychart-beta
    title "newt239/ginga-ui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-25 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `63277e96ee72` · [字段定义](../../DATASET.md)*
