# enveda/kgem-ensembles-in-drug-discovery

⭐ 21 · Jupyter Notebook · NOASSERTION · 推送 2026-09-09 · [GitHub](https://github.com/enveda/kgem-ensembles-in-drug-discovery) · [官网](https://enveda.com/) · 组织维护

**药物发现场景下知识图谱嵌入模型集成预测的论文代码库**

论文《Ensembles of knowledge graph embedding models improve predictions for drug discovery》的源码与数据仓库：在 OpenBioLink 与 BioKG 两个公开生物医学知识图谱上训练并评估 ComplEX、ConvE、RotatE 等 10 个知识图谱嵌入模型，研究将多个模型的预测结果集成以提升药物-疾病三元组排序的 Precision@K。代码基于 PyKEEN（底层 PyTorch），提供 requirements.txt 安装依赖、train_model.py 训练脚本，已训练模型与预测结果托管于 Zenodo。许可证为 CC BY-NC 4.0，自标成熟度 level-1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在两个公开生物医学 KG 上基准测试 10 个 KGE 模型
- ensemble-all 与 ensemble-top5 两种集成方式的 Precision@K 评估
- 基于 PyKEEN/PyTorch，提供训练脚本与依赖清单
- 已训练模型与预测结果托管于 Zenodo

## 适用场景

- 复现论文中的 KGEM 集成实验
- 获取药物发现链接预测的预训练模型与预测结果
- 比较不同知识图谱嵌入模型在生物医学 KG 上的表现

## 场景标签

`知识图谱` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: In this work, we investigate the performance of ten knowledge graph embedding (KGE) models on two public biomedical
> L16: Thus, we assess whether combining the predictions of several models can lead to an overall improvement in predictiv
> L55: This repository contains code to replicate the experiments detailed in the accompanying manuscript. Each model is

## 星数曲线

```mermaid
xychart-beta
    title "enveda/kgem-ensembles-in-drug-discovery 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a425f8792c21` · [字段定义](../../DATASET.md)*
