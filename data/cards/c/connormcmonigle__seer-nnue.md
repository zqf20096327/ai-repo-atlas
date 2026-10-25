# connormcmonigle/seer-nnue

⭐ 143 · C++ · GPL-3.0 · 推送 2026-03-14 · [GitHub](https://github.com/connormcmonigle/seer-nnue) · 个人维护

**使用神经网络评估局面的 UCI 国际象棋引擎**

原创 UCI 国际象棋引擎：以神经网络估算局面胜/和/负（WDL）概率作为局面评估，网络通过逆向学习方法从 6 子 Syzygy 残局库的 WDL 值出发、借助自身搜索逐层回溯到 32 子局面进行训练。搜索采用 alpha-beta（主变搜索）结合 Lazy SMP 多线程、Zobrist 哈希的无锁共享置换表及多种剪枝与历史启发。推理部分为自研 SIMD 实现，训练脚本使用 PyTorch，需从源码 make 编译并下载权重文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 神经网络估算 WDL 概率用于局面评估
- 从 6 子 Syzygy EGTB 出发的逆向训练方法
- 自研 SIMD 神经网络训练与执行实现
- Lazy SMP 多线程与无锁共享置换表

## 适用场景

- 作为 UCI 引擎接入国际象棋 GUI 或分析工具对弈/分析
- 研究神经网络评估与传统 alpha-beta 搜索的结合
- 参考其神经网络推理的 SIMD 实现与搜索优化技术

## 场景标签

 · 领域:棋类博弈/游戏 AI

## 证据(README 行号)

> L3: Seer is an original, strong UCI chess engine. Seer relies on a neural network estimating WDL probabilities for posit
> L13: - From scratch neural network training and execution (using OpenMP SIMD directives and SIMD intrinsics) implementat

## 星数曲线

```mermaid
xychart-beta
    title "connormcmonigle/seer-nnue 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 142 --> 144
    line [143, 143]
```

2026-10-18 143 → 2026-10-25 143（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5483c46910d8` · [字段定义](../../DATASET.md)*
