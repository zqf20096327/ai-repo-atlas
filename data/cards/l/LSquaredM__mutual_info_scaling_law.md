# LSquaredM/mutual_info_scaling_law

⭐ 14 · Python · NOASSERTION · 推送 2025-11-09 · [GitHub](https://github.com/LSquaredM/mutual_info_scaling_law) · [官网](https://neurips.cc/virtual/2025/loc/san-diego/poster/115721) · 组织维护

**NeurIPS 2025 论文官方代码：长上下文语言建模的互信息标度律**

论文 L²M 的官方代码仓库，复现其提出的二部互信息标度律实验：利用 LLM 估计自然语言中的二部互信息与两点互信息，并在 PG19 数据集上开展长上下文语言建模实验。论文提出 L²M 条件，将模型有效长上下文建模能力与其存储历史信息的隐状态规模标度关联。仓库分为互信息估计与 PG19 训练两部分，面向科研复现者，未在 README 中给出安装或运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 利用 LLM 估计二部互信息与两点互信息
- PG19 数据集上的长上下文建模实验代码
- 对应 NeurIPS 2025 论文的官方实现

## 适用场景

- 复现论文中的互信息标度律实验
- 研究长上下文语言建模能力与隐状态规模的关系

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Official code repository for the paper "L²M: Mutual Information Scaling Law for Long-Context Language Modeling".
> L7: This repository contains code for reproducing the experiments and results from our paper, which establishes a bipart
> L25: - `measure_mutual_info/`: Code for estimating bipartite mutual information using LLMs as well as the two-point mutu
> L26: - `train_on_pg19/`: Code for experiments on the PG19 dataset

## 星数曲线

```mermaid
xychart-beta
    title "LSquaredM/mutual_info_scaling_law 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5d95b179c6d4` · [字段定义](../../DATASET.md)*
