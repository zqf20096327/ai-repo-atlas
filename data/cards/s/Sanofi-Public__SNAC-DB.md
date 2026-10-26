# Sanofi-Public/SNAC-DB

⭐ 38 · Python · NOASSERTION · 推送 2026-06-08 · [GitHub](https://github.com/Sanofi-Public/SNAC-DB) · 组织维护

**抗体/NANOBODY VHH 复合物结构数据整编流水线：从 PDB 构建机器学习就绪数据集**

Sanofi 公开的 SNAC-DB 数据整编流水线仓库：从 PDB/CIF 结构文件中抽取并整编非冗余的抗体与 NANOBODY® VHH 复合物，供下游机器学习应用使用。提供三条流水线：SNAC-DB 主整编流水线、构建结构新颖的对接模型基准测试集、以及基于 FoldSeek 结构相似性检索命中结构。附带脚本通过 MMseqs2 检索 SwissProt/UniRef90 补全未解析残基。流水线由 bash 脚本编排，底层 Python 模块可单独调用；整编好的即用数据集发布在 Zenodo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条流水线：结构整编、基准测试集构建、FoldSeek 结构相似性检索
- 附带 ANARCI 补丁以处理 'X' 歧义残基
- 未解析残基补全脚本：MMseqs2 检索 SwissProt/UniRef90 并输出修正 fasta
- 即用版 SNAC-DB 数据集已在 Zenodo 发布（DOI: 10.5281/zenodo.15870002）

## 适用场景

- 我从 PDB 结构文件中抽取并整编抗体/纳米抗体复合物数据
- 我为对接或结构预测模型构建结构新颖的基准测试集
- 我用结构相似性在整编数据集中检索命中复合物

## 场景标签

 · 领域:生命科学/蛋白质结构数据

## 证据(README 行号)

> L4: This repository contains pipelines used in the Structural NANOBODY® VHH and Antibody Complex Database (SNAC-DB) proj
> L14: #### The curated version of the ready-to-use SNAC-DB dataset is available at: https://doi.org/10.5281/zenodo.158700
> L192: @article{gupta2026snacdb,

## 星数曲线

```mermaid
xychart-beta
    title "Sanofi-Public/SNAC-DB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c6fdb3830c56` · [字段定义](../../DATASET.md)*
