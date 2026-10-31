# projectglow/glow

⭐ 310 · Scala · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/projectglow/glow) · [官网](https://projectglow.io) · 组织维护

**面向生物银行规模的基因组学分析开源工具包**

基于 Spark 的开源基因组分析工具包，供生物信息学研究与开发者在分布式环境处理生物银行级别数据。功能包括读取 VCF/BGEN/Plink 文件到分布式 DataFrame、内置质控与数据操作函数、变异规范化与 liftOver、全基因组关联研究（GWAS）、接入 Spark ML 库做群体分层，以及并行化命令行工具扩展既有工作流。以 sbt 和 Java 8 构建，通过 conda 环境管理 Python 依赖，支持在 Databricks 集群上构建与安装构件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载 VCF/BGEN/Plink 文件到分布式 DataFrame
- 全基因组关联研究（GWAS）与变异规范化、liftOver
- 接入 Spark ML 库进行群体分层
- 并行化命令行工具与 Pandas 函数以扩展工作流

## 适用场景

- 在 Spark 上大规模处理 VCF/BGEN/Plink 基因组数据
- 开展全基因组关联研究并做质控
- 把基因组数据与电子病历等数据集联合分析

## 场景标签

 · 领域:生物信息学/基因组大数据

## 证据(README 行号)

> L7: Glow is an open-source toolkit to enable bioinformatics at biobank-scale and beyond.
> L21: - Load VCF, BGEN, and Plink files into distributed DataFrames
> L25: - Integrate with Spark ML libraries for population stratification

## 星数曲线

```mermaid
xychart-beta
    title "projectglow/glow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 308 --> 311
    line [309, 310, 310]
```

2026-10-18 309 → 2026-10-31 310（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `bbcc129b78ed` · [字段定义](../../DATASET.md)*
