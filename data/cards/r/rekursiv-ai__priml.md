# rekursiv-ai/priml

⭐ 52 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/rekursiv-ai/priml) · [官网](https://rekursiv.ai) · 组织维护

**强类型可配置 ML 训练实验构建块库，支持 A/B 测试**

面向 ML 研究实验的 Python 库：提供可组合的模型定义、优化器、损失函数、指标、训练循环与数据管线模块，通过层级化 keyword bus 传递开放关键字参数；内置 nanochat、sudoku 等基线实验配置可直接打印与运行。特色是理论计算成本分析：按算子解析 FLOPs 与字节量，对照设备（如 H100）的 roofline 拐点估算利用率，README 明确该分析基于解析模型而非实测硬件利用率。需 Python 3.12+，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- model/optimizers/loss/metrics/train/data/inference 七类可组合模块
- 基于 keyword bus 的开放关键字参数向下传递机制
- 理论 FLOPs/字节成本分析与设备 roofline 利用率估算
- 内置 nanochat、sudoku 等基线实验配置

## 适用场景

- 以强类型配置组织 ML 训练实验并做 A/B 对比
- 在运行前估算模型各算子的理论计算量与利用率
- 快速复用现成基线实验配置开展研究

## 场景标签

`模型训练` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9: ML building blocks for training experiments.
> L22: - **model** -- composable model definitions and building blocks.
> L27: - **train** -- the training loop and experiment scaffolding.

## 星数曲线

```mermaid
xychart-beta
    title "rekursiv-ai/priml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4f10eee48b59` · [字段定义](../../DATASET.md)*
