# PacificStudio/streamdown-svelte

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-04-10 · [GitHub](https://github.com/PacificStudio/streamdown-svelte) · [官网](https://streamdown-svelte.pacificstudio.ai/) · 组织维护

**面向 AI 流式输出的 Svelte Markdown 渲染组件库**

Vercel Streamdown 的 Svelte 移植，以 Svelte 组件形式渲染 AI 生成中的 markdown 流：支持流式/静态双模式、未完成 markdown 修复、流式解析缓存、硬化的链接/图片/原始 HTML 安全处理，内置代码块（Shiki 高亮、复制、下载），并经 plugins 提供数学公式（KaTeX）与 Mermaid 可选插件。面向在 Svelte/SvelteKit 应用中展示 LLM 流式回复的开发者，需搭配 Tailwind v4 时在样式中声明 @source。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式模式下修复未完成的 markdown 并做块级解析缓存
- 原始 HTML/链接/图片的安全层（allowlist、URL 重写、跳过 HTML）
- 数学（KaTeX）与 Mermaid 图表经 plugins 按需启用
- snippet/component/custom marked extension 三层自定义渲染

## 适用场景

- 在 Svelte 聊天界面中逐 token 渲染 AI 回复
- 渲染含代码块、表格、公式的 LLM 输出
- 对 AI 生成的 HTML 内容做标签与链接来源管控

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Svelte port of Vercel Streamdown for rendering AI-generated markdown with streaming-friendly parsing, hardened HTML 
> L92: - Streaming and static rendering modes

## 星数曲线

```mermaid
xychart-beta
    title "PacificStudio/streamdown-svelte 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `fc32a674754f` · [字段定义](../../DATASET.md)*
