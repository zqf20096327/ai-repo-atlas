# BauplanLabs/DBPLANBENCH

⭐ 33 · Python · MIT · 推送 2026-06-06 · [GitHub](https://github.com/BauplanLabs/DBPLANBENCH) · 组织维护

**用 LLM 进化采样优化 SQL 物理执行计划的论文复现工具**

复现论文《DBPLANBENCH: Test-Time Optimization of Physical Query Plans with LLMs》的代码库，由 Stanford、TogetherAI、Wisconsin-Madison 与 Bauplan 合作。以 Python API 编排流水线：LLM 以 JSON Patch 形式提出执行计划改写建议，在 Modal 云沙箱中运行打过补丁的 DataFusion 引擎做规划、执行与基准测试，结果写入 S3，并支持优化在不同数据规模间迁移。默认通过 LiteLLM 使用 GPT-5；支持 TPC-H/TPC-DS/JOIN ORDER BENCH 数据集，也可用 Rust 工具链本地构建引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 以 JSON Patch 形式提出物理执行计划优化建议
- Modal 云沙箱运行补丁版 DataFusion 引擎并写入 S3
- 优化可在不同数据集规模因子间迁移复用
- 内置合成 SQL 查询生成与计划基准对比

## 适用场景

- 研究生成 LLM 改写执行计划能否加速查询
- 对 TPC-H/TPC-DS/JOB 查询做计划级基准对比
- 将小规模数据上发现的优化迁移到更大规模

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L11: This repository provides tools for optimizing SQL query execution plans using LLM-driven evolutionary sampling. For
> L26: The **Python API** runs on your machine and orchestrates the entire pipeline. **Modal sandboxes** run the patched D

## 星数曲线

```mermaid
xychart-beta
    title "BauplanLabs/DBPLANBENCH 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `86157f4087cb` · [字段定义](../../DATASET.md)*
