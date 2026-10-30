# OmerFarukTutkun/Devre

⭐ 22 · C++ · GPL-3.0 · 推送 2026-10-04 · [GitHub](https://github.com/OmerFarukTutkun/Devre) · 个人维护

**C++ 编写的 UCI 兼容国际象棋引擎（NNUE 评估）**

用 C++ 实现的开源 UCI 协议国际象棋引擎，面向棋类程序员与引擎使用者。搜索部分支持多线程 Lazy SMP、Syzygy 残局库、Chess960（FRC/DFRC）；局面评估采用嵌入二进制的 NNUE 网络（768x12+4560 兵对+59808 威胁输入→1024x2→32→32→1），网络用 bullet 训练器在自生成数据上训练。需从源码用 make 编译，支持 AVX512/AVX2/SSSE3 构建。

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

- UCI 协议兼容，可接入图形界面或其他对战程序
- NNUE 评估网络嵌入二进制，无需外部权重文件
- Lazy SMP 多线程搜索与 Syzygy 表库支持
- 支持 Chess960（FRC 与 DFRC）

## 适用场景

- 在国际象棋 GUI 中作为引擎对弈或分析局面
- 研究 alpha-beta 搜索与 NNUE 评估的引擎实现
- 参加计算机象棋引擎对测试

## 场景标签

 · 领域:游戏 AI/棋类引擎

## 证据(README 行号)

> L3: Devre is a strong open-source UCI-compatible chess engine written in C++. While writing the engine, I got great help
> L10: * NNUE evaluation, embedded in the binary

## 星数曲线

```mermaid
xychart-beta
    title "OmerFarukTutkun/Devre 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `effa427b1bc1` · [字段定义](../../DATASET.md)*
