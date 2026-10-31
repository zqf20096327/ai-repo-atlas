# filbench/filbench-eval

⭐ 13 · Python · 推送 2026-09-06 · [GitHub](https://github.com/filbench/filbench-eval) · [官网](https://huggingface.co/spaces/UD-Filipino/filbench-leaderboard) · 组织维护

**菲律宾语 LLM 评测基准与排行榜工具套件**

FilBench 的评测与实验仓库：包含覆盖文化知识、生成、阅读理解、经典 NLP 四类能力的菲律宾语评测基准，已评测 20+ 个模型。提供基于 Lighteval fork 的评测运行器与 filbench CLI，用于运行评测、计算 FilBench 分数并向排行榜提交结果（通过向结果数据集发 PR）。安装需 uv 与 Python 3.12，通过 git clone 与 submodule 方式部署。成果发表于 EMNLP 2025 Main。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类能力评测基准：文化知识/生成/阅读理解/经典 NLP
- 基于 Lighteval fork 的评测运行器，支持通过 vLLM 运行 HuggingFace 模型
- filbench CLI 计算分数并通过 PR 提交至排行榜

## 适用场景

- 评测 LLM 在菲律宾语上的能力并提交排行榜
- 复现或扩展菲律宾语 NLP 评测实验
- 为多语言模型选型提供菲律宾语基准参考

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: This repository contains all relevant tools and experiments for FilBench, an Open LLM Evaluation Suite and leaderboa
> L10: We curated an evaluation benchmark consisting of four major capabilities: Cultural Knowledge, Generation, Reading C
> L36: 1. **lighteval**: this is the main evaluation runner to use for launching evaluation jobs.

## 星数曲线

```mermaid
xychart-beta
    title "filbench/filbench-eval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1a9d73d0ca74` · [字段定义](../../DATASET.md)*
