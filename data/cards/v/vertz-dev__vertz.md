# vertz-dev/vertz

⭐ 45 · TypeScript · MIT · 推送 2026-05-02 · [GitHub](https://github.com/vertz-dev/vertz) · [官网](https://vertz.dev) · 组织维护

**全栈 TypeScript 框架：一份 schema 驱动 ORM、API、UI 与 AI agent**

TypeScript 全栈框架，用单一 schema 生成类型化的数据库 ORM（PostgreSQL/SQLite/D1）、CRUD API 服务器、编译型 UI 与类型化 SDK，覆盖路由、迁移、访问控制、部署（Node/Bun/Deno/Cloudflare Workers）与测试。AI 部分为 @vertz/agents 包，提供 AI agent、类型化工具与工作流。设计目标是将失败移到编译期，以减少 LLM 与团队的运行时猜测；代码库由 Claude Code 编写，当前处于 pre-release，API 会变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一份 schema 驱动数据库、API、UI 与 SDK 各层类型
- @vertz/agents 提供 AI agent、类型化工具与工作流
- 支持 Bun/Node/Deno/Cloudflare Workers 部署
- 12 个分层包：schema、db、server、ui、cli、testing、tui 等

## 适用场景

- 用 TypeScript 快速搭建类型安全的全栈应用
- 构建带类型化工具调用的 AI agent
- 将全栈应用部署到 Cloudflare Workers 等运行时

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8:  Database ORM, API server, compiled UI, AI agents, and a custom runtime — one schema drives every layer. If it build
> L90: |**Agents**|AI agents, typed tools, workflows, Cloudflare Workers|`@vertz/agents`|
> L124: **The problem:** LLMs write code fast — but they can't run it. They can't see the runtime error. They can't know t

## 星数曲线

```mermaid
xychart-beta
    title "vertz-dev/vertz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8278fbd3cc4b` · [字段定义](../../DATASET.md)*
