# snimu/rebasin

⭐ 18 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/snimu/rebasin) · 个人维护

**将 Git Re-Basin 论文方法应用于任意 PyTorch 模型的库**

实现 Git Re-Basin 论文（Ainsworth et al., arXiv:2209.04836）中方法的 PyTorch 库：通过 PermutationCoordinateDescent 对模型权重的行列做置换（rebasin），使 model_b 向 model_a 对齐，并提供简化线性插值（LerpSimple）与 MergeMany 算法，用于降低模型合并时的损失/精度壁垒。面向深度学习研究者与开发者。限制：仅实现 weight-matching；仅支持 nn.Module 而非函数；CNN 通常工作良好，而 transformer 模型因 reshape 加残差结构大多无法被有效置换。依赖 graphviz 需系统安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PermutationCoordinateDescent 实现论文 weight-matching 方法，可应用于任意（几乎）模型而无需修改
- 提供简化线性插值 LerpSimple 与 MergeMany 合并算法
- 可打印模型图（基于 torchview）辅助诊断可置换性
- 在 hlb-CIFAR10 上显著降低 loss/accuracy barrier

## 适用场景

- 研究模型置换对称性与损失壁垒
- 对齐两个独立训练的模型以便线性插值/合并
- 复现 Git Re-Basin 论文方法于自己的 CNN 模型

## 场景标签

 · 领域:深度学习/模型合并

## 证据(README 行号)

> L8: An implementation of methods described in
> L11: Can be applied to **arbitrary models**, without modification.

## 星数曲线

```mermaid
xychart-beta
    title "snimu/rebasin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `96920fb98b39` · [字段定义](../../DATASET.md)*
