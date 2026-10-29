# andrey-chmerev/the-frame-ai

⭐ 18 · JavaScript · MIT · 推送 2026-09-20 · [GitHub](https://github.com/andrey-chmerev/the-frame-ai) · [官网](https://www.npmjs.com/package/the-frame-ai) · 个人维护

**面向独立开发者的 Claude Code 辅助开发框架**

FRAME 为单人使用 Claude Code 开发产品的场景提供流程框架：以 Research→Plan→Build→Review→Ship→Reflect 六阶段组织每个会话，提供 33 个命令、10 个 AI 代理、项目记忆与 STATE/MAP 文档、安全钩子拦截破坏性命令。支持 /frame:auto 无人值守流水线、基于 git worktree 的多特性并行开发，review 阶段按 spec 的 Evidence 清单采集真实产物并按内容比对。限制：需 Node.js ≥18 与 git 仓库，深度依赖 Claude Code 运行。

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

- 六阶段工作流与 33 个命令覆盖完整开发周期
- /frame:auto 无人值守运行 plan→build→review→fix→ship
- git worktree 隔离的多特性并行与集成质量门
- spec Evidence 产物按内容比对的审查机制与 12 类统一审计

## 适用场景

- 独立开发者用 Claude Code 按流程从想法推进到部署
- 并行开发多个互不干扰的特性并统一集成
- 部署前做安全、性能、依赖等多类别审计

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: **FRAME (Framework for AI-Assisted Solo Development)** is a framework for solo developers building products with Cla
> L130: - **Pipeline autopilot**: `/frame:auto` drives plan → build → review → fix → ship unattended, with a Stop hook tha

## 星数曲线

```mermaid
xychart-beta
    title "andrey-chmerev/the-frame-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9c433153ac3b` · [字段定义](../../DATASET.md)*
