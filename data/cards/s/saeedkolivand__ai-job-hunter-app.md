# saeedkolivand/ai-job-hunter-app

⭐ 62 · Rust · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/saeedkolivand/ai-job-hunter-app) · [官网](https://aijobhunter.app) · 个人维护

**求职者用的本地优先 AI 桌面助手：抓取职位、匹配简历、生成简历与求职信**

基于 Tauri（Rust 核心 + React 渲染）的桌面应用，面向求职者：抓取 24 个职位板（含 Adzuna/JSearch 聚合、Greenhouse/Lever 等 ATS 板），将职位与用户简历做语义匹配与打分，生成定制简历（12 套模板，7 套 ATS-Safe + 5 套 Design，DOCX/PDF/TXT 导出）与求职信，起草基于简历的申请问题回答，并提供 Autopilot 定时工作流与申请跟踪。AI 提供方灵活：Ollama 完全离线运行，或自带 OpenAI/Anthropic/Gemini key，或经 CLI agent（Claude Code、Codex、Gemini CLI）。生成采用 Rust 端强制执行的溯源管线（证据映射、确定性校验、伪造审查门）。数据存本地 SQLite，凭据存 OS 钥匙串，无应用运营的后端。另有 Chrome/Firefox 浏览器扩展一键保存职位。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抓取 24 个职位板并做向量相似度 + LLM 重排的简历匹配与打分
- 12 套简历模板流式生成，支持 DOCX/PDF/TXT 导出与 11 种语言
- 多 AI 提供方：Ollama 离线、OpenAI/Anthropic/Gemini key、任意 OpenAI 兼容服务、CLI agent
- Rust 端确定性校验与伪造审查门：无来源声明阻止导出

## 适用场景

- 我想离线用本地模型批量生成针对不同职位的定制简历和求职信
- 我想自动抓取职位板、按简历匹配度排序并跟踪投递状态
- 我想在浏览招聘网站时用浏览器扩展一键保存职位并做公司调研

## 场景标签

`网页抓取` `工作流自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L5:  Your local-first, AI-native desktop assistant for intelligent job searching, résumé &amp; cover-letter generation, 
> L70: AI Job Hunter is a desktop application built with **[Tauri][tauri]** (a [Rust][rust] core with a [React][react] ren
> L96: - **One-click tailoring**: from any found job, click **Tailor** to seed the AI Generate workspace, open the posting

## 星数曲线

```mermaid
xychart-beta
    title "saeedkolivand/ai-job-hunter-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-25 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c719784113be` · [字段定义](../../DATASET.md)*
