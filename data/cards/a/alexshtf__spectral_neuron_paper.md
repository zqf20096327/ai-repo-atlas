# alexshtf/spectral_neuron_paper

⭐ 23 · Jupyter Notebook · BSD-3-Clause · 推送 2026-09-05 · [GitHub](https://github.com/alexshtf/spectral_neuron_paper) · [官网](https://arxiv.org/abs/2608.08003) · 个人维护

**谱神经元论文的实验代码：可解释标量模型的训练与扩展性研究**

arXiv 论文 Spectral Neuron 的配套实验仓库：实现 x↦λₖ(A₀+x₁A₁+…+xₙAₙ) 形式的谱模型（对称矩阵学习、按序特征值输出），在合成函数与 HIGGS、Criteo 两个表格数据集上研究其训练难度、随规模变化的表现，以及形状约束与特征敏感性界等谱结构性质。使用 uv 锁定环境管理（要求 Python 3.14），提供 sanity/full 两级实验配置、repeated_shuffle 扩展协议与分析专用 notebooks，结果以 manifest 记录溯源。面向科研复现，作者声明不作为 SOTA 基准提交。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 谱模型实现：对称矩阵 + 有序特征值选择，支持形状约束
- HIGGS（1000 万训练行）与 Criteo 真实数据扩展实验及特征敏感性界验证
- uv 锁定环境与 sanity/full 双档实验配置，结果 manifest 记录产生 commit
- notebooks 仅做分析：读取留存结果、跨种子汇总并绘图

## 适用场景

- 复现论文的合成与真实数据实验
- 研究形状约束模型在表格数据上的扩展行为
- 基于谱模型代码做后续研究修改

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the experiments for the spectral neuron paper (https://arxiv.org/abs/2608.08003): scalar mo
> L11: eigenvalue. The experiments study whether these models are straightforward to

## 星数曲线

```mermaid
xychart-beta
    title "alexshtf/spectral_neuron_paper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dd74734fab00` · [字段定义](../../DATASET.md)*
