# yimwoo/codex-agenteam

⭐ 14 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/yimwoo/codex-agenteam) · 个人维护

**给 Codex 的多角色 AI 开发团队：六角色经可配置流水线协作**

以原生 Codex agent 形式提供六个开发角色（Researcher/PM/Architect/Dev/QA/Reviewer），通过可配置流水线编排协作，用户以 @提及调用角色或 @ATeam 整体执行。通过 install.sh 脚本安装并在 Codex 插件面板启用，依赖 .codex/agents/*.toml。支持阶段控制、验证门、重试与恢复，可选结构化交接（schema 校验与 SHA-256 溯源）和治理交付（决策日志、tripwires、审批证据），可观测性含 doctor/status/trace 等命令。

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

- 六角色（Researcher/PM/Architect/Dev/QA/Reviewer）作为原生 Codex agent
- 可配置流水线：阶段、验证门、重试、恢复、CI 修复
- 结构化交接：schema 校验的角色结果与 SHA-256 溯源
- doctor/status/trace 等观测命令与可移植证据包

## 适用场景

- 让多角色 AI 团队按流水线协作完成开发任务
- 通过 @Dev/@Reviewer 等提及单独调用某个角色
- 对较长期工作启用决策日志与审批等治理机制

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8:  A full AI development team — researcher, PM, architect, dev, QA, and reviewer — as native Codex agents, orchestrate
> L13: curl -fsSL https://raw.githubusercontent.com/yimwoo/codex-agenteam/main/install.sh | bash

## 星数曲线

```mermaid
xychart-beta
    title "yimwoo/codex-agenteam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `13609b5d75d8` · [字段定义](../../DATASET.md)*
