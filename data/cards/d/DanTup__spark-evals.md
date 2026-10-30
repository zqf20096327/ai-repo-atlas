# DanTup/spark-evals

⭐ 51 · Shell · 推送 2026-08-23 · [GitHub](https://github.com/DanTup/spark-evals) · 个人维护

**DGX Spark 单机可容纳小模型与量化版本的评测结果集**

由个人维护的模型评测结果仓库：在单台 NVIDIA DGX Spark 上，通过 multipass 创建虚拟机并以 run_benchmarks.sh 运行评测，汇集 40 余个模型（含 FP8/NVFP4 量化版本）在 evo eval、aider polyglot、swe-rebench、bfcl、bigcodebench 等基准上的得分，并附带运行时长与输入输出 token 数。早期评测经 Inspect AI 运行，后切换到 Harbor。仓库为结果数据展示，不含安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 余个模型及量化版本在单台 DGX Spark 上的基准得分
- 记录各评测的运行时长与输入/输出 token 数
- 提供评测脚本 run_benchmarks.sh 与 multipass 虚拟机创建命令

## 适用场景

- 为 DGX Spark 选型可本地运行的小模型时查阅参考分数
- 比较同一模型不同量化格式（BF16/FP8/NVFP4）的得分差异

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Some basic evals run on various models that fit on a single DGX Spark.
> L9: |name|evo eval (codex)|evo eval (terminus-2)|aider polyglot (codex)|aider polyglot (terminus-2)|swe-rebench (codex)|
> L18: Below are scores from the original evals run via Inspect AI, before switching to Harbor.

## 星数曲线

```mermaid
xychart-beta
    title "DanTup/spark-evals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0b4c4ea8adbd` · [字段定义](../../DATASET.md)*
