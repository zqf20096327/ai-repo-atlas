# cozytab/fable5-mode

⭐ 106 · Python · MIT · 推送 2026-07-15 · [GitHub](https://github.com/cozytab/fable5-mode) · 个人维护 · 中文 README

**让任意 Claude 模型获得严格工作纪律的 Claude Code 技能与守卫钩子**

由一个 SKILL.md 技能与四个 Python 钩子组成的 Claude Code 扩展，为非前沿 Claude 模型施加流程约束：写代码前必须先产出含机器可检验验收条件的 SPEC 计划、任务卡片未通过验收命令不得推进、关键输出需经对抗性反驳、结束时账本有未勾项则阻止收尾。钩子按项目级 .fable/ 目录选择启用，fail-open 设计。声称弥补的是纪律差距而非能力差距；hooks 需 python3 与 POSIX 环境，原生 Windows 上强制层未测试。

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

- 计划门（Plan Gate）：编码前先写含机器可检验验收测试的 docs/SPEC.md
- 四个钩子将最常被规避的规则变为硬性阻断（模型上限、账本未清不许停等）
- 项目级 opt-in（.fable/ 目录）、fail-open、幂等安装脚本
- 并发分两档：保守默认 ≤5 并发子代理，吞吐模式按需开启

## 适用场景

- 在严肃项目中用钩子强制 AI 先规划再编码、留证据再收尾
- 让较便宜的 Claude 模型按结构化流程执行多卡片任务
- 在 Claude Code 里按名触发'fable 模式'获得严谨工作流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: Claude Code skill plus guard hooks that give a
> L108: **Prerequisites**: Claude Code, and `python3`

## 星数曲线

```mermaid
xychart-beta
    title "cozytab/fable5-mode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-29 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ee9de9681ce8` · [字段定义](../../DATASET.md)*
