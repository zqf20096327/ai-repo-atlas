# zebbern/repolens

⭐ 19 · TypeScript · MIT · 推送 2026-08-27 · [GitHub](https://github.com/zebbern/repolens) · [官网](https://mgithub.com) · 个人维护

**网页应用：在浏览器中用 AI 分析 GitHub 仓库并生成文档**

面向开发者/团队的 GitHub 仓库分析 Web 应用：在任意 github.com URL 前加 m 即可分析，功能含项目概览与技术栈检测、语法高亮代码浏览、安全问题扫描、Mermaid 架构图、6 种预设 AI 文档生成、针对代码库的 AI 对话（15 个工具）、PR 浏览、代码漫游、仓库对比与 git 贡献洞察。支持 OpenAI/Google/Anthropic/OpenRouter 四家 API，密钥在应用内配置并存储于浏览器；用 Next.js 16 + Vercel AI SDK 构建，源码方式运行（Node.js 22.12+、pnpm）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- m 前缀 URL 快捷分析任意公开 GitHub 仓库
- AI 文档生成（6 种预设）与代码库 AI 对话（15 个工具）
- 自动安全/质量问题扫描与 Mermaid 架构图生成
- 支持 OpenAI/Google/Anthropic/OpenRouter 四家 AI 提供商

## 适用场景

- 接手陌生仓库时快速生成架构与上手文档
- 扫描代码中的安全隐患与性能问题
- 对比候选依赖库，评估替代方案相似度

## 场景标签

`代码审查` `代码生成` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L23: - **Documentation Generator** — AI-powered docs generation with 6 presets, including Architecture, Setup, API Refer
> L24: - **AI Chat** — Ask questions about a selected codebase with 15 progressively available analysis and skill tools
> L111: |Chat with AI|Open the **Chat** tab and ask questions about the codebase|

## 星数曲线

```mermaid
xychart-beta
    title "zebbern/repolens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `199a323cae48` · [字段定义](../../DATASET.md)*
