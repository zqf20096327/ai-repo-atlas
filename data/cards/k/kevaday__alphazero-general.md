# kevaday/alphazero-general

⭐ 92 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/kevaday/alphazero-general) · 个人维护

**AlphaZero 的 PyTorch 通用化实现，可训练任意棋盘游戏 AI**

基于 suragnair/alpha-zero-general 及其 fork 的改进版 AlphaZero 实现，用 PyTorch 编写。核心计算组件以 Cython 编译加速，提供 GUI 用于训练与 Arena 对局（人人/人机/机机）；MCTS 采用节点结构并支持批处理，支持任意玩家数量的游戏、模型门控（按胜率阈值保留更优模型）、根 Dirichlet 噪声与折扣等机制。用户通过子类化 GameState 在 alphazero/envs/ 下添加自定义游戏引擎进行训练，超参数可经命令行、GUI 或 JSON 文件配置。项目自述为 work-in-progress。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Cython 编译核心组件，相较纯 Python 最高 30x 加速
- 节点式批处理 MCTS，支持任意玩家数量的游戏
- 模型门控：按最低胜率阈值决定是否保留新模型
- 提供 GUI 训练与 Arena 可视化对局（开发中）

## 适用场景

- 训练 Connect4 等棋盘游戏的 AlphaZero 智能体
- 通过子类化 GameState 接入自定义游戏环境做强化学习
- 用 Arena 或 roundrobin 脚本比较、排名不同模型迭代

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # AlphaZero General
> L12: 1. **Cython:** The most computationally intensive components are written in Cython to be compiled for a runtime spe
> L32: python train.py --env connect4 --numMCTSSims 200 --save-args args/connect4.json

## 星数曲线

```mermaid
xychart-beta
    title "kevaday/alphazero-general 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-28 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `57b6fd241f02` · [字段定义](../../DATASET.md)*
