# jakobhoeg/browser-ai

⭐ 204 · TypeScript · NOASSERTION · 推送 2026-10-14 · [GitHub](https://github.com/jakobhoeg/browser-ai) · [官网](https://browser-ai.dev) · 个人维护

**为 Vercel AI SDK 提供浏览器内 AI 模型接入的 TypeScript 库**

TypeScript 库集合，把浏览器端 AI 模型来源封装为 Vercel AI SDK 的 model provider：包括 Chrome/Edge 内置 AI（Prompt API）、WebLLM 与 Transformers.js，并提供向服务端模型的无缝回退机制。面向使用 Vercel AI SDK 构建客户端 AI 应用的 Web 开发者，以 npm 包（core/transformers-js/web-llm）分发，配套官方文档站、Chrome/Hugging Face 教程与 Next.js 示例应用。由个人开发者维护，属 Vercel OSS Program。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种浏览器内模型来源：Chrome/Edge 内置 AI、WebLLM、Transformers.js
- 兼容 AI SDK v5/v6/v7 多版本的三个 npm 包
- 浏览器端模型不可用时无缝回退到服务端模型

## 适用场景

- 在 Next.js 应用中直接调用浏览器内置或本地推理模型
- 客户端 AI 功能在离线或低延迟场景下运行
- 构建浏览器优先、服务端兜底的混合推理应用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: TypeScript libraries that provide access to in-browser AI model providers with seamless fallback to using server-si
> L79: If you've ever built apps with local language models, you're likely familiar with the challenges: creating custom h

## 星数曲线

```mermaid
xychart-beta
    title "jakobhoeg/browser-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-24 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ef3d7d280887` · [字段定义](../../DATASET.md)*
