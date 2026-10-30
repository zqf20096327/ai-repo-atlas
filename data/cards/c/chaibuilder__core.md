# chaibuilder/core

⭐ 487 · TypeScript · BSD-3-Clause · 推送 2026-10-13 · [GitHub](https://github.com/chaibuilder/core) · [官网](https://chaibuilder.com) · 组织维护

**面向 Next.js 的开源可视化建站器，含 AI 辅助编辑**

基于块编辑器的 Next.js 可视化网站构建工具：提供拖拽画布（Tailwind 样式、媒体、SEO）、自定义 React 块注册、服务端数据提供者、RSC 渲染与 App Router 支持。AI 功能（AI assist、ask-ai 编辑）构建在 Vercel AI SDK 之上，模型请求经可插拔 provider 路由，内置 OpenRouter、OpenAI 兼容端点、Cloudflare Workers AI 适配器，未配置时走 Vercel AI Gateway。要求 Next.js ≥ 15.3、React ≥ 19、Tailwind CSS 4，支持 npm 包或 git subtree 两种接入方式，数据库适配 LibSQL/D1/better-sqlite3，附带 schema（非迁移）由宿主应用管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 块编辑器画布：Tailwind 样式、媒体、SEO 与 AI assist
- AI provider 可插拔：OpenRouter/OpenAI 兼容端点/Cloudflare Workers AI 插件，默认 Vercel AI Gateway
- 非可执行的安全数据绑定管道（currency/trim/gt 等内置 pipe，输出转义）
- 自定义 React 块注册与 RSC 渲染（RenderChaiBlocks/ChaiPageCSS/JSON-LD）

## 适用场景

- 在 Next.js 项目中搭建可视化页面编辑器供内容团队使用
- 注册自有 React 业务块并配置服务端数据提供者
- 通过 OpenAI 兼容端点接入本地 Ollama/vLLM 作为建站 AI 后端

## 场景标签

 · 领域:Web 开发/低代码建站

## 证据(README 行号)

> L3: **AI-enabled visual website builder for Next.js.**
> L21: |Visual editor|Drag-and-drop canvas with Tailwind styling, media, SEO, and AI assist|
> L223: ChaiBuilder's AI features run on the Vercel AI SDK. Model ids use the

## 星数曲线

```mermaid
xychart-beta
    title "chaibuilder/core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 485 --> 488
    line [486, 487, 487]
```

2026-10-18 486 → 2026-10-30 487（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c99b279f0092` · [字段定义](../../DATASET.md)*
