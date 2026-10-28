# rohingosling/taumax-uci-chess-engine

⭐ 20 · Rust · MIT · 推送 2026-09-22 · [GitHub](https://github.com/rohingosling/taumax-uci-chess-engine) · 个人维护

**基于因果熵方程 F=T∇Sτ 的 UCI 国际象棋引擎**

用 Rust 编写的 UCI 协议国际象棋引擎，可在 Arena 等 UCI 图形界面中运行。核心机制是将 Alex Wissner-Gross 的因果熵方程应用于对抗博弈：不使用子力价值、开局库、残局库或训练网络，而是以双方合法行动空间（机动性）在有限视野内估计每个候选走法带来的未来相对自由度，将杀棋、被杀与逼和分别设为高/低/中性终局边界。提供 Random 对照策略、可选 GPU 叶子评估（带 CPU 回退）与诊断输出。作者声明目标不是棋力强度，而是探索因果熵在对抗场景中的应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以因果熵方程 F=T∇Sτ 评分合法走法的未来相对自由度
- 不依赖子力价值、开局库、残局库或训练网络
- 可选 GPU 叶子评估，运行失败时自动回退 CPU
- 支持 Arena 等 UCI 图形界面，含 Random Seed 复现实验与诊断跟踪

## 适用场景

- 在 Arena 等 UCI 界面中观察因果熵策略下棋
- 研究因果熵智能方程在对抗性博弈中的表现
- 用 Random 对照与固定种子做可复现实验

## 场景标签

 · 领域:游戏 AI/决策算法

## 证据(README 行号)

> L10: **Taumax** is a UCI-compliant chess engine written in Rust, that explores the ideas expressed by *Alex Wissner-Gros
> L16: The goal of **Taumax** is not to be a strong chess engine, but instead, to explore ways in which causal entropy may
> L155: `RelativeCausalEntropy` does not use material values, piece-square tables, opening books, tablebases,

## 星数曲线

```mermaid
xychart-beta
    title "rohingosling/taumax-uci-chess-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a4434228be53` · [字段定义](../../DATASET.md)*
