# trekhleb/nano-neuron

⭐ 2,273 · JavaScript · MIT · 推送 2025-11-23 · [GitHub](https://github.com/trekhleb/nano-neuron) · 个人维护

**7 个纯 JavaScript 函数演示机器学习**

教学性质的代码示例：用 7 个纯 JavaScript 函数从零实现一个超简化的'神经元'，覆盖模型预测（y=w*x+b）、代价计算、前向/反向传播与训练循环，训练其学会摄氏到华氏温度的换算。无任何第三方库、外部数据集或依赖，数据由换算函数生成（100 个训练/测试样本）。README 明确声明这是刻意过度简化的入门演示，跳过了大量机器学习概念，不构成完整指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现 predict、predictionCost、forwardPropagation、backwardPropagation、trainModel 等 7 个函数
- 训练单一神经元学会摄氏→华氏换算（w≈1.8、b≈32）
- 无第三方库、无外部数据集与依赖，纯 JavaScript
- 含学习率 alpha、epochs 等训练参数的可调示例

## 适用场景

- 通过可运行的极简代码理解前向/反向传播
- 体会学习率与训练轮数对收敛的影响
- 作为机器学习入门的第一步教学材料

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > 7 simple JavaScript functions that will give you a feeling of how machines can actually "learn".
> L15: ☝🏻These functions are **NOT**, by any means, a complete guide to machine learning. A lot of machine learning concep

## 星数曲线

```mermaid
xychart-beta
    title "trekhleb/nano-neuron 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 2272 --> 2274
    line [2273, 2273]
```

2026-10-18 2,273 → 2026-10-24 2,273（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5793f8e41dd3` · [字段定义](../../DATASET.md)*
