# ThomasLangbroek/frugal

⭐ 38 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/ThomasLangbroek/frugal) · [官网](https://thomaslangbroek.github.io/frugal/) · 个人维护

**Claude Code 的成本优化 agent 路由插件：子任务走廉价模型**

面向 Claude Code 用户的插件，由一个路由技能、五个 agent 定义和两个 hook 组成。决策表将定位、提取、机械编辑等子任务派给 Haiku/Sonnet 层的 worker，仅在确定性校验失败时逐级升级。通过 SessionStart/PreToolUse hook 注入策略并实施内联搜索预算、昂贵层封锁与美元预算熔断；SubagentStop hook 记录本地 jsonl 指标，/frugal:router-stats 输出分层成本与节省估算。无框架、无运行时、无需 API key，仅限 Claude Code（多 provider 为文档配方非测试路径）。

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

- 决策表路由：确定性工具 → Haiku → Sonnet → 主模型 → 顶层（升级需验证失败）
- hook 级强制：内联搜索预算（默认 5）、昂贵层封锁、FRUGAL_BUDGET_USD 预算熔断（80% 警告/100% 停止确认）
- 本地 jsonl 指标记录与 /frugal:router-stats 成本报告（含委托下限估算）
- 每项目可覆盖路由规则与模型映射（.claude/routing-overrides.md、/frugal:models）

## 适用场景

- 降低 Claude Code 会话中廉价子任务的模型调用成本
- 团队统一部署路由策略并用统计报告调优决策表
- 为会话设置美元预算上限并阻止高价模型层的调用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: A cost-optimised agent router for Claude Code. Frugal teaches the main loop to send every sub-task to the cheapest e
> L11: The expensive reasoning model plans and judges; commodity work (locating files, extracting data, mechanical edits) 

## 星数曲线

```mermaid
xychart-beta
    title "ThomasLangbroek/frugal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-25 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8dd749449983` · [字段定义](../../DATASET.md)*
