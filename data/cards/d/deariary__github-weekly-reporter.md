# deariary/github-weekly-reporter

⭐ 28 · TypeScript · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/deariary/github-weekly-reporter) · [官网](https://deariary.github.io/github-weekly-reporter/) · 个人维护

**把 GitHub 活动自动生成 AI 摘要周报页面的 Action**

以 GitHub Action 形式运行的 TypeScript 工具：每周汇总用户的 commits、PR、code review 等活动数据，调用 LLM 生成叙事性摘要，渲染为自包含 HTML 报告并部署到 GitHub Pages，附每周归档。通过 npx 交互式 setup 完成建仓、工作流、secrets 与 Pages 配置。支持 OpenRouter/Groq/Gemini/OpenAI/Anthropic/Grok 六家 LLM 提供商，其中三家有免费额度；公开仓库全链路零成本。提供 4 套主题、10 种界面语言与可嵌入 Profile 的新闻滚动卡片。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每周汇总 commits/PR/review 并生成 AI 叙事摘要
- npx 交互式 setup 自动建仓、配置工作流与 Pages
- 支持 6 家 LLM 提供商，其中 3 家有免费额度
- 4 套主题、10 种语言、自包含 HTML 报告

## 适用场景

- 自动生成并发布我的 GitHub 每周活动周报
- 在 Profile README 里展示 AI 生成的动态新闻卡片
- 以零成本在公开仓库跑通整个周报流水线

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: Every week, this tool looks at everything you did on GitHub (commits, pull requests, code reviews) and generates a 
> L122: - AI-generated narrative summary

## 星数曲线

```mermaid
xychart-beta
    title "deariary/github-weekly-reporter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `eb835174449d` · [字段定义](../../DATASET.md)*
