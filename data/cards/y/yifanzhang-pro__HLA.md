# yifanzhang-pro/HLA

⭐ 104 · HTML · CC-BY-4.0 · 推送 2026-06-15 · [GitHub](https://github.com/yifanzhang-pro/HLA) · [官网](https://yifanzhang-pro.github.io/HLA) · 个人维护

**论文项目页：高阶线性注意力机制的论文介绍**

HLA（Higher-order Linear Attention）的研究项目页面，介绍一种因果、流式线性注意力机制：通过紧凑前缀充分统计量实现高阶交互，二阶情形保持常数大小状态、逐 token 线性时间计算；给出闭式流式恒等式、严格因果掩码变体与基于 associative scan 的分块并行训练方案，并概述三阶及以上扩展。README 仅含摘要、作者与引用信息，未提供代码、安装或运行说明，许可为 CC-BY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 二阶情形常数状态、逐 token 线性时间计算，不构造 n×n 矩阵
- 分块并行训练方案基于 associative scan，精确复现串行递归的激活
- 给出严格因果掩码变体并概述三阶及以上扩展

## 适用场景

- 了解线性注意力高阶交互的建模方法
- 引用该论文用于长上下文注意力机制研究
- 追踪 State Space Models 与线性注意力方向的进展

## 场景标签

 · 领域:深度学习/模型架构研究

## 证据(README 行号)

> L9: A causal, streaming linear attention mechanism that realizes higher‑order interactions via compact prefix statistics
> L17: The quadratic cost of scaled dot-product attention is a central obstacle to scaling autoregressive language models 

## 星数曲线

```mermaid
xychart-beta
    title "yifanzhang-pro/HLA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-23 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `13c534830f06` · [字段定义](../../DATASET.md)*
