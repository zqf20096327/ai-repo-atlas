# HKU-BAL/Clair3-RNA

⭐ 45 · Python · BSD-3-Clause · 推送 2026-04-16 · [GitHub](https://github.com/HKU-BAL/Clair3-RNA) · 组织维护

**面向长读长 RNA 测序数据的深度学习小变异检测工具**

HKU-BAL 团队开发的 RNA 测序小变异（SNV/Indel）检测工具：读取长读长 RNA 测序 BAM（需 samtools 索引）与参考基因组，通过深度学习模型（pileup 与 phasing 模型）输出 VCF 格式变异结果。支持 ONT R10.4.1/R9.4.1 cDNA 与 dRNA（SQK-RNA004）、PacBio Sequel Iso-Seq 与 MAS-Seq 数据，提供 8 种预训练模型，可按染色体/区域/BED/VCF 位点检测，并可基于 REDIportal 标注 RNA 编辑位点（仅限 GRCh38/GRCh37）。安装提供 Docker、Singularity 与 conda 三种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 ONT cDNA/dRNA 与 PacBio Iso-Seq/MAS-Seq 数据的变异检测
- 提供 8 个预训练模型，部分支持 pileup phasing 模型
- 支持按染色体、区域、BED、指定 VCF 位点（genotyping）的调用模式
- 可利用 REDIportal 数据集标注 RNA 编辑位点（FILTER 列标记 RNAEditing）

## 适用场景

- 对长读长 RNA 测序数据做小变异检测
- 在指定基因区域或 BED 区域内做变异基因分型
- 区分真实变异与 A-to-I RNA 编辑位点

## 场景标签

 · 领域:生物信息学/基因组学

## 证据(README 行号)

> L1: # Clair3-RNA - A deep learning-based small variant caller for long-read RNA sequencing data
> L10: Clair3-RNA is a small variant caller for **long-read RNA sequencing (lrRNA-seq)** data. Clair3-RNA supports ONT R10

## 星数曲线

```mermaid
xychart-beta
    title "HKU-BAL/Clair3-RNA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b6a421d00f73` · [字段定义](../../DATASET.md)*
