# lucidrains/fast-weight-attention

⭐ 35 · Python · MIT · 推送 2026-09-17 · [GitHub](https://github.com/lucidrains/fast-weight-attention) · 个人维护

**PyTorch 快速权重情景记忆注意力模块实现，供研究者构建模型**

lucidrains 维护的 PyTorch 库，实现基于注意力的快速权重情景记忆（fast weight episodic memory），思路同类于 TTT/Titans 的 memory MLP 与 Sakana AI 的 fast weight PKM。序列内部按 chunk_size 分段处理并在段间携带快速权重记忆，段末 token 使用可学习边界嵌入且其存储目标回绕至段首 token。以 pip 包形式提供，通过 import 即可在模型中使用。

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

- 提供 FastWeightAttention 模块，基于注意力的快速权重记忆实现
- 序列按 chunk_size 分段，跨段携带快速权重记忆，无需前瞻
- 段末 token 带可学习边界嵌入，存储目标回绕至段首

## 适用场景

- 在自有 Transformer 模型中加入快速权重记忆层
- 复现或实验 TTT/Titans 类情景记忆机制
- 研究长上下文分段记忆的边界处理策略

## 场景标签

 · 领域:深度学习/模型组件

## 证据(README 行号)

> L3: An attention based fast weight episodic memory, in the same vein as the memory MLP from TTT / Titans and fast weight
> L14: import torch

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/fast-weight-attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7d5aa9fc998f` · [字段定义](../../DATASET.md)*
