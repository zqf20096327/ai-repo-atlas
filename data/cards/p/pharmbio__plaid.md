# pharmbio/plaid

⭐ 21 · Jupyter Notebook · Apache-2.0 · 推送 2026-06-10 · [GitHub](https://github.com/pharmbio/plaid) · [官网](https://plaid.pharmb.io) · 组织维护

**给实验研究者：用约束规划生成微孔板布局设计**

PLAID 是基于 MiniZinc 约束建模语言的微孔板布局设计模型，面向从事微孔板实验的研究者。用户在文本文件（.dzn）中填写化合物、组合、对照等参数，经 Gecode 求解器运行后输出含板 ID、孔位、内容、浓度的 CSV 布局列表。支持边缘效应留空、重复化合物同行/列约束、对照孔分离与跨板平衡等布局规则。使用无需编程知识，可经 MiniZinc IDE、网页版或离线 GUI（MPLACE）操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 MiniZinc 约束编程模型，支持自定义布局约束
- 输出 CSV 格式布局（板 ID、孔位、内容、浓度），可接入自动化工具
- 对边缘效应、重复、对照分离与跨板平衡等规则建模
- 无需编程知识，提供网页版与离线 GUI

## 适用场景

- 设计高通量实验的微孔板布局以减少边缘效应与偏倚
- 自动安排对照与重复化合物在多块板上的均衡分布
- 为自动化移液工具生成可直接使用的布局 CSV

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: **PLAID** is a flexible
> L16: the quality of the data obtained from an experiment. A web version is available at plaid.pharmb.io.

## 星数曲线

```mermaid
xychart-beta
    title "pharmbio/plaid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b1f9b45b75c3` · [字段定义](../../DATASET.md)*
