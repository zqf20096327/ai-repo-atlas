# lucidrains/taylor-series-linear-attention

⭐ 102 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/lucidrains/taylor-series-linear-attention) · 个人维护

**泰勒级数线性注意力的 PyTorch 探索实现库**

对论文 Zoology 提出的 Taylor Series Linear Attention 的实现与探索，以 PyTorch 模块形式提供自注意力、交叉注意力与自回归（causal）变体，自回归路径借助 pytorch-fast-transformers 的 CUDA kernel。另含二阶 Poly-Attention（Taylor 特征映射）实现与函数组合训练示例脚本。README 指出线性注意力将二次复杂度转移到注意力头维度，二阶泰勒展开为 O(D^3)，需进一步研究。面向深度学习研究者的实验性代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 TaylorSeriesLinearAttn 的 self/cross/causal 三种用法
- 自回归变体复用 pytorch-fast-transformers 的 CUDA kernel
- 含二阶 Poly-Attention（Taylor 特征映射）实现
- 附带函数组合训练演示脚本 train_function_composition.py

## 适用场景

- 在语言模型实验中替换标准注意力为线性注意力
- 复现并研究 Zoology 论文的线性注意力方法
- 研究高阶线性注意力（Poly-Attention）的复杂度表现

## 场景标签

 · 领域:深度学习/注意力机制研究

## 证据(README 行号)

> L7: Explorations into the Taylor Series Linear Attention proposed in the paper Zoology: Measuring and Improving Recall i
> L9: This repository will offer full self attention, cross attention, and autoregressive via CUDA kernel from `pytorch-fa

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/taylor-series-linear-attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-30 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `69f8c9ac2d08` · [字段定义](../../DATASET.md)*
