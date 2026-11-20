# mediaworkbench/steuermann-ai

⭐ 10 · Python · 推送 2026-10-26 · [GitHub](https://github.com/mediaworkbench/steuermann-ai) · 个人维护

**自托管的多智能体 AI 系统运行时，以 profile 配置适配多领域**

一个 on-prem 优先的自托管运行时，用于部署与运营多智能体 AI 系统：以 LangGraph 为编排核心，整合持久化记忆、RAG 摄取（监听目录自动分块嵌入至 Qdrant）、YAML 工具发现与 MCP 路由、Redis 缓存与 Prometheus 监控，并自带 Next.js 前端与 FastAPI 后端。各领域部署通过 YAML profile overlay 定制 LLM 提供商、提示词、工具与记忆配置，无需改动运行时代码。面向需要在自己基础设施内运行的企业/内部部署，官方声明处于实验性 Beta，尚非生产就绪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- profile overlay（YAML）逐层定制部署，无需 fork 或改代码
- 图式编排：工具选择、记忆、检索、响应均为显式图节点
- 可选认知记忆与 Dreaming Engine（遗忘/漂移/晋升/程序性四类周期，7 天可撤销）
- docker compose up 即可启动完整系统（前端+后端+Qdrant/PostgreSQL/Redis/Prometheus）

## 适用场景

- 在自有服务器内搭建不外传数据的多智能体对话系统
- 用一套代码库面向医疗、金融等不同领域做差异化部署
- 为团队提供带用户角色隔离与记忆管理的内部 AI 工作台

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L11: Steuermann (German for steersman) is a **self-hosted runtime** for deploying and operating multi-agent AI systems *
> L21: - **Not just a library — a complete application.** Ships with a frontend (chat, settings, metrics, analytics), a Fa

## 星数曲线

```mermaid
xychart-beta
    title "mediaworkbench/steuermann-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `a9e9fa1694e9` · [字段定义](../../DATASET.md)*
