# mcthouacbb/Sirius

⭐ 51 · C++ · 推送 2026-10-16 · [GitHub](https://github.com/mcthouacbb/Sirius) · 个人维护

**C++ 编写的 UCI 国际象棋引擎，供 GUI 对弈使用**

纯 C++ 实现的 UCI 协议国际象棋引擎，自身不带 GUI，需配合 Arena、Cutechess、Fastchess 等支持 UCI 的界面或对局运行器使用，也可在 Lichess 上对弈。棋盘采用 BitBoard 与 Zobrist 哈希，评估为增量更新的 Tapered Evaluation（子力、兵型、王安全等），搜索包含 Alpha-Beta 剪枝、LMR、空步剪枝、Singular Extensions、Lazy SMP 等技术。构建需 C++20、CMake 与编译器，支持 Threads 最多 2048 线程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BitBoard + Magic Bitboards 棋盘与走法生成
- Tapered Evaluation 增量更新评估，Texel 调参
- Alpha-Beta/LMR/Null Move 等完整搜索技术栈，Lazy SMP 多线程
- 支持 Chess960、非标准 UCI 命令（perft/bench/eval）

## 适用场景

- 在 UCI 兼容 GUI 中人机对弈
- 参加计算机国际象棋对局或 SPRT 测试
- 研究国际象棋引擎的评估与搜索技术实现

## 场景标签

 · 领域:游戏/棋类引擎

## 证据(README 行号)

> L3: A UCI chess engine written in c++.
> L18: Sirius can be used with any UCI Chess GUI or matchrunner including Arena, Cutechess, Cutechess-cli, Fastchess, Bank

## 星数曲线

```mermaid
xychart-beta
    title "mcthouacbb/Sirius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3a8c0c45240b` · [字段定义](../../DATASET.md)*
