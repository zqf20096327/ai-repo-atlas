# boatclaw/boatclaw

⭐ 24 · TypeScript · MIT · 推送 2026-07-20 · [GitHub](https://github.com/boatclaw/boatclaw) · [官网](https://boatclaw.dev) · 组织维护

**连接项目看板与 AI 编码代理的工具：看板卡片自动变 PR**

面向开发团队的 CLI 工具：监听 Trello/Jira/Linear 看板的触发列表，将卡片任务分派给 AI 编码代理（Claude Code 全支持含交互模式，Cursor/Codex 基础支持），在本地代码库中实现任务并自动创建 GitHub PR，随后移动卡片状态。支持多项目规划阶段（haiku 规划模型）、跨项目上下文传递、AI Review 阶段（审 PR 或 git diff 后批准或驳回）。通过 Claude 的 MCP 提供 ask_human/post_update 两个工具实现任务执行中的提问交互。以 npm 全局安装，需 Node.js 18+。

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

- 看板卡片→AI 实现→自动 PR 的流程自动化（Trello/Jira/Linear）
- Claude Code 交互模式：通过 MCP 的 ask_human 在执行中向工单提问并等待回复
- 多项目任务的规划阶段：分析各项目改动需求、执行顺序与共享契约
- AI Review 阶段：审 PR 或本地 diff，批准或要求修改

## 适用场景

- 在 Linear/Jira/Trello 看板上描述任务，由 AI 代理实现并提 PR
- 多项目（前后端）任务由规划模型拆解执行顺序并传递上下文
- 通过工单评论与 AI 交互澄清模糊任务

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: 3. AI implements the task in your codebase
> L33: - **Claude Code** - Full support with interactive mode

## 星数曲线

```mermaid
xychart-beta
    title "boatclaw/boatclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `22a57f885e27` · [字段定义](../../DATASET.md)*
