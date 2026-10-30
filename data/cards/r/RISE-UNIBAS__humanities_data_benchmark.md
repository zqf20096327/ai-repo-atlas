# RISE-UNIBAS/humanities_data_benchmark

⭐ 31 · Python · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/RISE-UNIBAS/humanities_data_benchmark) · [官网](https://rise-services.rise.unibas.ch/benchmarks/) · 组织维护

**面向人文数据的 LLM 评测基准套件：转录、抽取与版面分析**

由巴塞尔大学 RISE 团队维护的数字人文 LLM 基准套件：收录 12 个基准（含中世纪手稿转录、Fraktur 广告转录、档案卡片结构化抽取、文档版面定位等任务），以图像与文本文件、提示词、标准答案和评分脚本形式提供，并记录成本与运行时间。支持通过 API key 调用 OpenAI、Google、Anthropic 等提供商，也可注册本地模型后端（DocLayout-YOLO、Grounding DINO、SAM 3 等）。每个基准附带 BenchmarkCard 说明来源、指标与版本，评分结果以 MAJOR.MINOR.PATCH 版本管理并可重算。需 Python 3.12+，从源码克隆运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个人文任务基准，覆盖转录、结构化抽取与版面分析
- 每个基准附 BenchmarkCard（来源、许可、指标、版本）
- 支持多家 API 提供商与可扩展的本地模型后端
- 结果含成本与运行时间记录，可生成独立 HTML 报告

## 适用场景

- 数字人文研究中比较不同 LLM 在历史文档任务上的表现
- 为文献转录或档案抽取任务选型模型
- 复用基准数据与评分脚本评估自研模型

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L5: This repository contains benchmark datasets (images and text files), prompts, ground truths, and evaluation
> L10: Tasks covered include transcription, structured information extraction, and document layout analysis, each scored
> L22: Benchmarking is the process of systematically evaluating and ranking various models for specific tasks using

## 星数曲线

```mermaid
xychart-beta
    title "RISE-UNIBAS/humanities_data_benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ef69844c266c` · [字段定义](../../DATASET.md)*
