# RojanSapkota/BrowserMind

⭐ 26 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/RojanSapkota/BrowserMind) · 个人维护

**用自然语言驱动浏览器自动完成任务的 AI agent 工具**

基于 browser-use 构建的浏览器自动化 agent：用户输入任务描述（如填写求职申请、抓取数据），由所选 LLM 驱动浏览器自动浏览并完成任务。支持 Anthropic、OpenAI、Groq、Google 及本地 Ollama 等多种模型，内置无头浏览、错误回退与速度优化。安装方式为克隆仓库后 pip 安装依赖，需配置 API key（本地 Ollama 除外），浏览器依赖 Playwright/Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Anthropic/OpenAI/Groq/Google/Ollama 多模型切换
- 自然语言任务驱动浏览器自动执行（填表、抓取、工作流）
- 基于 browser-use 工具生态，支持无头浏览与错误回退
- 可编程调用（run_agent / initialize_agent）

## 适用场景

- 用一句话让 agent 帮我填求职申请等表单
- 自动抓取网站结构化数据
- 自动执行重复性浏览器操作与研究信息收集

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: **BrowserMind** is a browser automation agent built on top of browser-use. giving you a single interface to run any
> L14: #### Task = "Fill in this job application with my resume and information."

## 星数曲线

```mermaid
xychart-beta
    title "RojanSapkota/BrowserMind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-26 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `96c3c096e861` · [字段定义](../../DATASET.md)*
