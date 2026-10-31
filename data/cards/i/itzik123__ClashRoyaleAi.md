# itzik123/ClashRoyaleAi

⭐ 25 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/itzik123/ClashRoyaleAi) · 个人维护

**皇室战争确定性对战模拟器与强化学习训练环境**

用 C++17 从零重建 Clash Royale 战斗的 headless 模拟器，经 pybind11 暴露为 Gymnasium 环境，单核约 10 毫秒跑完一整局，可 7–20 微秒 fork 任意局面用于前瞻搜索。其上提供循环 PPO（CNN+LSTM，185 万参数）训练栈、基于搜索的老师对手与 PFSP 自博弈联赛，另有从屏幕读取实时对局的视觉管线和单文件回放查看器。面向强化学习研究/实验；README 自述为活跃研究项目，agent 尚不能击败人类玩家，构建目前仅支持 Windows + VS2022，Linux/macOS 在路线图上，且声明在真实账号上自动对战违反 Supercell 服务条款。

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

- 确定性引擎：132 张卡与 41 种进化，715 个 Catch2 测试
- 单核约 10 ms 跑完整局（约 20000 倍实时），fork 局面 7–20 µs
- Gymnasium 环境 + 循环 PPO + 前瞻搜索蒸馏 + PFSP 自博弈联赛
- 视觉管线读取屏幕实时对局，驱动模拟器作为状态估计器

## 适用场景

- 在快速确定性环境中做强化学习/自博弈实验
- 前瞻搜索与策略蒸馏等方法的对比评测（成对 A/B 测试）
- 通过屏幕感知把模拟器当作真实对局的状态估计器

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L37: You can't speed up the real game, and it has no API. Reinforcement learning
> L70: - **Recurrent PPO** (CNN + LSTM, 1.85M parameters). Actions are chosen in two
> L191: This is an active research project. **The engine and tooling are the mature

## 星数曲线

```mermaid
xychart-beta
    title "itzik123/ClashRoyaleAi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bd96c74b59fa` · [字段定义](../../DATASET.md)*
