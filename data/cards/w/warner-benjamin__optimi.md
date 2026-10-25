# warner-benjamin/optimi

⭐ 131 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/warner-benjamin/optimi) · [官网](https://optimi.benjaminwarner.dev) · 个人维护

**低精度高内存效率的 PyTorch 优化器库**

面向 PyTorch 用户的优化器库：实现 Adam/AdamW/Adan/Lion/RAdam/Ranger/SGD/StableAdamW 八种优化器，通过 Kahan 求和支持纯 BFloat16 训练以降低训练内存并提升速度；提供逐层反向中执行优化步的 gradient release、优化器累积与完全解耦权重衰减。优化器采用 Triton 实现，支持 NVIDIA（Ampere 及以上）、AMD、Intel GPU，可作为标准优化器的直接替换。限制：不支持编译、微分、复数、AMSGrad 与 Nesterov 动量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Kahan 求和支持纯 BFloat16 低精度训练，非激活训练内存可降 37-45%
- gradient release 在反向传播中逐层执行优化步并释放梯度内存
- Triton 实现支持 NVIDIA/AMD/Intel GPU，默认启用
- 支持完全解耦权重衰减，权重衰减与学习率分离

## 适用场景

- 在显存受限的单卡环境用 BFloat16 训练模型
- 替换现有 PyTorch 优化器以获得梯度内存释放
- 需要权重 decay 与学习率独立调参的训练

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: ### Fast, Modern, and Low Precision PyTorch Optimizers
> L10: optimi enables accurate low precision training via Kahan summation, integrates gradient release and optimizer accum

## 星数曲线

```mermaid
xychart-beta
    title "warner-benjamin/optimi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 129 --> 132
    line [130, 131, 131]
```

2026-10-18 130 → 2026-10-25 131（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b1b765ec28ac` · [字段定义](../../DATASET.md)*
