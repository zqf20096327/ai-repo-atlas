# eric-cielo/moflo

⭐ 19 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/eric-cielo/moflo) · [官网](https://cielolimitada.com/moflo) · 个人维护

**给 Claude Code 的本地化 AI agent 编排工具包：记忆/路由/门禁**

面向 Claude Code 的自含式 agent 编排工具包：npm 安装后 `flo init` 即启用语义记忆（384 维 MiniLM 嵌入 + HNSW 检索）、会话启动时增量索引文档与代码、通过 hooks 强制 memory-first 与任务注册的门禁、基于任务结果反馈的学习式路由、上下文耗尽告警、YAML 多步自动化 Spell 引擎及 `/flo` GitHub issue 执行流程。全部本地运行，无需 API key 与云服务；明确仅以 Claude Code 为支持面，不对 Claude Desktop 提供集成。依赖 Node.js 22 内置 SQLite，无原生编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 384 维 all-MiniLM-L6-v2 嵌入 + HNSW 向量检索的语义记忆，开箱即用
- hooks 强制 memory-first 与任务注册门禁，任务结果反馈学习式路由
- YAML Spell 引擎定义多步自动化（shell/agent 生成/条件/循环/记忆操作）
- 全本地运行，无 API key、无云服务、无原生编译（node:sqlite）

## 适用场景

- 让 Claude Code 记住项目知识、先查记忆再探索代码
- 把 GitHub issue 走完研究→实现→测试→PR 的流程化执行
- 跨 git worktree 或团队间共享经机器沉淀的经验（learnings）

## 场景标签

`Agent 记忆` `工作流自动化` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A standalone, opinionated AI agent orchestration toolkit for Claude Code, optimized for local development.**
> L11: MoFlo makes Claude Code remember what it learns, check what it knows before exploring files, and get smarter over t
> L60: - **Claude Code is the only target** — MoFlo is built and shipped for Anthropic's Claude Code (CLI, IDE extensions,

## 星数曲线

```mermaid
xychart-beta
    title "eric-cielo/moflo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6f16b684836a` · [字段定义](../../DATASET.md)*
