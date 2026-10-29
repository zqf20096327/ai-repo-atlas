# pinky39/grove

⭐ 132 · C# · GPL-3.0 · 推送 2026-04-14 · [GitHub](https://github.com/pinky39/grove) · 个人维护

**万智牌电脑对弈游戏：实现能与休闲玩家对战的 AI**

C#/WPF 实现的《Magic: The Gathering》卡牌游戏，玩家在 Windows 上与电脑对战。已实现 1118 张卡，支持轮抽（最多 10 个 AI 对手）与现开（最多 500 个 AI 对手）赛制。AI 通过模拟对局构建博弈树，按 min/max 规则选步，模拟时不使用隐藏信息，配合启发式剪枝与针对目标选择、施放时机、战斗模拟等的专用规则；限制赛套牌由算法自动生成并经模拟比赛挑选。附卡组编辑器（Lucene 语法检索）、自定义主题与存档功能，需 .NET Framework 4.7.2，源码 GPL-3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 博弈树模拟 + min/max + 启发式剪枝的对战 AI，模拟时不读取隐藏信息
- 轮抽/现开限制赛制，最多 500 个电脑对手
- 限制赛套牌自动生成并经模拟比赛择优
- 1118 张卡牌与 4 个可玩系列

## 适用场景

- 与电脑进行万智牌单局或轮抽/现开限制赛对局
- 研究卡牌游戏中不完全信息博弈的 AI 实现
- 用卡组编辑器构建与检索卡组

## 场景标签

 · 领域:游戏/游戏AI

## 证据(README 行号)

> L114: `Magic: The Gathering` is a game with hidden state. With every move computer
> L117: scored and the best move is chosen according to the min/max rule. The unpruned

## 星数曲线

```mermaid
xychart-beta
    title "pinky39/grove 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-18 132 → 2026-10-29 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0465d566f533` · [字段定义](../../DATASET.md)*
