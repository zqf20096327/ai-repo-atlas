# smeznar/HVAE

⭐ 32 · Python · BSD-3-Clause · 推送 2026-03-04 · [GitHub](https://github.com/smeznar/HVAE) · [官网](https://link.springer.com/article/10.1007/s10994-023-06400-2) · 个人维护

**用分层变分自编码器将数学表达式嵌入连续空间的符号回归方法**

论文《Efficient Generator of Mathematical Expressions for Symbolic Regression》的官方代码库。实现 HVAE（分层变分自编码器，把数学表达式嵌入连续向量空间）及两个流水线：EDHiE（HVAE+进化算法做方程发现/符号回归）与 HVAR（HVAE+随机采样）。训练后可生成句法合法表达式，支持潜空间线性插值分析、重构精度评估，可在 Nguyen 基准上跑符号回归实验。提供 pip 从 GitHub 安装，参数（潜空间维度、训练轮数、种群规模等）可配置。README 声明正在重构，部分代码可能不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- HVAE 将数学表达式嵌入连续潜空间，设计上只生成句法合法表达式
- EDHiE 流水线：HVAE + 进化算法执行符号回归/方程发现
- 提供重构精度评估与潜空间线性插值分析脚本
- 训练集可由 NLTK 概率文法生成，默认 50000 条表达式

## 适用场景

- 在 Nguyen 等符号回归基准上运行方程发现实验
- 研究生成模型在符号回归中的表达式生成能力
- 分析变分自编码器潜空间的结构与插值性质

## 场景标签

 · 领域:机器学习/符号回归

## 证据(README 行号)

> L1: # Efficient Generator of Mathematical Expressions for Symbolic Regression
> L58: This repository implements HVAE and EDHiE (HVAE + evolutionary algorithm), HVAR (HVAE + random sampling). HVAE is a
> L61: Our motivation for this approach is symbolic regression (equation discovery), a machine learning task where you try

## 星数曲线

```mermaid
xychart-beta
    title "smeznar/HVAE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aee8880b8899` · [字段定义](../../DATASET.md)*
