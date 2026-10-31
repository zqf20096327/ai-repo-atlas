# julilien/LabelRelaxation

⭐ 15 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/julilien/LabelRelaxation) · 个人维护

**PyTorch 版 label relaxation 损失函数库：改进分类校准**

AAAI 2021 论文 'From Label Smoothing to Label Relaxation' 的 PyTorch 实现包，以 PyPI 包 label-relaxation 发布（Python ≥ 3.10，PyTorch ≥ 2.13）。核心机制：用 credal 集合（给观测类至少 1-alpha 概率的所有分布）替代点目标分布，预测落入集合内损失与梯度均为零，否则惩罚到集合最近成员的 KL 散度。可作为 nn.CrossEntropyLoss 的替代直接使用，支持 Mixup/CutMix 混合目标（四情形闭式解）、token 级输入与 fp16/bf16 autocast；拒绝任意软标签输入。legacy/ 目录保存原 TensorFlow 2 论文代码供复现。

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

- credal 集合替代点目标的 label relaxation 损失，集合内预测零损失零梯度
- nn.CrossEntropyLoss 的 drop-in 替代，支持形状 (batch, seq_len, vocab) 的 token 级输入
- Mixup/CutMix 混合目标的 credal 集推广，含 KKT 闭式解推导
- 71 个测试对冻结的 legacy TensorFlow 实现做数值与梯度等价校验

## 适用场景

- 训练需要更好校准的分类模型时替换交叉熵损失
- Mixup/CutMix 数据增强训练中使用混合目标损失
- 复现 AAAI 2021 label relaxation 论文实验

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: A modern, tested PyTorch implementation of the **label relaxation** loss from
> L18: This repository contains the maintained `label-relaxation` package (PyTorch) and, under
> L39: criterion = LabelRelaxationLoss(alpha=0.1)  # drop-in for nn.CrossEntropyLoss

## 星数曲线

```mermaid
xychart-beta
    title "julilien/LabelRelaxation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f2597615025f` · [字段定义](../../DATASET.md)*
