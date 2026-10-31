# Chunjiang-Intelligence/low-rank-decay

⭐ 19 · Python · GPL-3.0 · 推送 2025-11-25 · [GitHub](https://github.com/Chunjiang-Intelligence/low-rank-decay) · 组织维护

**核范数正则化方法实现：用低秩衰减加速 Transformer Grokking**

论文《Grokking by Rank Collapse》的官方研究原型，PyTorch 实现。针对 RMSNorm/QK-Norm 等尺度不变 Transformer 中 L2 权重衰减失效的问题，提出 Low-Rank Decay：以 Newton-Schulz 迭代近似矩阵符号函数来高效计算核范数梯度（无需 SVD），诱导 QK 矩阵秩坍缩，从而在数据稀缺场景（40%-50%）扩大泛化区间并加速 Grokking。仓库以单文件自包含，提供机制分析与相图两种实验复现入口，核心类可插入 HF Trainer 等训练循环。实验任务为模加法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Newton-Schulz 迭代近似核范数梯度，无需 SVD
- 诱导 QK 矩阵秩坍缩，前 500 步内有效秩降至近 1
- 在 40%-50% 数据量区间实现完美准确率（L2 失败场景）
- 核心逻辑与优化器解耦，可插入现有训练循环

## 适用场景

- 复现 Grokking 与秩坍缩机制分析实验
- 研究生成相图的网格搜索实验
- 将低秩衰减正则化接入自己的 Transformer 训练循环

## 场景标签

 · 领域:深度学习研究/优化

## 证据(README 行号)

> L5: Status
> L73: * **Architecture:** Scale-Invariant Transformer (Pre-RMSNorm + **QK-Norm**)
> L91: *This is a research prototype.*

## 星数曲线

```mermaid
xychart-beta
    title "Chunjiang-Intelligence/low-rank-decay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e09ed32916e2` · [字段定义](../../DATASET.md)*
