# pleco-rs/Pleco

⭐ 431 · Rust · GPL-3.0 · 推送 2026-02-22 · [GitHub](https://github.com/pleco-rs/Pleco) · [官网](https://crates.io/crates/pleco) · 个人维护

**Rust 重写的 Stockfish 国际象棋引擎与库**

用 Rust 对 Stockfish C++ 代码进行直接移植的国际象棋引擎与库，分为两个 crate：pleco 提供棋盘、FEN 解析、走子生成/撤销等库功能，pleco_engine 提供 UCI 兼容的可执行引擎。项目目标是利用 Rust 的效率构建匹配现代象棋引擎速度的 Chess AI，用于两种语言的速度对比与教育目的。库通过 crates.io 以 Cargo.toml 依赖方式引入，支持 stable/beta/nightly 三个 Rust 通道，采用 GPL-3.0 许可。搜索与评估算法的功劳归属于 Stockfish 原作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stockfish C++ 代码的直接 Rust 移植
- 拆分为库 crate（pleco）与 UCI 引擎 crate（pleco_engine）
- 支持 FEN 解析、合法走子生成、apply/undo 操作
- 版本 0.5.0 起支持 stable/beta/nightly 三个 Rust 通道

## 适用场景

- 在 Rust 项目中集成国际象棋棋盘与走子逻辑
- 作为 UCI 引擎对接国际象棋 GUI 运行对局
- 对比 Rust 与 C++ 在象棋引擎上的性能表现

## 场景标签

 · 领域:游戏/棋类引擎

## 证据(README 行号)

> L10: Pleco is a chess Engine & Library derived from Stockfish, written entirely in Rust.
> L15: The overall goal for this project is to utilize the efficiency of Rust to create a Chess AI matching the speed of m

## 星数曲线

```mermaid
xychart-beta
    title "pleco-rs/Pleco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 430 --> 432
    line [431, 431]
```

2026-10-18 431 → 2026-10-26 431（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `18a66e667cb4` · [字段定义](../../DATASET.md)*
