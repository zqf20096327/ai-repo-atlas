# DGouron/review-flow

⭐ 44 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/DGouron/review-flow) · [官网](https://dgouron.github.io/review-flow) · 个人维护

**基于 Claude Code 的自动化 AI 代码审查服务：GitLab/GitHub MR/PR 触发**

面向开发团队的 Node.js/TypeScript 服务，通过 webhook 在指派审查者或打标签时触发 Claude Code 对 GitLab MR 与 GitHub PR 进行多 agent 代码审查（Clean Architecture、SOLID、Testing、DDD 等可配置），内置 MCP 服务器供 Claude 以类型化工具调用汇报进度与操作讨论线程。提供 p-queue 驱动的智能队列（并发控制、去重、内存保护）、WebSocket 实时仪表盘、开发者/团队表现洞察、推送修复后的迭代式跟进审查。每个 MR 运行于隔离 git worktree，认证走 glab/gh CLI OAuth，无需 API token。以 npm 全局安装并经 CLI 初始化运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- webhook 触发的多 agent 代码审查，agent 可按项目自定义
- 内置 MCP 服务器提供 get_workflow/start_agent/add_action 等类型化工具
- 智能队列：并发限制、时间窗去重、4GB 内存守卫、失败重试
- 推送修复后自动重读讨论线程、检查阻塞问题并发布跟进总结

## 适用场景

- 在 GitLab/GitHub 上自动审查合并请求与拉取请求
- 团队通过实时仪表盘跟踪审查进度与历史评分
- 查看每位开发者的质量、响应速度等维度洞察
- 推送修复后让 AI 自动核验阻塞问题是否解决

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Automated AI code reviews powered by Claude Code. Assign a reviewer on your merge request — Claude reviews the code
> L94: When a developer pushes fixes after a review, Claude automatically:
> L128: 1. **MCP `set_phase('completed')`** — Claude's skill calls the MCP server when the review finishes

## 星数曲线

```mermaid
xychart-beta
    title "DGouron/review-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d7f5e94bf889` · [字段定义](../../DATASET.md)*
