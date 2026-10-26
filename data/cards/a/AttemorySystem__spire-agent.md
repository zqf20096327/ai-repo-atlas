# AttemorySystem/spire-agent

⭐ 38 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/AttemorySystem/spire-agent) · 组织维护 · 中文 README

**自主游玩《杀戮尖塔》的 AI agent，实现 A20H 多次通关**

面向游戏 AI 研究与爱好者的《杀戮尖塔》自主代理：将游戏划分为地图、构筑、战斗三个决策单元，由确定性 harness 保证交互正确，战斗决策交给 sts_lightspeed 快速模拟器与 MCTS，构筑决策基于专家胜利卡组模板（Winning Path），仅开放式取舍交由可配置的 LLM 判断。每次运行完整记录并可重放，作为后续策略改进的固定测试证据。铁甲战士与故障机器人均在进阶 20 心脏局达成多次通关。需在 Linux/macOS 上安装 Steam 游戏与多个 mod，并用 CMake 编译模拟器，Windows 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 铁甲战士与故障机器人均达成多次 A20H（进阶20心脏）通关
- 战斗决策由 sts_lightspeed 快速模拟器 + MCTS 完成，非 LLM 计算
- 全部运行可记录重放，冻结轨迹用于策略改进的回归比较
- Winning Path 基于专家（Baalorlord）胜利卡组模板做选卡

## 适用场景

- 让 AI 代理自主运行《杀戮尖塔》进阶局
- 研究 LLM 与 MCTS/确定性工具混合的 agent 架构
- 重放既有运行并基于固定证据迭代决策策略

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: **Spire Agent: An Autonomous Agent for Slay the Spire**
> L165: - **Combat Agent** receives the complete combat state. Its default tool searches
> L166:  `sts_lightspeed` with MCTS and returns one root action plus any required card

## 星数曲线

```mermaid
xychart-beta
    title "AttemorySystem/spire-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-26 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3fe88c9571fe` · [字段定义](../../DATASET.md)*
