# sehoon787/my-claude

⭐ 17 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sehoon787/my-claude) · [官网](https://sehoon787.github.io/my-claude/) · 个人维护

**Claude Code 一体化 agent 编组套件：Boss 编排器+32 agents+139 skills**

面向 Claude Code 用户的 agent 编组（harness）插件：以 Boss 元编排器为核心，运行时自动发现 agents、skills、MCP 工具与 hooks，按 P0-P4 优先级链把任务路由给专家 agent，并对结果做测试/lint/构建验证与最多 3 次重试。整合 16 个上游开源项目（OMC、ECC、serena、headroom、codeburn 等），提供按模型与 effort 层级的任务分派和 3 阶段 sprint 工作流。通过 install.sh 脚本或 Claude Code 插件市场安装，可分 lane 增装前端等技能包。

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

- Boss 元编排器运行时发现能力并按 P0-P4 优先级链路由任务
- 整合 32 个策展 agents、139 个 skills、3 个 MCP 服务器、8 个 hooks
- 按模型复杂度与 effort 前置字段分层分派任务
- 3 阶段 sprint 工作流（Design/Execute/Review）

## 适用场景

- 让 Boss 自动把编码任务分派给专家 agent 并验证结果
- 在 Claude Code 中一站式获得预置的 agent 团队与技能库
- 按项目需要分 lane 安装前端/浏览器测试等技能包

## 场景标签

`多智能体` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L16: **All-in-one agent harness for Claude Code.**
> L19: Boss auto-discovers every agent, skill, and MCP tool at runtime,
> L92: Boss is the meta-orchestrator at the core of my-claude. It never writes code — it discovers, classifies, matches, d

## 星数曲线

```mermaid
xychart-beta
    title "sehoon787/my-claude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `5532e8b210ce` · [字段定义](../../DATASET.md)*
