# kyh/ai-canvas

⭐ 39 · TypeScript · 推送 2026-10-16 · [GitHub](https://github.com/kyh/ai-canvas) · [官网](https://canvas.kyh.io) · 个人维护

**可 Fork 的 Next.js AI 设计画布模板：自然语言生成编辑画布内容**

基于 Next.js 16 + React 19 + Konva 的可 Fork 设计画布模板，提供无限画布编辑器（缩放、多选、图层、文本/框架/图片块、样式系统）。AI 部分：单个 eve agent 携五个工具，可生成文本、框架、AI 图片（gpt-image-1）与交互式 HTML 块；每次请求附带画布 PNG 快照与 JSON 上下文。开发模式用 AI_GATEWAY_API_KEY，生产环境访客自带 Vercel AI Gateway key（存浏览器，按会话使用）。模型为 openai/gpt-5.1-instant，经 Vercel AI Gateway 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 agent 五工具：生成文本/框架/AI 图片/交互式 HTML 块
- 视觉上下文感知：每次请求携带画布 PNG 快照与 JSON 上下文
- BYO-key 机制：访客自带 Vercel AI Gateway key，按会话运行
- eve agent 运行时 + Vercel AI SDK (ai@7) 架构

## 适用场景

- Fork 后自建 Canva/Figma/tldraw 类设计工具
- 搭建白板、图表编辑器或演示文稿应用的原型
- 学习 eve agent 运行时与画布类应用的 AI 集成方式

## 场景标签

 · 领域:开发模板/设计工具

## 证据(README 行号)

> L7: Forkable Next.js template featuring an AI design canvas — generate, edit, and compose on an infinite canvas in natur
> L25: - One agent, five tools: generate text, frames, and AI images (gpt-image-1), or build/update live interactive HTML 

## 星数曲线

```mermaid
xychart-beta
    title "kyh/ai-canvas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-31 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fb8c3e0d46fb` · [字段定义](../../DATASET.md)*
