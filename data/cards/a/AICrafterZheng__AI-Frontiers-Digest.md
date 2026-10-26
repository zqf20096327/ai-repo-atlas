# AICrafterZheng/AI-Frontiers-Digest

⭐ 43 · Python · MIT · 推送 2026-04-28 · [GitHub](https://github.com/AICrafterZheng/AI-Frontiers-Digest) · [官网](https://aicrafter.io) · 个人维护

**用 LLM 汇总 AI 资讯并生成播客的自动化新闻摘要系统**

由 Prefect 工作流驱动的 AI 资讯聚合与摘要项目：从 Hacker News 与 TechCrunch AI 抓取文章，经关键词过滤后用 LLM（Azure gpt-4o、Mistral-large，经 OpenRouter 接入 claude-3.5-sonnet、mistral-7b）生成文章与讨论区摘要，通过邮件、Discord 和 Web 应用（Vite+React+TypeScript）分发；并借助 NotebookLM 流程（gpt-4o 生成转录、Azure TTS 生成音频）产出音频与播客。数据与音频存储用 Supabase，后端 API 跑在 Cloudflare Page Functions 上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Hacker News 与 TechCrunch AI 按关键词过滤抓取文章
- LLM 汇总文章及 Hacker News 讨论内容
- 基于 gpt-4o 转录 + Azure TTS 的播客与音频生成
- 邮件、Discord、Web 应用三渠道分发摘要

## 适用场景

- 自动跟踪每日 AI 领域新闻动态
- 将文章转成音频或播客形式收听
- 为社区或订阅者定期推送 AI 资讯摘要

## 场景标签

`AI 写作` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: **AI Frontiers Digest** leverages Large Language Models (LLMs) to intelligently summarize and curate the latest deve
> L35: - LLMs

## 星数曲线

```mermaid
xychart-beta
    title "AICrafterZheng/AI-Frontiers-Digest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `701129645bd3` · [字段定义](../../DATASET.md)*
