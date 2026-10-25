# PeterOvermann/TriadicMemory

⭐ 41 · Wolfram Language · MIT · 推送 2026-07-10 · [GitHub](https://github.com/PeterOvermann/TriadicMemory) · 个人维护

**基于稀疏分布式表示的联想记忆算法库（C 等多语言实现）**

一组作用于稀疏分布式表示（SDR）的联想记忆算法集合，核心包括：三元联想记忆（Triadic Memory，存储 SDR 三元组、支持三方向查询与单次学习）、二元联想记忆（Dyadic Memory，实现 Kanerva 的 SDM）、以及由多个三元记忆单元与反馈线路构成的 Deep Temporal Memory 时序预测算法。提供 C 参考实现及 Chez Scheme、Javascript、Julia、Mathematica、Odin、Python、Rust 等实现。README 声明本仓库已不再活跃。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Triadic Memory 存储 SDR 三元组，任意两部分可召回第三部分，单次学习
- 容量公式 (n/p)^3：1% 稀疏度下可存取并完整检索百万级三元组
- Deep Temporal Memory 在 SPMF 数据集上报告 99.5% 预测准确率
- C 实现可编译为命令行程序或库，另有 7 种语言实现

## 适用场景

- 构建内容可寻址的三元组/语义信息存储
- 处理含噪或不完整输入的联想检索
- 基于 SDR 流的时序预测与序列学习实验

## 场景标签

 · 领域:机器学习算法/认知计算

## 证据(README 行号)

> L6: This repository is a collection of associative memory algorithms operating on sparse distributed representations, wh
> L60: A temporal memory processes a stream of SDRs, at each step making a prediction for the following step based on prev
> L69: Trained with a dataset from the SPMF project, Deep Temporal Memory achieves a prediction accuracy of 99.5 percent.

## 星数曲线

```mermaid
xychart-beta
    title "PeterOvermann/TriadicMemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7a125e3933b1` · [字段定义](../../DATASET.md)*
