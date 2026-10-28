# MatPoliquin/stable-retro-scripts

⭐ 42 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/MatPoliquin/stable-retro-scripts) · [官网](https://www.videogames.ai) · 个人维护

**在复古游戏上训练强化学习模型并组织 AI 对战**

基于 PyTorch、stable-baselines3 与 stable-retro 的强化学习训练脚本集合：在复古游戏上训练 MLP、Nature CNN、Impala CNN 等模型（含实验性 Attention MLP），支持课程学习、让两个模型在 NHL94、Mortal Kombat 等 PvP 游戏中对战、玩家对抗训练好的 AI，并可导出模型供 retro-ai-runtime 在 RetroArch 等模拟器前端接管玩家输入。需自备 ROM，测试环境为 Ubuntu 与 Windows WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MLP/Nature CNN/Impala CNN/组合输入模型的训练与课程学习
- AI vs AI 对战（NHL94、Mortal Kombat、Wrestlemania 等）
- 模型可导出供 RetroArch 等前端通过 retro-ai-runtime 接管输入
- 提供 NHL94 等游戏专属示例页

## 适用场景

- 我想在复古游戏中训练强化学习模型
- 让两个训练好的模型在 PvP 复古游戏里对战
- 在模拟器里和训练好的 AI 对手游玩

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: * Train models on retro games
> L6: * Pit two models against each other on PvP retro games such as NHL94, Mortal Kombat or WWF Wrestlemania: The Arcade 
> L30: * stable-baselines3

## 星数曲线

```mermaid
xychart-beta
    title "MatPoliquin/stable-retro-scripts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2f67d2f9ea55` · [字段定义](../../DATASET.md)*
