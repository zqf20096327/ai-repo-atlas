# langchain-ai/managed-deepagents

⭐ 24 · 推送 2026-10-29 · [GitHub](https://github.com/langchain-ai/managed-deepagents) · [官网](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview) · 组织维护

**帮助开发者在 LangSmith 托管基础设施上构建与部署深度 agent 的 SDK/CLI**

LangChain 团队提供的 Managed Deep Agents 工具：通过 mda CLI 初始化 agent 项目、本地开发调试并部署到 LangSmith Cloud 托管基础设施。支持 Python（uv）与 TypeScript（npm）两种语言的项目工作流，需在 .env 中配置 LangSmith 与模型提供商 API key。项目处于 public beta，SDK 在 beta 期间不开源，本仓库仅为公开落地页与 issue 跟踪器，托管服务当前仅 US 区域可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- mda CLI 提供 init/dev/deploy 项目工作流
- 支持 Python（uv）与 TypeScript（npm）两种语言
- 部署目标为 LangSmith Cloud 托管基础设施
- SDK 在 beta 期间不开源，仓库作为公开落地页与 issue 跟踪器

## 适用场景

- 用 CLI 快速创建并本地调试深度 agent 项目
- 将开发完成的 agent 部署到 LangSmith 托管环境
- 通过 GitHub Issues 报告 SDK/CLI 的 bug 与功能请求

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Build and deploy production-ready deep agents on managed LangSmith infrastructure.
> L30: mda deploy .

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/managed-deepagents 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26", "2026-10-30", "2026-10-31"]
    y-axis "stars" 19 --> 25
    line [20, 21, 22, 24, 24]
```

2026-10-18 20 → 2026-10-31 24（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a53892142874` · [字段定义](../../DATASET.md)*
