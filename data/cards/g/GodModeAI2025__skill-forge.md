# GodModeAI2025/skill-forge

⭐ 20 · Python · MIT · 推送 2026-09-20 · [GitHub](https://github.com/GodModeAI2025/skill-forge) · [官网](https://godmodeai2025.github.io/skill-forge/) · 个人维护

**通过实验循环迭代改进 agent 技能与代码的工具**

面向 AI agent 技能与通用代码库的自动化改进工具：运行『分析→假设→变异→评估→打分→保留/回退』的实验循环，Skill Mode 针对 Claude 技能的 SKILL.md 依据 eval 断言优化，Generic Mode 针对任意文件以返回数值的 shell 命令为指标优化。支持全自主与带检查点的引导两种模式；v3 将决策固化为 decide() 函数、引入分辨率下限、噪声底、防奖励篡改的 invariants 检查与受保护区域，并以 410 个测试覆盖。

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

- Skill Mode / Generic Mode 双模式实验循环，保留改进、回退回归
- 决策固化为单一 decide() 函数，keep 阈值取 max(阈值, 噪声底, 分辨率)
- invariants 快照/校验等防奖励篡改机制与 FORGE_KEEP 受保护区域
- 26 个 composite_score 子命令与 6 个 agent（假设/变异/评分/元/图书管理员等）

## 适用场景

- 夜间无人值守地迭代改进自己的 Claude 技能文件
- 以任意 shell 指标为基准自动优化代码库中的目标文件
- 以引导模式逐步审查每轮变异再决定保留或回退

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: Autonomous improvement of AI skills and generic codebases through iterative experimentation. An AI agent modifies in
> L9: **Skill Mode**: optimizes a Claude Cowork Skill's SKILL.md against eval assertions:
> L15: **Generic Mode**: optimizes any file against any shell command that returns a number:

## 星数曲线

```mermaid
xychart-beta
    title "GodModeAI2025/skill-forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4bcc35b1509c` · [字段定义](../../DATASET.md)*
