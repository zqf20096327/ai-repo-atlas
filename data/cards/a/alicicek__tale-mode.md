# alicicek/tale-mode

⭐ 37 · Shell · MIT · 推送 2026-07-03 · [GitHub](https://github.com/alicicek/tale-mode) · 个人维护

**给 Claude Code/Codex 加工程纪律的插件：先计划、对真实代码验证、留证据**

面向 Claude Code 与 OpenAI Codex 的插件，通过三层机制约束模型行为：指令层（技能/阶段命令）、强制层（确定性 bash hooks，含 Stop 钩子自主循环，检查未通过则阻止回合结束）、审查层（独立对抗性 plan-reviewer 与可选 governor）。提供任务分级（trivial/substantial/high-stakes）决定流程量，要求每个决策引用来源，验证需对照真实代码而非记忆。安装后 hooks 即生效，含 164 项检查的测试覆盖。要求 Claude Code ≥ v2.1.154。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层架构：指令 + 确定性 hooks 强制 + 独立对抗审查
- Stop 钩子自主循环：写目标文件并运行确定性检查，通过前回合不结束
- 任务分级（trivial/substantial/high-stakes）决定流程量
- 计划模式只读命令由 fail-closed 钩子自动批准，减少逐条确认

## 适用场景

- 让编码 agent 在动工前先对照真实代码做计划与验证
- 大型多阶段功能按 phase 逐会话推进并留存计划文件
- 要求支付/安全类改动经过独立对抗性审查后再交付

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: Not smarter — *more disciplined.* A drop-in plugin for **Claude Code and OpenAI Codex** that makes
> L62: B · ENFORCEMENT    deterministic bash hooks        session-start · phase marker · plan-mode read-only approve · the
> L187: Claude Code's `/goal` and `/loop` are user-only — *you* type them. Tale Mode ships a

## 星数曲线

```mermaid
xychart-beta
    title "alicicek/tale-mode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4e5630518464` · [字段定义](../../DATASET.md)*
