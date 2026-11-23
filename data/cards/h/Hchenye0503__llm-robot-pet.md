# Hchenye0503/llm-robot-pet

⭐ 4 · Python · Apache-2.0 · 推送 2026-10-31 · [GitHub](https://github.com/Hchenye0503/llm-robot-pet) · [官网](youtu.be/M3AWN9dTlrI) · 个人维护

**给 25cm 双足机器人 Microduck 做 LLM 驱动的仿生宠物系统**

面向 Microduck 双足机器人的仿真宠物系统：头部相机感知主人（Grounding DINO 检测 + VLM 描述姿态），结合能量、好奇等内在驱动，由 LLM 规划器输出命名行为序列，验证器钳制越界值后交由 RL 策略驱动 14 个舵机；行为库基于动物行为学 ethogram 定义 26 种狗猫行为。全部结果来自 MuJoCo 仿真，尚未在实体机器人上运行；规划器可脱离仿真器单独以 CLI 运行（需 OpenAI API key）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于动物行为学 ethogram 的 26 种狗猫行为库，定义 LLM 规划词表
- LLM 仅输出行为计划不输出关节目标，验证器钳制/拒绝/允许重试一次
- 内在驱动（能量、好奇、想念、紧张）跨阈值时自主触发规划器
- 自定义 RL 步态策略经 3 种子预置准则验证后部署

## 适用场景

- 在 MuJoCo 仿真中体验机器人宠物的问候、陪伴等行为
- 研究 LLM 规划 + 验证器 + RL 执行的机器人控制分层架构
- 复现步态与规划器的评测流程（含 held-out 集）

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L5: choosing from a library of real dog and cat behaviors. An LLM plans, a validator checks, and RL policies move
> L33: **LLM as planner, not end-to-end control.**
> L65: |Decide|The LLM plans a short sequence of behaviors|

## 星数曲线

```mermaid
xychart-beta
    title "Hchenye0503/llm-robot-pet 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9823749e5bca` · [字段定义](../../DATASET.md)*
