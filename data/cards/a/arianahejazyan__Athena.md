# arianahejazyan/Athena

⭐ 32 · C++ · MIT · 推送 2026-09-14 · [GitHub](https://github.com/arianahejazyan/Athena) · 个人维护

**UCI 兼容的四国象棋引擎（C++，256 位 bitboard）**

用 C++ 编写的四人国际象棋（4PC）引擎，实现 UCI 协议的全部标准命令，支持 modern/classic 两种棋盘布局。核心机制包括 256 位 bitboard 棋盘表示、优化的合法着法生成器（基准测试约 120 Mnps）、Negamax 搜索、Alpha-Beta 剪枝、迭代加深与子力计分评估。从源码用 CMake 构建，构建后可通过可执行文件进入交互式 CLI；附带 perft 与打印棋盘等调试命令。Introduction 部分标注 coming soon，功能仍以引擎核心为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UCI 协议全命令支持，兼容现代象棋 GUI
- 256 位 bitboard 棋盘表示，着法生成基准约 120 Mnps
- Negamax + Alpha-Beta 剪枝 + 迭代加深搜索
- 支持 modern/classic 两种四人棋盘布局

## 适用场景

- 接入支持 UCI 的图形界面下四人国际象棋
- 用 perft 命令验证与基准测试着法生成
- 作为四人象棋引擎开发的参考实现

## 场景标签

 · 领域:游戏/棋类引擎

## 证据(README 行号)

> L5:  A UCI-compatible four-player chess engine
> L69: - Negamax
> L73: - Material counting

## 星数曲线

```mermaid
xychart-beta
    title "arianahejazyan/Athena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5f82954d455a` · [字段定义](../../DATASET.md)*
