# oripress/AlgoTune

⭐ 119 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/oripress/AlgoTune) · [官网](https://AlgoTune.io) · 个人维护

**NeurIPS 2025 基准：让 LLM 写出更快求解 154 个数理/CS 问题的代码**

由 154 个数学、物理、计算机科学函数构成的基准：对每个函数，目标是写出与原实现输出一致但更快的代码。配套提供 agent AlgoTuner，让语言模型自动优化代码，支持指定模型（如 o4-mini）在单任务或全部任务上运行。支持 SLURM 自动检测调度，并可经 AWS Batch 在云端提交任务（Spot/On-Demand 队列、S3 结果存储、ECR 仓库）。数据集从 HuggingFace 流式加载，也可本地生成后离线评估；支持在不运行 agent 的情况下单独评测代码，并可生成 AlgoTune.io 风格的 HTML 报告。面向从事 LLM 代码能力评测与算法优化研究的用户。

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

- 154 个数学/物理/计算机科学任务构成的速度优化基准
- AlgoTuner agent 让 LLM 自动生成更快实现
- 支持 SLURM 自动检测与 AWS Batch 云端运行（Spot 队列自动重试）
- 数据集可从 HuggingFace 流式加载或本地生成供离线评估

## 适用场景

- 评测语言模型编写更快数值算法的能力
- 研究者在集群或云端批量运行代码优化实验
- 为 AlgoTune 风格任务添加新基准题目并做 CI 校验

## 场景标签

`模型评测` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: How good are language models at coming up with new algorithms? To try to answer this, we built a benchmark, AlgoTun
> L22: ### ✨ **New:** AlgoTune can now be easily run on AWS with just an OpenRouter API key and AWS credentials. Try it ou

## 星数曲线

```mermaid
xychart-beta
    title "oripress/AlgoTune 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 117 --> 120
    line [118, 119, 119]
```

2026-10-18 118 → 2026-10-29 119（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `683d220d2a6d` · [字段定义](../../DATASET.md)*
