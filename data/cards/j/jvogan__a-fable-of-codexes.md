# jvogan/a-fable-of-codexes

⭐ 55 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/jvogan/a-fable-of-codexes) · 个人维护

**Claude Code 技能：让 Claude 指挥多路 Codex/Opus 工作者舰队并行开发**

一个名为 campaign-conductor 的 Claude Code skill：Claude（Fable/Opus）担任指挥者，负责规划、分发与验收，将实现任务以 Git worktree 并行分发给多个 OpenAI Codex（Sol）工作者；Sol 工作者可再派生 feature/critic/grunt 叶子代理，Opus 代理负责设计与小队领导，Sonnet/Luna 执行扫描。含分波次调度、JSON 报告、交叉评审门、偏好持久化与 LEARNINGS.md 记忆。面向使用 Claude Code 与 Codex CLI 的开发者。

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

- 指挥者-工作者分层舰队：规划/实现/评审/扫描角色分离
- Git worktree 并行写作 + campaign 状态存于仓库可跨会话续接
- Claude 与 Codex 互相评审 diff，高风险任务可跑 bake-off
- 可通过 Antigravity/Grok/Muse 等其他模型家族做只读二次意见

## 适用场景

- 在大型代码库上并行分发多个 AI 工作者执行开发任务
- 用自然语言指挥跨模型团队的代码实现与评审
- 以评审门和 bake-off 控制合并前质量

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: A Claude Code skill that makes Claude the conductor of a fleet of OpenAI Codex
> L50: The skill is campaign-conductor.
> L122: ## Requirements

## 星数曲线

```mermaid
xychart-beta
    title "jvogan/a-fable-of-codexes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-30 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1d77072ab784` · [字段定义](../../DATASET.md)*
