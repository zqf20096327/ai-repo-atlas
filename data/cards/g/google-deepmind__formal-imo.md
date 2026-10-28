# google-deepmind/formal-imo

⭐ 36 · Lean · Apache-2.0 · 推送 2026-04-23 · [GitHub](https://github.com/google-deepmind/formal-imo) · 组织维护

**Google DeepMind 的 IMO 题目 Lean 形式化基准数据集**

收录国际数学奥林匹克（IMO）题目陈述的 Lean 4 形式化版本，作为基准数据集使用。形式化内容混合了 Google 内部编写、改编自 miniF2F 与 mathlib4/Archive 的版本，改编文件在头部注释中标注。命名约定要求每题对应 Imo/YYYY/PN.lean 文件中的 imo_YYYY_pN 定理，多部分问题可拆分为独立定理以支持部分得分。题目原文来自 IMO 官网及 AoPS Wiki 等下游副本。软件部分采用 Apache 2.0，其他材料采用 CC-BY 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IMO 题目陈述的 Lean 4 形式化集合
- 支持多部分问题拆分为独立定理以实现部分计分
- 答案猜测类问题使用 answer() elaborator 标注
- 来源混合 Google 编写与 miniF2F/mathlib4 改编并在注释中标注

## 适用场景

- 在 Lean 环境中评估定理证明系统的 IMO 题目表现
- 研究数学问题的形式化编写风格
- 作为形式数学基准数据集扩展新题目

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: This repository contains Lean formalizations of the statements of problems from the International Mathematical Olymp
> L10: This package contains a mixture of formalizations written at Google, formalizations adapted from `miniF2F`, and for

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/formal-imo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d1200da6df69` · [字段定义](../../DATASET.md)*
