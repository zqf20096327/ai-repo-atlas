# vobase/vobase

⭐ 61 · TypeScript · MIT · 推送 2026-08-05 · [GitHub](https://github.com/vobase/vobase) · 组织维护

**面向 AI 编程代理的全栈 TypeScript 应用框架**

基于 Bun 的全栈 TypeScript 应用框架，在单进程内提供数据库（Drizzle+PostgreSQL/pgvector）、认证（better-auth）、文件存储、后台任务（pg-boss）、多渠道消息、审计日志，以及 AI agent 运行时（agent harness）与同进程 MCP server。采用统一模块形态与约定（单写路径、整数金额、状态机、gap-free 编号），使 Claude Code、Cursor、Codex 等 AI 编程工具生成的模块首次即可运行。通过 bun create 脚手架创建项目，Docker Compose 启动本地 Postgres，部署提供 Dockerfile 与 railway.json。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Bun 进程整合数据库、认证、存储、任务与 agent 运行时
- 统一模块形态与 skill packs 约定，供 AI 编程工具生成完整模块
- agent harness：冻结系统提示词、provider 缓存、转向间 steer/abort、空闲恢复
- 同进程 MCP server，AI 工具可读取 schema、模块与日志

## 适用场景

- 用 AI 编程工具按约定生成业务模块并保留代码所有权
- 搭建 agent 原生客服应用（WhatsApp/邮件收件箱、联系人记忆）
- 构建带认证、任务、审计的 SaaS 或内部工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L36: A full-stack TypeScript framework that gives you auth, database, storage, jobs, and a first-class AI agent runtime 
> L59: |**Agent harness**|First-class AI agent runtime (`pi-agent-core` + `pi-ai`). Frozen system prompt per wake, byte-st
> L63: |**MCP**|Model Context Protocol server in the same process. AI tools can read your schema, list modules, and view l

## 星数曲线

```mermaid
xychart-beta
    title "vobase/vobase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-31 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3434602ebd0d` · [字段定义](../../DATASET.md)*
