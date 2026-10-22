# banmu123/LoomFlow

⭐ 141 · TypeScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/banmu123/LoomFlow) · [官网](https://loom-flow-ashen.vercel.app) · 个人维护 · 中文 README

**面向个人与小团队的 AI 原生工作流构建器：自然语言生成可发布为 API 的工作流**

自托管的 AI 工作流平台：用户用自然语言描述流程，AI 生成含 12 种节点类型（LLM/HTTP/Code 等）的可执行工作流并加载到可视化画布，可一键发布为带全局 API Key 的 HTTP 端点或生成免登录分享页。内置演进引擎（定时/指标/事件触发回归检测并生成 AI 优化提案，需人工批准）、节点级执行追踪、画布 AI 助手与工作流笔记。通过管理后台接入任意 OpenAI 兼容模型（如 DeepSeek），无需改代码。提供一条命令的 Docker 自托管部署（含 PostgreSQL/PostgREST/Nginx），最低 1 GB 内存；也可用 Vercel Serverless 做演示（不支持长任务）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述直接生成可执行工作流并加载到画布
- 一键发布为带统一 API Key 的 HTTP API 与免登录分享页
- 演进引擎：自动回归检测 + AI 优化提案，人工批准后生效
- 管理后台接入任意 OpenAI 兼容模型（如 DeepSeek），零代码

## 适用场景

- 不搭编排平台就快速做出一个 AI 自动化流程并对外提供 API
- 把内容创作等重复步骤变成一键运行的自动化流
- 给客户做可分享、可运行的 AI 工作流演示

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: An AI-native workflow runtime with built-in evaluation, evolution, and quality gates.
> L11: Describe your idea in natural language → generate a runnable workflow → customize it on a visual canvas → publish i
> L112: Add **any model** (DeepSeek / Ark / any OpenAI-compatible endpoint) through the admin UI — **no code changes**:

## 星数曲线

```mermaid
xychart-beta
    title "banmu123/LoomFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 140 --> 142
    line [141, 141]
```

2026-10-18 141 → 2026-10-22 141（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `d516fabb0ffa` · [字段定义](../../DATASET.md)*
