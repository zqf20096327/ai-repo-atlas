# ever-works/ever-works

⭐ 171 · TypeScript · AGPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/ever-works/ever-works) · [官网](https://ever.works) · 组织维护

**开源 agentic 运行时：AI agent 自主研究、生成并维护完整业务站点**

Ever Co. LTD 维护的 TypeScript monorepo 平台（Turborepo + pnpm，NestJS API、Next.js Web、CLI、MCP server、文档站）。用户给一个想法，多步 pipeline 中的 AI agent 完成研究、长文内容生成、完整站点/仓库代码生成、部署与定时持续更新，代码与内容均以 Git 提交管理。多模型接入（OpenAI/Anthropic/Google/Groq/Mistral/Ollama 等，经 OpenRouter 等网关），支持插件扩展、REST API、订阅计费、OAuth 认证。AGPL-3.0 许可，另有 pre-release SaaS；Docker Compose 预构建镜像或源码（Node.js>=22/pnpm）运行，生产推荐 Kubernetes。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单个提示词驱动的研究→写作→编码→部署自动化 pipeline
- 多 AI 提供方插件（OpenAI/Anthropic/Google/Groq/Mistral/Ollama）与 OpenRouter 等网关
- 代码与内容 Git 原生版本控制，含定时更新与社区 PR 工作流
- Web UI / API / CLI / Admin / MCP server / 文档单仓多应用

## 适用场景

- 从一句想法自动生成并部署内容型网站/目录站
- 让 AI agent 按计划持续维护和更新已生成的站点
- 通过 API、CLI 或 MCP 将平台能力接入其他 agent 与 IDE

## 场景标签

`代码生成` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: [Ever® Works™][uri_everworks] - **The Workshop for AI** - an open-source, extensible, **agentic runtime** that auto
> L13: Give it an idea, and AI agents handle the rest:
> L31: - **Autonomous AI agents** with a configurable, multi-step generation **pipeline**

## 星数曲线

```mermaid
xychart-beta
    title "ever-works/ever-works 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 169 --> 172
    line [170, 171, 171]
```

2026-10-18 170 → 2026-10-23 171（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7ca16422c199` · [字段定义](../../DATASET.md)*
