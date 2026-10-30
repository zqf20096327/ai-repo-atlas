# akramcodez/osfit

⭐ 18 · TypeScript · MIT · 推送 2026-07-05 · [GitHub](https://github.com/akramcodez/osfit) · [官网](https://osfit.akramcodez.tech) · 个人维护

**分析 GitHub 文件并给出 issue 解决方案的 AI 网页工具**

基于 Next.js 16 的独立 Web 应用：读取 GitHub 文件与 issue，用 AI 生成多语言解释、流程图说明代码，并为 issue 生成逐步解决方案，支持 20+ 种语言。技术栈为 TypeScript、Supabase（含 SQL 数据库 schema）、Tailwind CSS，AI 后端可选 Gemini 或 Groq，抓取 GitHub 内容依赖 Apify 的 multilingual-github-scraper actor，本地化文本用 Lingo。需克隆源码并配置 .env.local 后 npm run dev 运行。

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

- 将 GitHub 文件/issue 转为多语言解释与流程图
- 为 issue 生成逐步解决方案，支持 20+ 语言
- AI 后端可选 Gemini 或 Groq，GitHub 内容抓取经 Apify actor

## 适用场景

- 我想快速理解陌生仓库里的复杂代码文件
- 给 GitHub issue 生成可执行的解决步骤
- 用母语阅读代码解释与 issue 方案

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: AI-powered tool for analyzing GitHub files and solving issues. Supports 20+ languages.
> L22: Minimal setup requires Supabase + one AI key (Gemini or Groq). Add Apify for better file/issue analysis. Add Lingo 

## 星数曲线

```mermaid
xychart-beta
    title "akramcodez/osfit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2bb91024fdb8` · [字段定义](../../DATASET.md)*
