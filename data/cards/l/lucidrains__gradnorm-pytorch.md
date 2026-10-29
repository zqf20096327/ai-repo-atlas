# lucidrains/gradnorm-pytorch

⭐ 135 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/lucidrains/gradnorm-pytorch) · 个人维护

**多任务训练的自适应损失权重平衡 PyTorch 库**

GradNorm 论文（Chen 等 2017）的 PyTorch 实用实现：通过梯度归一化在训练中自适应调整多个损失的权重，支持分布式训练、梯度累积、loss_mask 选择参与 GradNorm 的损失，以及退化为静态固定权重以便对照实验。也支持对中间激活的梯度做归一化，并可通过传入 Accelerator 实例与 Hugging Face Accelerate 配合使用。面向需要平衡 3 个以上辅助损失的多任务神经网络训练场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GradNorm 自适应损失权重平衡的 PyTorch 实现
- 支持分布式训练与梯度累积
- loss_mask 可控制哪些损失参与 GradNorm
- 支持对中间激活的梯度归一化及静态权重对照实验

## 适用场景

- 多任务/多辅助损失网络训练中自动平衡各项损失
- 将 GradNorm 权重与固定权重方案做对比实验
- 在 Accelerate 分布式训练流程中集成损失平衡

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: A practical implementation of GradNorm, Gradient Normalization for Adaptive Loss Balancing, in Pytorch
> L7: Increasingly starting to come across neural network architectures that require more than 3 auxiliary losses, so will

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/gradnorm-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-29 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `317a11906689` · [字段定义](../../DATASET.md)*
