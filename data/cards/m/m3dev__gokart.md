# m3dev/gokart

⭐ 342 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/m3dev/gokart) · [官网](https://gokart.readthedocs.io/en/latest/) · 组织维护

**基于 luigi 的 Python 机器学习流水线框架，解决可复现与任务依赖**

构建在 luigi 之上的 Python 批处理流水线框架：以 Task 类组织机器学习任务，为每个任务以 pkl 文件分别存储输出数据、模块版本、处理时间、随机种子与参数等元数据；参数变更时自动重跑流水线，支持 GCS/S3 作为中间结果存储，任务间以中间文件交换数据。并行任务通过 redis 加锁，自动固定 numpy/random 种子，支持 pandas.DataFrame 类型与列校验及 mypy 类型注解。限制：不支持任务可视化、不做实验管理（拆分至 Thunderbolt），I/O 与存储容量可能成为瓶颈。m3.inc 使用超过 3 年。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每任务以 pkl 文件存储输出/模块版本/参数/种子等元数据
- 参数变更自动重跑流水线，支持 GCS/S3 中间结果存储
- 任务间以中间文件交换数据，并行任务经 redis 锁定
- pandas.DataFrame 类型与列校验，支持类型注解的流水线

## 适用场景

- 构建可复现的机器学习批处理流水线
- 团队协作中追踪每个任务的参数、版本与运行记录
- 将中间结果存至 S3/GCS 并自动管理依赖重跑

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: Gokart solves reproducibility, task dependencies, constraints of good code, and ease of use for Machine Learning Pip
> L104: gokart is a wrapper for luigi. Thanks to luigi and dependent projects!

## 星数曲线

```mermaid
xychart-beta
    title "m3dev/gokart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 341 --> 343
    line [342, 342]
```

2026-10-18 342 → 2026-10-26 342（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dfb248830f42` · [字段定义](../../DATASET.md)*
