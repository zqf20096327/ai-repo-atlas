# QueensGambit/CrazyAra

⭐ 296 · Jupyter Notebook · GPL-3.0 · 推送 2026-03-02 · [GitHub](https://github.com/QueensGambit/CrazyAra) · [官网](https://lichess.org/@/CrazyAra) · 个人维护

**深度学习国际象棋变体 UCI 引擎，下 Crazyhouse 等变体棋**

开源神经网络棋类变体引擎，起源于 TU Darmstadt 2018 年学期项目，后由 Johannes Czech 移植为 C++ 版本。采用 AlphaZero 式技术：神经网络结合 MCTS/MCGS 搜索，先以 lichess.org 人类对局做监督学习，再用强化学习训练 Crazyhouse、Chess 等变体。以 UCI 引擎形式提供，需配合 GUI（Cute Chess、XBoard 等）使用；提供 Linux/Windows/Mac 二进制（CUDA/TensorRT 或 MXNet/CPU 后端）及预训练模型，训练脚本位于 Python 代码库。附带多篇论文与学位论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 神经网络 + MCTS/MCGS 搜索的 UCI 国际象棋变体引擎
- 提供 Linux/Windows/macOS 二进制（GPU 与 CPU 后端）与预训练模型
- 监督学习与强化学习训练脚本（Python，DeepCrazyhouse/src）
- 支持 Crazyhouse 与 Chess 变体，附 ICAPS/Frontiers 论文

## 适用场景

- 通过 UCI GUI 与 AI 对弈 Crazyhouse 等变体棋
- 研究者复现或改进 AlphaZero 式棋类训练流程
- 在 lichess 等平台使用其 bot 账号对弈

## 场景标签

 · 领域:游戏 AI/深度学习

## 证据(README 行号)

> L19: _CrazyAra_ is an open-source neural network chess variant engine, initially developed in pure python by Johannes Cz
> L25: The project is mainly inspired by the techniques described in the Alpha-(Go)-Zero papers by David Silver, Thomas Hu
> L32: _CrazyAra_ is an UCI chess engine and requires a GUI (e.g. Cute Chess, XBoard, WinBoard) for convinient usage.

## 星数曲线

```mermaid
xychart-beta
    title "QueensGambit/CrazyAra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 295 --> 297
    line [296, 296]
```

2026-10-18 296 → 2026-10-24 296（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2f87d8253c64` · [字段定义](../../DATASET.md)*
