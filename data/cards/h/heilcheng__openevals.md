# heilcheng/openevals

⭐ 139 · Python · MIT · 推送 2025-12-29 · [GitHub](https://github.com/heilcheng/openevals) · [官网](http://haileycheng.com/openevals/) · 个人维护

**开源权重语言模型的评测基准框架（GSoC 2025 项目）**

面向大语言模型的系统化评测框架，支持在 MMLU、GSM8K、HumanEval 等 13 个学术基准上评测开源权重模型（Gemma、Llama、Mistral、Qwen、DeepSeek 及任意 HuggingFace 模型），测量延迟、吞吐与显存占用等效率指标，生成含置信区间的统计分析与可视化报告。提供 Python API、YAML 配置与浏览器端 Web 平台（含仪表盘与排行榜）。为 Google Summer of Code 2025 项目，由个人开发者完成、Google DeepMind 指导，需 Python 3.10+ 与 GPU（CUDA 11.8+），磁盘空间 50 GB 起且按模型规模要求 4-80GB 显存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个学术基准覆盖知识、数学、代码、推理、忠实度等类别
- 跨模型家族（Gemma/Llama/Mistral/Qwen/DeepSeek 等）对比评测
- 计算效率指标（延迟/吞吐/显存）与置信区间统计分析
- 提供 Python API、YAML 配置与 Web 平台（仪表盘/排行榜/报告导出）

## 适用场景

- 对开源权重模型做标准化基准评测与横向对比
- 测量模型推理的延迟、吞吐与显存占用
- 生成可用于论文的统计图表与报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: An open-source evaluation framework for large language models, providing systematic benchmarking across standardized
> L11: - Evaluating open-weight models on established benchmarks (MMLU, GSM8K, MATH, HumanEval, ARC, TruthfulQA, and more)
> L14: - Generating statistical analyses with confidence intervals

## 星数曲线

```mermaid
xychart-beta
    title "heilcheng/openevals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-29 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `437a9691a4dc` · [字段定义](../../DATASET.md)*
