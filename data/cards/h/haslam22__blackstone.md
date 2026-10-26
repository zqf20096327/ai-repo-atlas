# haslam22/blackstone

⭐ 42 · Java · MIT · 推送 2025-12-19 · [GitHub](https://github.com/haslam22/blackstone) · 个人维护

**带内置 AI 的五子棋（Gomoku）游戏管理器**

Java 编写的五子棋对局程序，包含基于 Negamax（Minimax + α-β 剪枝）的内置 AI 玩家与 JavaFX 图形界面对局管理器。支持自由规则五子棋对弈、每步/每局时限与棋盘尺寸配置、棋局保存与加载（保持落子顺序）、高 DPI 显示，并可加载符合 Piskvork 协议的外部 AI。运行需 Java 11+，以可运行 jar 发布；开发构建需 Maven 3.8+。README 列出 AI 性能限制：无置换表、无双重威胁检测、无 VCT 搜索，局面评估为实时计算。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Negamax（Minimax + α-β 剪枝）内置 AI 玩家
- 加载符合 Piskvork 协议的外部 AI
- 每步/每局时限与棋盘尺寸可配置
- 棋局保存与加载（保持落子顺序）

## 适用场景

- 与内置 AI 进行自由规则五子棋对弈
- 通过 Piskvork 协议加载外部五子棋 AI 对局
- 保存和复盘对局局面

## 场景标签

 · 领域:游戏/棋类

## 证据(README 行号)

> L3: A **Gomoku** (Five in a Row) game manager featuring a powerful AI written in `Java`. Download the latest release **h
> L7: * A strong AI player based on Minimax with α-β pruning, alongside many performance optimisations (haslam.blackstone.

## 星数曲线

```mermaid
xychart-beta
    title "haslam22/blackstone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `852dc6cce5b3` · [字段定义](../../DATASET.md)*
