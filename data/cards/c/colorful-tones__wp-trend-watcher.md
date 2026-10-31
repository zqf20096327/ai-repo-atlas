# colorful-tones/wp-trend-watcher

⭐ 15 · HTML · MIT · 推送 2026-10-26 · [GitHub](https://github.com/colorful-tones/wp-trend-watcher) · [官网](https://colorful-tones.github.io/wp-trend-watcher/) · 组织维护

**为 WordPress 开发者生成 AI 辅助、人工审阅的周报工作流**

基于 Node.js/pnpm 的开源工作流：从 6 个 RSS 源（4 个一级 + 2 个二级）抓取 WordPress 生态文章，调用本地 LLM（LM Studio、Ollama 或任意 OpenAI 兼容端点）生成摘要并合成周报，再经本地审阅服务器（127.0.0.1:3001）人工复核后产出 Markdown/HTML 报告，部署到 GitHub Pages 并提供 RSS 订阅。面向自由职业与代理商 WordPress 开发者。收集、诊断与审阅步骤无需 LLM，仅摘要步骤需要；需 Unix 环境（macOS/Linux/WSL2）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pnpm weekly 单命令串联 doctor/collect/summarize/review 全流程
- 本地 LLM 摘要（LM Studio/Ollama/OpenAI 兼容端点），Provider 无关
- 本地审阅服务器支持人工批注后自动生成 SEO 描述并重建 HTML
- 报告含 RSS feed、分页存档与多主题（Light/Dark/System）呈现

## 适用场景

- 每周自动汇总 WordPress 生态动态并人工审阅后发布
- 不逐篇阅读 Make 博客与开发者博客也能跟进生态变化
- 通过 RSS 订阅历史与最新周报存档

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: WP Trend Watcher is a lightweight, open-source workflow for helping WordPress developers stay informed about changes
> L25: - **A local LLM provider** for summarization: LM Studio, Ollama, or any OpenAI-compatible endpoint. Collection, doc
> L42: pnpm collect         # Fetch RSS feeds from 6 sources (4 Tier 1 + 2 Tier 2), store articles as JSON
> L43: pnpm summarize       # Fetch article content, generate summaries, synthesize the weekly report, and build HTML + in

## 星数曲线

```mermaid
xychart-beta
    title "colorful-tones/wp-trend-watcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a8a9404b89b4` · [字段定义](../../DATASET.md)*
