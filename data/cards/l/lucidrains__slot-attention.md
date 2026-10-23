# lucidrains/slot-attention

⭐ 500 · Python · MIT · 推送 2026-06-06 · [GitHub](https://github.com/lucidrains/slot-attention) · 个人维护

**PyTorch 实现的 Slot Attention 注意力/聚类模块，供研究者使用**

GoogleAI 论文《Object-Centric Learning with Slot Attention》的 PyTorch 实现，以层形式提供 SlotAttention 模块，用于以对象为中心的学习与聚类；训练后可泛化到不同 slot 数量，forward 时可用 num_slots 关键字覆盖；另提供 MultiHeadSlotAttention 与 AdaptiveSlotWrapper，生成可微分的 one-hot 掩码决定 slot 启用。通过 pip 以 slot_attention 包名安装，README 附引用的后续论文（Adaptive Slot Attention、MetaSlot、OrthoRF）。

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

- SlotAttention 模块的 PyTorch 实现
- forward 可用 num_slots 覆盖 slot 数量
- AdaptiveSlotWrapper 生成 slot 启用的可微分 one-hot 掩码
- MultiHeadSlotAttention 多头变体

## 适用场景

- 在以对象为中心的学习研究中复现 Slot Attention
- 将 slot 机制作为可插拔层接入自有 PyTorch 模型
- 对比固定 slot 数与自适应 slot 数的实验

## 场景标签

 · 领域:深度学习/表示学习

## 证据(README 行号)

> L5: Implementation of Slot Attention from the paper 'Object-Centric Learning with Slot Attention' in Pytorch. Here is a 
> L17: ```python

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/slot-attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 499 --> 501
    line [500, 500]
```

2026-10-18 500 → 2026-10-23 500（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `eb79f91a0f21` · [字段定义](../../DATASET.md)*
