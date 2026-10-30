# inngest/agentkit-render-tutorial

⭐ 32 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/inngest/agentkit-render-tutorial) · 组织维护

**定时汇总 Hacker News 热文并发送邮件报告的 agent 教程项目**

由 Inngest 维护的示例教程：基于 Next.js、Render 与 Inngest AgentKit 构建的 Hacker News agent。用户在 Web UI 中指定关注领域、问题与频率（每小时/每天/每周），agent 周期性生成摘要并通过 Resend 发送邮件。架构含三个部分：索引 cron 任务（将 HN 内容写入启用 pgvector 的 Render PostgreSQL）、承载 UI 与 agent 逻辑的 Next.js 应用、Inngest 的编排层。需自备 Render/Inngest/OpenAI/Resend 四类账号，通过分步指引在 Render 上部署，也可本地用 pnpm 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用户自定义关注领域、问题与摘要频率
- 索引器将 Hacker News 内容存入 pgvector 向量库
- 基于 Inngest AgentKit 的路由/agent/工具编排（AgentKit Network）
- 提供 Render 云端部署与本地运行两条路径

## 适用场景

- 定时收到自己关注的 Hacker News 主题摘要邮件
- 学习如何用 Inngest AgentKit 与 Render 搭建与部署 agent
- 参考 pgvector + cron 索引 + Next.js 的 agent 应用结构

## 场景标签

`教程课程` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L15: This Hacker News Agent periodically generates a summary of popular articles on Hacker News, and emails you a report
> L36:  This app is written in Next.js and hosted as a web service on Render. The app uses Inngest's AgentKit to create an

## 星数曲线

```mermaid
xychart-beta
    title "inngest/agentkit-render-tutorial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8d9fc1cda9e2` · [字段定义](../../DATASET.md)*
