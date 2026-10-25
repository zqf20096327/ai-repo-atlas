# Alex2262/AltairChessEngine

⭐ 59 · C++ · MIT · 推送 2026-04-21 · [GitHub](https://github.com/Alex2262/AltairChessEngine) · 个人维护

**UCI 协议 C++ 国际象棋引擎，供对弈与局面分析**

Altair 是用 C++20 编写的 UCI 协议国际象棋引擎，支持标准国际象棋与 Fischer Random（Chess960），可接入 Arena、Cutechess、Banksia 等 UCI GUI 对弈，也可在 ChessBase 等软件中做局面分析。内部采用 Bitboard 棋盘表示、magic Bitboard 走法生成、negamax 与 alpha-beta 剪枝搜索，5.0.9 起使用 NNUE 神经网络评估（当前网络 Europa 基于 31 亿 FEN 训练）。通过 release 页下载二进制或 make 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持标准国际象棋与 Fischer Random (Chess960)
- NNUE 神经网络评估（Europa，31 亿 FEN 训练数据）
- negamax + alpha-beta 剪枝 + 迭代加深搜索架构
- 可配置 hash 大小、线程数与 MultiPV

## 适用场景

- 接入 UCI GUI 与引擎对弈
- 用 ChessBase 或 lichess API 分析局面
- 参加 CCRL/CEGT 等引擎评级测试

## 场景标签

 · 领域:游戏/博弈 AI

## 证据(README 行号)

> L11:  Altair is a superhuman UCI-protocol chess engine named after the star Altair.
> L117: and currently uses NNUE (Efficiently Updatable Neural Networks) from version 5.0.9 and onwards.

## 星数曲线

```mermaid
xychart-beta
    title "Alex2262/AltairChessEngine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-25 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f6ddecb43f18` · [字段定义](../../DATASET.md)*
