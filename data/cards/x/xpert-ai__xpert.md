# xpert-ai/xpert

⭐ 466 · TypeScript · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/xpert-ai/xpert) · [官网](https://xpertai.cn/en/) · 组织维护 · 中文 README

**构建与治理 AI Agent 团队的开源平台及桌面端 Bosi**

Xpert 是基于 NestJS 的插件式平台，提供 Agent + Workflow 运行时（Agent 定义编译为 LangGraph 状态图）、插件生命周期管理、权限/审批/审计，以及 RAG/GraphRAG 知识检索与 Agentic BI 等能力；配套桌面应用 Bosi 作为 AI 团队入口，可执行云端电脑或本地 Shell 命令（默认逐命令审批）。面向需要构建、发布和治理 AI 团队与应用的开发者与企业。自托管需 2 CPU、4 GiB RAM 与 Docker Compose，Community Edition 采用 AGPL-3.0，另有商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件优先架构：覆盖模型、工具/MCP、中间件、Skills、工作流等扩展点
- Agent 定义编译为 LangGraph 状态图，支持检查点中断/恢复与多 Agent 协作
- 治理执行：类型化工具、语义对象、策略与审批、审计与用量跟踪
- 桌面端 Bosi 支持 macOS/Windows/Linux，可操作云端电脑或执行本地 Shell 命令

## 适用场景

- 企业内自托管并治理多 Agent 工作流与业务应用
- 通过 Bosi 桌面端组织数字专家团队并审批本地命令执行
- 将 ChatKit 嵌入自有前端或用 SDK 调用 Xpert API

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L45: Build and publish the AI teams used in Bosi, Xpert Web, or your own product. Xpert provides the runtime, permission
> L100: - **AI Agents & workflows:** Agent definitions compile into LangGraph state graphs. The model–tool loop combines c

## 星数曲线

```mermaid
xychart-beta
    title "xpert-ai/xpert 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 465 --> 467
    line [466, 466]
```

2026-10-18 466 → 2026-10-24 466（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ce6c3b65ae80` · [字段定义](../../DATASET.md)*
