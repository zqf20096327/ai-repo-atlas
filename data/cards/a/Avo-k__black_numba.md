# Avo-k/black_numba

⭐ 17 · Python · 推送 2026-05-06 · [GitHub](https://github.com/Avo-k/black_numba) · 个人维护

**用 Numba 编译的 Python 国际象棋引擎（UCI/Lichess 机器人）**

以 bitboard 表示棋局、经 Numba JIT 编译的 Python 国际象棋引擎，README 自述速度从 7300 提升至约 150 万节点/秒。搜索采用 negamax 驱动，配 Alpha-Beta 剪枝、PVS、LMR、空步剪枝、迭代加深、静态搜索与置换表；评估为过渡式（MG/EG 混合），含子力、子力位置表、兵型、通路兵、机动性等项。走子生成用 magic bitboards 并以 python-chess perft 校验。提供 UCI 接口接入 Cute Chess/Arena 等 GUI，附带 lichess-bot 模式、polyglot 开局库与 Docker 部署。Python 3.10–3.13，用 uv 管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Numba JIT 编译的 bitboard 引擎，12 子力位板 + 3 占位板表示局面
- negamax 搜索配 Alpha-Beta/PVS/LMR/空步剪枝/迭代加深/静态搜索
- 4M 条目 Zobrist 置换表与 MVV/LVA、killer、history 走子排序
- UCI 接口 + Lichess 机器人模式 + Docker/compose 无人值守部署

## 适用场景

- 在 Cute Chess、Arena 等 UCI GUI 中对弈或分析
- 以机器人账号在 Lichess 上自动应战快棋与慢棋
- 学习国际象棋引擎的 bitboard、搜索与评估实现（README 面向初学者讲解）

## 场景标签

 · 领域:游戏/博弈算法

## 证据(README 行号)

> L4: written in a clear pythonic style, black_numba is a Numba-enhanced bitboard
> L195: In order to search the best move in a given chess position, traditionnal chess
> L196: engines like Stockfish or black_numba have to explore the tree representing

## 星数曲线

```mermaid
xychart-beta
    title "Avo-k/black_numba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `570ffdec5222` · [字段定义](../../DATASET.md)*
