# sgrvinod/chess-transformers

⭐ 160 · Python · MIT · 推送 2025-12-31 · [GitHub](https://github.com/sgrvinod/chess-transformers) · 个人维护

**训练 Transformer 下国际象棋的 PyTorch 库，含 4 个预训练模型**

用于训练 Transformer 模型下国际象棋的 Python 库，模型从人类棋局数据（Lichess 棋谱）中学习走子。提供 4 个预训练模型（20M–85M 参数，纯编码器或编码器-解码器架构），预测形式包括最佳着法（UCI 记法）、From/To 格子预测及着法序列预测，检查点可自动下载。模型在 Fairy Stockfish 引擎 1–6 强度等级下各进行 1000 局对弈评测并给出胜率与 Elo 差。训练/对弈引擎需通过环境变量配置数据目录与 Stockfish 可执行文件路径（可选），安装方式为克隆仓库后 pip 本地安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个预训练模型（20M–85M 参数），检查点自动下载
- 对 Fairy Stockfish 1–6 级各 1000 局对弈评测，给出胜率与 Elo 差
- 支持三种预测形式：UCI 着法、From/To 格子、着法序列（多任务训练）
- 4 个训练数据集，最大含 1.27 亿数据点

## 适用场景

- 加载预训练模型与之对弈或用于研究
- 从人类棋局数据训练自己的 Transformer 棋类模型
- 复现不同架构（编码器 vs 编码器-解码器）的棋力评测结果

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: *Chess Transformers* is a library for training transformer models to play chess by learning from human games.
> L39: |***CT-E-20***|20M|***LE22ct***|Transformer encoder only|Best next half-move (or ply) eg. *f2e3*|

## 星数曲线

```mermaid
xychart-beta
    title "sgrvinod/chess-transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 159 --> 161
    line [160, 160]
```

2026-10-18 160 → 2026-10-26 160（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b6680d59f868` · [字段定义](../../DATASET.md)*
