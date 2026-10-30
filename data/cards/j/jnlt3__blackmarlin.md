# jnlt3/blackmarlin

⭐ 104 · Rust · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/jnlt3/blackmarlin) · 个人维护

**Rust 编写的 UCI 国际象棋引擎，NNUE 评估与 alpha-beta 搜索**

由 Doruk Sekercioglu 开发的 UCI 协议国际象棋引擎，完全用 Rust 编写，自述为 WIP。搜索部分实现迭代加深、期望窗口、PVS、多种剪枝与 Late Move Reductions、Singular Extensions、Lazy SMP 多线程等；评估采用 NNUE 神经网络（增量更新、跳跃连接、按局面阶段分桶），训练通过 Marlinflow 仓库完成。支持 Chess960。不带 GUI，需配合 UCI 图形界面使用，通过 make 编译或下载 release 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- NNUE 评估：增量更新、跳跃连接、子网络分桶
- 搜索含 Lazy SMP 多线程与原子置换表条目（XOR Trick）
- 支持 Chess960 变体
- UCI 协议兼容，可用任意 UCI 图形界面调用

## 适用场景

- 配合 UCI 图形界面对弈或分析棋局
- 作为引擎对战测试与自生成训练数据的对象
- 学习国际象棋引擎搜索与 NNUE 技术的参考实现

## 场景标签

 · 领域:游戏/博弈引擎

## 证据(README 行号)

> L9: Black Marlin is a UCI compliant chess engine fully written in Rust by Doruk Sekercioglu.
> L125: ### Neural Networks
> L137: ### Efficiently Updatable Neural Networks

## 星数曲线

```mermaid
xychart-beta
    title "jnlt3/blackmarlin 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-30"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-25 104 → 2026-10-30 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ac34ad54eccd` · [字段定义](../../DATASET.md)*
