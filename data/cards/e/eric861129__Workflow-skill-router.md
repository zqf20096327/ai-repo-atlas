# eric861129/Workflow-skill-router

⭐ 17 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/eric861129/Workflow-skill-router) · [官网](https://huangchiyu.com/Workflow-skill-router/) · 个人维护 · 中文 README

**为 Codex agent 做 Skill 路由与阶段化工作流编排的插件**

面向 Codex 用户的开源插件：在单任务、分阶段工作与托管 Goal 三种形态下，依据个人/工作区 Routing Profile 用确定性规则选取最小可用 Skill 集合，并通过 Runtime Capability Discovery 区分已安装/可用/已授权的能力。Plugin+MCP 模式提供 12 个类型化工具，持久化本地计划与同意记录；也可作为纯指令型 Skill 使用，但无法持久化执行同意状态。不安装或激活 Skill，不授予部署权限。评估为探索性，未证明开发结果改善。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 个人/工作区 Routing Profile 映射任务到主 Skill 与阶段支持
- Runtime Capability Discovery 区分安装/暴露/认证/授权/新鲜度五类事实
- Plugin+MCP 模式提供 12 个类型化 MCP 工具与本地计划/同意记录
- Explicit Skill Lock：用户指定的 Skill 为权威选择，支持性添加需说明并征得同意

## 适用场景

- Skill 库变大后让 Codex 按我定义的流程选 Skill
- 规划-实现-验证分阶段工作流，每阶段独立选 Skill 并做完成检查
- 跨项目恢复有依赖关系的工作图

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Workflow Skill Router helps Codex choose Skills for the task at hand, keep each phase focused, and respect the workf

## 星数曲线

```mermaid
xychart-beta
    title "eric861129/Workflow-skill-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2167ccd6dfc0` · [字段定义](../../DATASET.md)*
