# omarperacha/ps4-dataset

⭐ 15 · Python · CC0-1.0 · 推送 2026-09-11 · [GitHub](https://github.com/omarperacha/ps4-dataset) · [官网](https://www.future-science.com/doi/10.2144/btn-2023-0024) · 个人维护

**蛋白质单序列二级结构预测的最大开源数据集及配套模型工具包**

提供 18,731 条蛋白质数据（PDB 编号、残基序列、9 类二级结构序列）及训练/测试划分，附带预训练模型权重（PS4-Mega、PS4-Conv）、训练与评测流程、对新序列 FASTA 文件的二级结构预测，以及基于 Rust 的 ps4-rs 预处理工具保证新样本与现有数据集非冗余。面向蛋白质结构预测研究者的数据集与模型开发工具包；数据准备需从蛋白质语言模型抽取嵌入，耗时数小时且建议 GPU，采样建议至少 16GB 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18,731 条蛋白质、9 类二级结构序列（含多聚脯氨酸螺旋）的数据集
- 预训练 PS4-Mega / PS4-Conv 权重及训练、评测、预测命令行流程
- ps4-rs 预处理工具保证新样本对 PS4 与 CB513 非冗余
- 提供 Hugging Face Space 免安装预测二级结构

## 适用场景

- 我要训练或评测蛋白质二级结构预测模型
- 我想用自己的 FASTA 序列跑二级结构预测
- 我想向社区数据集添加经非冗余校验的新样本

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: PS4 is the largest open-source dataset for Protein Single Sequence Secondary Structure prediction.
> L5: This repository contains the data itself, pretrained AI model weights, methods to validate and add new samples to th

## 星数曲线

```mermaid
xychart-beta
    title "omarperacha/ps4-dataset 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ff592ddca368` · [字段定义](../../DATASET.md)*
