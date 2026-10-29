# eren23/neo-unify

⭐ 52 · Python · 推送 2026-03-08 · [GitHub](https://github.com/eren23/neo-unify) · 个人维护

**玩具级统一多模态模型实验：MLX 上复现 Neo-Unify 架构**

受 SenseNova Neo-Unify 论文启发的从零复现实验库，基于 MLX 在 Apple Silicon 上训练。以 18,000 张 16x16 合成图像（6 个程序生成类别）为数据，分 5 个阶段递进实现：VQ-VAE+自回归 Transformer、Flow Matching Transformer、共享注意力+任务专家 FFN 的 Mixture-of-Transformers（理解分类+流匹配生成一体），以及加入 CFG/EMA/RK2 与 VQ-VAE 潜空间生成的两个扩展实验。非官方实现，规模为玩具级（最大 2.4M 参数），Python 3.9。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 共享注意力+任务专家 FFN 的 MoT 结构，单模型同时做分类与生成
- 5 个递进实验：AR 基线、Flow 基线、MoT、CFG/EMA/RK2、潜空间生成
- Phase C 分类准确率 6000/6000，理解任务未因共享主干退化
- 重建头 MSE 0.000010，低于 VQ-VAE 的 0.004

## 适用场景

- 在小规模数据上理解统一多模态模型的架构行为
- 学习 Mixture-of-Transformers 与 flow matching 的实现方式
- 在 Apple Silicon 本地跑通理解+生成一体的实验流程

## 场景标签

`多模态` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Toy-scale experiments inspired by Neo-Unify (SenseNova), which introduces an encoder-free unified multimodal model w
> L22: |**C**|Mini Neo-Unify (MoT)|**Neo-Unify**|ONE model with shared attention + task-specific expert FFNs for both unde
> L38: **Framework:** MLX on Apple Silicon (M-series GPU). All models use NHWC format per MLX convention. Python 3.9.

## 星数曲线

```mermaid
xychart-beta
    title "eren23/neo-unify 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-29 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `874c1553de7c` · [字段定义](../../DATASET.md)*
