# masaic-ai-platform/AgC

⭐ 113 · Kotlin · Apache-2.0 · 推送 2026-07-10 · [GitHub](https://github.com/masaic-ai-platform/AgC) · [官网](https://masaic.ai/) · 组织维护

**部署与编排 AI agent 的开源平台（Open Agentic Compute）**

AgC 是将 agent 作为一等计算单元的开源核心平台，提供可插拔 Agent Runtime、长期/情景/向量记忆系统、多 LLM 动态模型路由、多 agent 编排、内置追踪与可观测性（集成 OpenTelemetry）、沙箱测试与回放，以及安全治理模块。由 Platform Server（编排 API 层，内置文件搜索等工具与 MCP server）、Platform UI 与 Docker Compose 部署配置组成，支持云端中立部署，另有托管版本 platform.agc.dev。给需要在规模上运行 agent 的开发者和组织使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 作为一等计算单元的编排 API 层（内置工具与 MCP server）
- 多 LLM 动态路由与长期/情景/向量记忆系统
- 内置追踪与可观测性，集成 OpenTelemetry
- Docker Compose 多种部署模式与沙箱测试回放

## 适用场景

- 像云原生工作负载一样大规模运行和编排 agent
- 统一管理多 LLM 后端的 agent 开发与部署
- 对 agent 执行过程做追踪、观测与回放测试

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **AgC** is the open-core platform that powers **Open Agentic Compute** — a new compute substrate purpose-built for d
> L37: |**Platform Server**|Agentic orchestration API layer with built-in tools like file search, agentic file search, MCP

## 星数曲线

```mermaid
xychart-beta
    title "masaic-ai-platform/AgC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-24 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a3bbca45f17d` · [字段定义](../../DATASET.md)*
