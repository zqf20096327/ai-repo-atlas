# vladfi1/phillip

⭐ 595 · Python · GPL-3.0 · 推送 2026-07-06 · [GitHub](https://github.com/vladfi1/phillip) · 个人维护

**基于深度强化学习的 SSBM（任天堂明星大乱斗DX）游戏 AI 玩家**

Phillip 是用深度强化训练的 SSBM 对战 AI，通过本地回环接口与 dolphin 模拟器通信，在游戏内对战人类或自身。提供已训练 agent（FalconFalconBF、delay0 系列、delay18/FalcoBF 等），支持带 GUI 对战、并行训练（slurm 集群或本地）、TensorBoard 查看训练统计。训练需配合使用 zmq 同步的定制版 dolphin，Windows 不支持训练。README 声明项目已不再活跃，后继项目为 slippi-ai。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度强化学习训练的 SSBM 对战 agent，附多个预训练模型
- 通过 TCP 回环接口与 dolphin 模拟器交互运行
- 支持 slurm 集群大规模并行训练与本地训练
- TensorBoard 查看训练统计

## 适用场景

- 在 dolphin 模拟器中与已训练 AI 对战 SSBM
- 自行训练新的 SSBM 对战 agent
- 观看或复现 RL 训练流程与结果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: An SSBM player based on Deep Reinforcement Learning.
> L20:  python3 phillip/run.py --gui --human --start 0 --reload 0 --epsilon 0 --load agents/FalconFalconBF --iso /path/to/

## 星数曲线

```mermaid
xychart-beta
    title "vladfi1/phillip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 594 --> 596
    line [595, 595]
```

2026-10-18 595 → 2026-10-25 595（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `18958c5bd461` · [字段定义](../../DATASET.md)*
