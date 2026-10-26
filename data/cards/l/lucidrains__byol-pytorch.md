# lucidrains/byol-pytorch

⭐ 1,899 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/lucidrains/byol-pytorch) · 个人维护

**PyTorch 实现的 BYOL 自监督学习库，可包裹任意图像网络**

DeepMind 论文 Bootstrap Your Own Latent 的 PyTorch 实现：提供一个模块，可包裹任意基于图像的神经网络（残差网络、判别器、策略网络），指定图像尺寸与隐藏层后，即可利用无标注图像数据做自监督训练，以提升下游监督任务表现。默认使用 SimCLR 论文的数据增强，支持自定义增强管线、SimSiam 变体（use_momentum=False）、通过 return_embeddings 取嵌入/投影，并集成 Hugging Face Accelerate 提供分布式训练（BYOLTrainer）。以 pip 包形式发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可包裹任意图像网络进行 BYOL 自监督预训练
- 内置 SimSiam 变体（use_momentum=False，无需更新移动平均）
- 可取回嵌入与投影（return_embeddings）
- 通过 BYOLTrainer 与 Hugging Face Accelerate 支持分布式训练

## 适用场景

- 用无标注图像数据预训练视觉骨干网络
- 在下游监督任务前提升残差网络等的表现
- 复现或实验 BYOL/SimSiam 自监督变体

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: Practical implementation of an astoundingly simple method for self-supervised learning that achieves a new state of 
> L9: This repository offers a module that one can easily wrap any image-based neural network (residual network, discrimin

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/byol-pytorch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 1898 --> 1901
    line [1900, 1899, 1899]
```

2026-10-18 1,900 → 2026-10-26 1,899（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3321c3c4a0d4` · [字段定义](../../DATASET.md)*
