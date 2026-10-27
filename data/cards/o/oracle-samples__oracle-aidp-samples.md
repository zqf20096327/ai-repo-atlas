# oracle-samples/oracle-aidp-samples

⭐ 56 · Python · UPL-1.0 · 推送 2026-10-26 · [GitHub](https://github.com/oracle-samples/oracle-aidp-samples) · [官网](https://docs.oracle.com/en/cloud/paas/ai-data-platform/index.html) · 组织维护

**Oracle AI 数据平台工作台示例笔记本集（数据工程/ML/AI）**

由 Oracle 维护的示例笔记本合集，演示在其 AIDP Workbench（基于 Apache Spark 的数据工程、ML 与 AI 统一工作区）上构建数据管道与集成 AI 能力：覆盖 Delta Lake、Iceberg、多源数据摄取（Oracle 生态、SQL Server、BigQuery、Kafka 等）、Medallion 架构行业变体、数据血缘可视化、UniForm 元数据健康检查与 ADW Iceberg 外部表同步、PII 掩码等。面向使用 Oracle 云数据平台的开发者与数据工程师，需配合 AIDP 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | UPL-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖摄取/转换/血缘/流处理的数据工程示例目录
- Delta Lake、Iceberg、UniForm 跨格式互操作示例
- 12 个行业的 Medallion 架构与 Liquid Clustering 变体
- AI PII 掩码工具支持 Anthropic Claude 与 OCI 原生模型

## 适用场景

- 在 AIDP Workbench 上学习数据管道构建
- 从 Databricks 迁移笔记本与文件到 AIDP
- 维护 Delta UniForm 与 ADW Iceberg 外部表同步
- 用 AI 检测并掩码 DataFrame 中的 PII 列

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains a curated collection of sample notebooks demonstrating how to build data pipelines, run mac
> L7: Oracle AI Data Platform Workbench is a unified, governed workspace for building, managing, and deploying AI and data
> L165: |DataFrame PII Masking with AI|PySpark utility that detects and masks PII columns using a pluggable `PIIChecker` a

## 星数曲线

```mermaid
xychart-beta
    title "oracle-samples/oracle-aidp-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-27 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `124c045ef0f2` · [字段定义](../../DATASET.md)*
