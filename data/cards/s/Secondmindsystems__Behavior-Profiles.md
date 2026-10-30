# Secondmindsystems/Behavior-Profiles

⭐ 18 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/Secondmindsystems/Behavior-Profiles) · 组织维护

**AI agent 行为约束的便携契约层：让预期行为显式化、可审查**

面向 AI agent 开发与治理的开源项目：Behavior Profile 是一种可移植的行为契约，写入 AGENTS.md 或 CLAUDE.md 等指令面，在任务与技能变化时保持对预期行为（守住范围、处理不确定性、请求许可、结果可审查）的显式声明。首个 Profile 为 Scope Control，要求 agent 在行动前展示任务边界并在完成后给出简报。提供 Python 校验脚本与 harness（19 条结构断言、8 组配对合成对照）验证包完整性与 profile 结构。仓库另记录一个独立的 Scope Control Runtime 实验架构（发布架构与资格记录而非可执行运行时），曾在 Windows 上用 Claude Code 2.1.137 与 PreToolUse 集成做过记录试验。

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

- 可移植行为契约，驻留在 AGENTS.md / CLAUDE.md 等指令面
- 首个 Profile：Scope Control，要求行动前展示任务边界、完成后给出变更简报
- Python 校验脚本与 harness：19 条结构断言、8 组配对合成对照（含负控制）
- 独立的 Scope Control Runtime 实验架构记录（发布架构与资格记录，非可执行运行时）

## 适用场景

- 约束 coding agent 在指定范围内完成任务，防止任务被悄悄扩大
- 在指令面中长期固化对 agent 行为的预期与边界
- 用 harness 校验 profile 包的结构完整性与判别能力

## 场景标签

 · 领域:AI agent 工程与治理

## 证据(README 行号)

> L5: Skills expand what an agent can do. Behavior Profiles describe how the agent is expected to conduct itself while usi
> L15: Capabilities describe what is technically possible. Skills provide procedures. Permissions define available operati
> L17: A profile can remain in an instruction surface such as `AGENTS.md` or `CLAUDE.md` as tasks and skills change. Wheth

## 星数曲线

```mermaid
xychart-beta
    title "Secondmindsystems/Behavior-Profiles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `8af7acc9244e` · [字段定义](../../DATASET.md)*
