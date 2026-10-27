# lucidrains/recurrent-transformer

⭐ 24 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/lucidrains/recurrent-transformer) · 个人维护

**哈佛提出的 Recurrent Transformer 的 PyTorch 探索实现（wip）**

lucidrains 对 Harvard 的 Costin-Andrei Oncescu 等人提出的 Recurrent Transformer 的探索性实现：提供 RecurrentTransformer 模块可从 recurrent_transformer 包导入，并附带在 enwik8 数据集上的训练脚本（uv run train_enwik8.py），在训练长度与外推长度上做验证。README 自标注 wip，属于研究性代码。引用列表含原论文、注意力机制与长度外推相关文献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 RecurrentTransformer 的 PyTorch 模块实现
- 附带 enwik8 训练脚本，在训练长度与外推长度上验证
- 训练脚本通过 uv 运行

## 适用场景

- 复现或试验 Recurrent Transformer 架构
- 在 enwik8 上验证长度外推能力的研究实验

## 场景标签

 · 领域:深度学习/模型架构研究

## 证据(README 行号)

> L5: Explorations into the Recurrent Transformer proposed by Costin-Andrei Oncescu et al. of Harvard University
> L18: Train on enwik8, validating at the trained length and extrapolated length

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/recurrent-transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e9c9a569f4f7` · [字段定义](../../DATASET.md)*
