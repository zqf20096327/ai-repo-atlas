# CMU-SAFARI/Hermes

⭐ 77 · C++ · MIT · 推送 2026-09-15 · [GitHub](https://github.com/CMU-SAFARI/Hermes) · [官网](https://arxiv.org/abs/2209.00188) · 组织维护

**MICRO 2022 论文工件：感知机预测片外访存的微架构机制仿真**

CMU-SAFARI 发布的 MICRO 2022 论文（Bera 等）配套研究工件：Hermes 用轻量感知机预测器识别可能访问片外内存的 load 请求，并投机地在缓存访问同时直接从主存预取数据，以缩短关键路径。机制在修改版 ChampSim 模拟器中建模，兼容公开 ChampSim trace；内置 9 种片外预测器实现，可扩展 OffchipPredBase 类自定义；附 McPAT 功耗统计流程与批量实验脚本，支持 slurm 集群运行。需源码编译安装。

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

- 感知机片外 load 预测器，仅用表与增减运算实现
- 基于修改版 ChampSim 建模，兼容公开 ChampSim trace
- 内置 9 种片外预测器并可扩展自定义 predict()/train()
- 提供实验批量脚本、统计汇总与 McPAT 功耗评估流程

## 适用场景

- 复现 MICRO 2022 论文的片外访存预测实验
- 在 ChampSim 上研究/替换不同的片外预测器实现
- 评估微架构机制的性能与功耗（配合 McPAT）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L35: > Hermes is a speculative mechanism that accelerates long-latency off-chip load requests by removing on-chip cache 
> L37: The key idea behind Hermes is to: (1) accurately predict which load requests might go to off-chip, and (2) speculat
> L45: Hermes is modeled in ChampSim simulator. This modified simulator version is largely similar to the one used by Pyth

## 星数曲线

```mermaid
xychart-beta
    title "CMU-SAFARI/Hermes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-31 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c76eccd278eb` · [字段定义](../../DATASET.md)*
