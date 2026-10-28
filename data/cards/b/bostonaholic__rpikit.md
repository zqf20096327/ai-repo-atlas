# bostonaholic/rpikit

⭐ 20 · Shell · MIT · 推送 2026-10-28 · [GitHub](https://github.com/bostonaholic/rpikit) · [官网](https://bostonaholic.github.io/rpikit/) · 个人维护

**Claude Code 插件：Research-Plan-Implement 结构化开发工作流**

面向 Claude Code 的插件，实现 Research-Plan-Implement（RPI）框架：先研究代码库、再制定计划、经人工批准后实施。提供 9 个斜杠命令覆盖头脑风暴、代码库研究、计划编写、实施、代码/安全审查与 ADR 记录；完整管线使用并行子代理并在阶段间设批准门，实施在隔离 git worktree 中运行。各阶段产物输出到 docs/plans/ 与 docs/decisions/。README 顶部声明已弃用，推荐迁移到 bostonaholic/team。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个斜杠命令覆盖研究-计划-实施全流程
- 阶段间人工批准门与并行研究子代理
- 实施运行在隔离 git worktree 中保护主分支
- 附 16 个方法论技能（TDD、系统化调试、ADR 等）

## 适用场景

- 在 Claude Code 中按结构化流程完成功能开发
- 开发前对陌生代码库做研究并生成带 file:line 引用的报告
- 将架构决策记录为 ADR 文档

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L1: # rpikit
> L6: A plugin implementing the **Research-Plan-Implement (RPI)** framework for disciplined software engineering.
> L20: /plugin marketplace add bostonaholic/rpikit

## 星数曲线

```mermaid
xychart-beta
    title "bostonaholic/rpikit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5e7c55aed72e` · [字段定义](../../DATASET.md)*
