# navox-labs/agents

⭐ 14 · Python · MIT · 推送 2026-08-30 · [GitHub](https://github.com/navox-labs/agents) · [官网](https://navox.tech) · 组织维护

**19 个 Claude Code 专用 AI agent：覆盖完整冲刺周期从规划到交付**

面向 Claude Code 的 agent 集合插件，附带 Python SDK 用于自主编排。19 个 agent 以 markdown 提示词形式提供，角色覆盖策略、规格、架构、UX、构建、代码审查（7 专家并行）、QA、安全（OWASP+STRIDE）、隐私、发布与回顾；通过接力契约（handoff contract）与评估门控（8/10 阈值重试）串联成冲刺链。支持 FULL/QUICK/Mobile（React Native/Expo）/HOTFIX 四种模式。目标用户为独立创始人、技术负责人与 Claude Code 新手；插件零依赖，SDK 走 Anthropic API 计费且不能使用订阅。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个分工 agent 通过接力契约与冲刺链编排
- 评估门控重试（8/10 阈值）与 10 分制评分自校验
- FULL/QUICK/Mobile/HOTFIX 四种冲刺模式
- 插件形态零依赖，另提供 Python SDK 无人值守运行

## 适用场景

- 用一条指令跑完从想法到 PR 的完整开发冲刺
- React Native/Expo 移动应用的带隐私门控开发流程
- 独立开发者以 agent 团队代替人力完成代码构建与审查

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L18: A Claude Code plugin **and** a Python CLI for autonomous orchestration. Install the plugin for interactive sprints.
> L114: The 19 agents are markdown prompts in `.claude/agents/`. Two different engines
> L122: |Billing|Your Claude subscription|Anthropic API credit|

## 星数曲线

```mermaid
xychart-beta
    title "navox-labs/agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `66bf6230ea6f` · [字段定义](../../DATASET.md)*
