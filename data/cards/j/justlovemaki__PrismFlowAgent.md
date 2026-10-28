# justlovemaki/PrismFlowAgent

⭐ 97 · JavaScript · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/justlovemaki/PrismFlowAgent) · [官网](https://hex2077.dev/) · 个人维护 · 中文 README

**全栈自动化资讯抓取、AI 总结与多渠道分发系统**

基于 Node.js/Fastify/React 的资讯处理系统：插件化接入 GitHub Trending、RSS、Twitter/Reddit 等多源数据，经 SQLite 存储与调度后，用 Gemini/Claude/GPT 或本地 Ollama 生成结构化总结，一键或自动发布到微信公众号、GitHub 归档或 RSS；另支持浏览器自动化渠道（小红书，需配合 OpenChromeCLI）。提供 DeepSeek Harness 原生插件 @prismflow/dsh，在 DSH 进程内完成同步、筛选、生成、审批与受控发布，关键配置带版本与 SHA-256 CAS 审计。从源码安装运行，默认密码 admin123。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件化多源抓取（GitHub Trending/RSS/社交媒体），支持 24 小时无人值守调度
- 原生支持 Gemini/Claude/GPT/Ollama，Prompt 模板化结构化输出
- 多端发布：微信公众号、GitHub 归档、RSS，媒体自动压缩（AVIF/FFmpeg）
- DeepSeek Harness 原生插件，含草稿审批、发布审计与 SHA-256 CAS

## 适用场景

- 自动聚合多源资讯并生成 AI 深度总结
- 将 AI 生成内容定时发布到微信公众号或 GitHub 归档
- 通过外部 AI Agent 调用系统的抓取、筛选与发布流程

## 场景标签

`网页抓取` `AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 流光 (PrismFlowAgent) 是一个全栈自动化资讯处理系统。它能帮你从 GitHub、RSS、社交媒体抓取海量信息，利用最强的 AI (Gemini/Claude/GPT) 进行深度总结，并自动分发到你的微信公众号、Git
> L20: - **全模型适配**: 原生支持 Gemini, Claude, GPT 和本地部署的 Ollama。
> L24: - **多端触达**: 一键（或全自动）推送到**微信公众号**、存入 **GitHub** 归档，或生成标准 **RSS**。

## 星数曲线

```mermaid
xychart-beta
    title "justlovemaki/PrismFlowAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 95 --> 98
    line [96, 97, 97]
```

2026-10-18 96 → 2026-10-28 97（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fbbb5c1cfdfd` · [字段定义](../../DATASET.md)*
