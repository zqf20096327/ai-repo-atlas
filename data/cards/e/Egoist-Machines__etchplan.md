# Egoist-Machines/etchplan

⭐ 29 · Python · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/Egoist-Machines/etchplan) · 组织维护

**把 agent 重复工作流编译成可免费回放例程的工具，带 agent 兜底**

面向使用 Claude Code、Codex、opencode 等 agent 的开发者：捕获本地 agent 轨迹，挖掘重复工具调用工作流，将其中参数可绑定的安全部分编译为确定性的 ExecutionPlan，回放时零模型调用；guard 失败、工具未绑定或输入漂移时回退给原 agent。提供 shadow/approval/canary/漂移熔断的信任上线流程、追加式审计日志，以及 CLI 与 MCP server。明确拒绝自由文本编码类任务的编译。Apache-2.0，local-first，Python>=3.11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完全编译后的回放零模型调用
- 从 Claude Code、Codex、opencode 本地捕获轨迹（写入 ~/.etchplan/）
- draft→shadow→approved→canary→served 的信任上线流程与漂移熔断
- 追加式审计日志记录例程决策、工具调用与回退

## 适用场景

- 我的 agent 反复执行相同的 API/MCP 工具流程，想省掉重复模型调用
- 上线编译例程前先用影子模式积累一致性证据
- 审计每个例程决策与回退原因

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: _etchplan_ watches local agent traces, mines recurring workflows, and compiles the safe ones into deterministic `Exe
> L20: **etchplan** removes repeat model calls when a validated tool workflow can replay directly, with the agent still be
> L106: **4. Run it behind your tools, with the agent as fallback.** `--registry` binds the plan's tool names to your call

## 星数曲线

```mermaid
xychart-beta
    title "Egoist-Machines/etchplan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a6a5728fa347` · [字段定义](../../DATASET.md)*
