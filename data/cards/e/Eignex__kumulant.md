# Eignex/kumulant

⭐ 14 · Kotlin · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Eignex/kumulant) · [官网](https://eignex.com/docs/kumulant) · 组织维护

**Kotlin 多平台流式机器学习库：在线回归、bandit 与流式统计**

面向 Kotlin/JVM 与 Kotlin Multiplatform 的流式机器学习库：所有模型在线运行，边到达边更新，内存占用有界，支持来自独立分片的可合并快照（各统计量标注合并是否精确）。功能覆盖在线回归与分类（OLS、逻辑回归、softmax、朴素贝叶斯、决策树、随机森林）、多臂与上下文 bandit、异常评分、事后校准，以及 DDSketch、t-digest、HyperLogLog、变更检测等流式统计。支持 spec 组合与跨进程 wire 传输，提供三种并发模式。运行于 JVM、native Linux (x64/Arm64) 与 macOS Arm64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在线运行、内存占用有界的流式学习模型
- 快照可从独立分片合并，并标注精确/近似
- 覆盖在线回归分类、bandit、异常评分、校准与流式统计 sketch
- spec 组合与跨进程 wire 可移植的统计描述

## 适用场景

- 在数据流上做在线回归、分类或异常评分
- 构建多臂/上下文 bandit 做实时决策
- 跨分片聚合流式统计量（分位数、基数、heavy-hitter）

## 场景标签

 · 领域:机器学习库/流式计算

## 证据(README 行号)

> L14: Kumulant is a Kotlin multiplatform library for streaming machine
> L21: It covers online regression and classification (OLS, logistic, softmax,

## 星数曲线

```mermaid
xychart-beta
    title "Eignex/kumulant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `052750cb7fb4` · [字段定义](../../DATASET.md)*
